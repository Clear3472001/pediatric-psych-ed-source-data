import csv
import random
import math
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)
num_rows = 2500

# Base pools for generating attributes
genders = ["Male", "Female", "Non-Binary"]
gender_probs = [0.49, 0.49, 0.02]

payers = ["Medicaid", "Commercial BlueCross", "Commercial United", "Self-Pay/Uninsured"]
payer_probs = [0.55, 0.25, 0.15, 0.05]

arrival_modes = ["Walk-In", "Ambulance", "School Transport", "Police Escort"]
arrival_probs = [0.40, 0.35, 0.15, 0.10]

acuity_scores = [1, 2, 3, 4]
acuity_probs = [0.05, 0.65, 0.25, 0.05]

# Helper function for weighted random choice without numpy
def weighted_choice(choices, weights):
    return random.choices(choices, weights=weights, k=1)[0]

# Helper function to simulate a skewed distribution (gamma/exponential approximation)
def get_skewed_hours(base_scale, shift=0):
    # Using log-normal simulation with random math to create a realistic hospital bottleneck curve
    return math.exp(random.normalvariate(0.5, 0.7)) * base_scale + shift

# Generate rows
data_rows = []
for i in range(num_rows):
    encounter_id = 100001 + i
    patient_id = random.randint(50000, 99999)
    age = random.randint(5, 17)
    gender = weighted_choice(genders, gender_probs)
    payer = weighted_choice(payers, payer_probs)
    arrival_mode = weighted_choice(arrival_modes, arrival_probs)
    esi = weighted_choice(acuity_scores, acuity_probs)
    
    # Generate randomized triage base dates spanning the last 12 months
    random_days_back = random.randint(0, 365)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    triage_start = datetime(2025, 11, 1) + timedelta(days=random_days_back, hours=random_hours, minutes=random_minutes)
    
    # Time to medical clearance logic
    clearance_delay = get_skewed_hours(1.5)
    if arrival_mode == "Ambulance" or esi == 1:
        clearance_delay *= 0.7 # Faster clearance for critical cases
    med_cleared = triage_start + timedelta(hours=clearance_delay)
    
    # Admit decision timestamp
    admit_delay = random.uniform(0.1, 1.0)
    admit_decision = med_cleared + timedelta(hours=admit_delay)
    
    # Systemic bed bottleneck wait time simulation
    if random.random() < 0.25:
        bed_wait_hours = get_skewed_hours(12, shift=12) # Severe backlog simulation
    else:
        bed_wait_hours = get_skewed_hours(4, shift=2) # Standard backlog simulation
        
    # The Tipping Point logic: probability of family leaving matches the length of stay
    lwbs_prob = min(0.85, (bed_wait_hours / 96.0) * 0.6)
    
    if random.random() < lwbs_prob and bed_wait_hours > 4:
        # Family eloped / left before bed placement
        disposition = weighted_choice(["Left Without Being Seen", "Left Against Medical Advice"], [0.70, 0.30])
        actual_wait = random.uniform(2, bed_wait_hours)
        discharge = admit_decision + timedelta(hours=actual_wait)
        distance = "" # Blanks handle cleanly as NULL values in DuckDB
    else:
        # Successful bed placement
        disposition = weighted_choice(["Admitted Internally (Psych Unit)", "Transferred to External Facility"], [0.30, 0.70])
        discharge = admit_decision + timedelta(hours=bed_wait_hours)
        distance = round(math.exp(random.normalvariate(2.5, 0.8)), 1) if disposition == "Transferred to External Facility" else 0.0

    # Format datetimes cleanly for SQL parsers
    data_rows.append([
        encounter_id, patient_id, age, gender, payer, arrival_mode, esi,
        triage_start.strftime('%Y-%m-%d %H:%M:%S'),
        med_cleared.strftime('%Y-%m-%d %H:%M:%S'),
        admit_decision.strftime('%Y-%m-%d %H:%M:%S'),
        discharge.strftime('%Y-%m-%d %H:%M:%S'),
        disposition, distance
    ])

# Write output file straight to the data/ folder you already have created
output_filepath = "./data/pediatric_psych_boarding_raw.csv"

headers = [
    'encounter_id', 'patient_id', 'age', 'gender', 'payer_type', 'arrival_mode', 
    'emergency_severity_index', 'triage_start_datetime', 'medical_clearance_datetime', 
    'admit_decision_datetime', 'discharge_datetime', 'final_disposition', 'destination_facility_distance_miles'
]

with open(output_filepath, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data_rows)

print(f"Bypass script ran successfully! Generated mock data file at: {output_filepath}")
