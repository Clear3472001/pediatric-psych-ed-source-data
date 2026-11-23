# Data Dictionary

| Field | Data Type | Description |
|---------|----------|-------------|
| encounter_id | Integer | Unique encounter identifier |
| patient_id | Integer | Unique patient identifier |
| age | Integer | Patient age in years |
| gender | String | Gender identity |
| payer_type | String | Insurance coverage |
| arrival_mode | String | Method of arrival |
| emergency_severity_index | Integer | ESI triage score |
| triage_start_datetime | Timestamp | Start of ED encounter |
| medical_clearance_datetime | Timestamp | Medical clearance timestamp |
| admit_decision_datetime | Timestamp | Admission decision timestamp |
| discharge_datetime | Timestamp | Encounter completion timestamp |
| final_disposition | String | Outcome of encounter |
| destination_facility_distance_miles | Decimal | Transfer distance |