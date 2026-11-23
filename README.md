## Portfolio Context

This repository is Project 1 of a 9-project data engineering portfolio focused on psychiatric emergency department boarding analytics.

Subsequent projects transform this source data into an operational database, enterprise data warehouse, analytics layer, and cloud-based healthcare data platform.

# Project 1: Pediatric Psychiatric Emergency Department Source Data

## Overview

This project generates realistic synthetic data representing pediatric behavioral health patients presenting to an emergency department (ED) for psychiatric evaluation and placement. The dataset simulates the complete patient journey from triage through medical clearance, psychiatric placement decisions, and final disposition.

The primary focus is pediatric psychiatric boarding, a widespread healthcare operational challenge in which pediatric patients remain in emergency departments for extended periods while awaiting available inpatient psychiatric beds.

This dataset serves as the foundation for the remaining projects in the portfolio, supporting database design, ETL development, data warehousing, analytics engineering, business intelligence reporting, and cloud data platform implementation.

---

## Business Problem

Children experiencing psychiatric emergencies often require admission to specialized behavioral health facilities. Due to limited inpatient capacity, many remain boarded in emergency departments long after medical clearance.

Extended boarding creates challenges including:

- Increased emergency department overcrowding
- Delayed access to definitive psychiatric care
- Increased transfer distances to available facilities
- Higher rates of patient and family dissatisfaction
- Greater likelihood of patients leaving before placement

This project simulates these real-world operational challenges using synthetic healthcare data.

---

## Dataset Description

The generated dataset contains **2,500 pediatric psychiatric emergency department encounters** covering approximately one year of activity.

Each record represents a unique emergency department encounter and tracks the patient's progression through key clinical and operational milestones.

### Sample Workflow

```text
ED Arrival
    ↓
Triage Assessment
    ↓
Medical Clearance
    ↓
Psychiatric Admission Decision
    ↓
Bed Search / Boarding Period
    ↓
Final Disposition
```

---

## Data Model

### Patient Demographics

| Column | Description |
|----------|-------------|
| patient_id | Unique patient identifier |
| age | Patient age (5-17 years) |
| gender | Male, Female, or Non-Binary |
| payer_type | Insurance coverage type |

### Encounter Information

| Column | Description |
|----------|-------------|
| encounter_id | Unique encounter identifier |
| arrival_mode | Walk-In, Ambulance, School Transport, or Police Escort |
| emergency_severity_index | Emergency Severity Index (ESI) score |

### Clinical Timeline

| Column | Description |
|----------|-------------|
| triage_start_datetime | Initial ED triage timestamp |
| medical_clearance_datetime | Medical clearance completion timestamp |
| admit_decision_datetime | Psychiatric admission decision timestamp |
| discharge_datetime | Final disposition timestamp |

### Outcome Fields

| Column | Description |
|----------|-------------|
| final_disposition | Encounter outcome |
| destination_facility_distance_miles | Distance to receiving psychiatric facility |

---

## Simulated Operational Logic

The data generator introduces realistic healthcare workflow behavior and operational bottlenecks.

### Medical Clearance

Critical patients arriving by ambulance or assigned higher acuity scores generally move through the medical clearance process more quickly than lower-acuity patients.

### Psychiatric Boarding

After medical clearance and admission decision, patients enter a simulated boarding period while awaiting psychiatric placement.

Two operational scenarios are modeled:

#### Standard Capacity Environment

Patients experience moderate waits for placement.

#### Behavioral Health Capacity Crisis

A subset of encounters experience extreme boarding periods caused by severe inpatient bed shortages.

### Family Attrition Model

As boarding times increase, the probability of patients leaving before psychiatric placement also increases.

Possible outcomes include:

- Left Without Being Seen (LWBS)
- Left Against Medical Advice (AMA)

This mirrors real-world emergency department behavior where prolonged wait times significantly impact patient retention.

### Placement Outcomes

Patients who remain in care are either:

- Admitted to an internal psychiatric unit
- Transferred to an external behavioral health facility

Transfer distances are simulated using a skewed distribution to reflect regional shortages of pediatric psychiatric beds.

---

## Key Metrics Supported

This dataset enables analysis of several healthcare operational metrics.

### Throughput Metrics

- Time to Medical Clearance
- Time to Admission Decision
- Boarding Hours
- Total Length of Stay

### Quality Metrics

- Left Without Being Seen Rate
- Left Against Medical Advice Rate
- Admission Rate
- Transfer Rate

### Capacity Metrics

- Average Boarding Duration
- Median Boarding Duration
- Psychiatric Placement Delays
- Facility Transfer Distances

### Population Metrics

- Boarding by Age Group
- Boarding by Payer Type
- Boarding by Arrival Mode
- Boarding by Acuity Level

---

## Technology Stack

- Python
- CSV
- Randomized Data Generation
- Healthcare Workflow Simulation

---

## Repository Structure

```text
pediatric-psych-ed-source-data/
│
├── data/
│   └── pediatric_psych_boarding_raw.csv
│
├── scripts/
│   └── generate_pediatric_psych_data.py
│
├── docs/
│   └── data_dictionary.md
│
└── README.md
```

---

## Portfolio Roadmap

This repository serves as the source system for the complete Pediatric Psychiatric Emergency Department Analytics Platform:

1. Pediatric Psych ED Source Data
2. Pediatric Psych ED Database Design
3. Pediatric Psych ED ETL Pipeline
4. Pediatric Psych ED Data Warehouse
5. Pediatric Psych ED Warehouse ETL
6. Pediatric Psych ED dbt Transformations
7. Pediatric Psych ED Analytics & BI
8. Pediatric Psych ED Cloud Lakehouse
9. Pediatric Psych ED Data Platform

---

## Learning Objectives

Through this project, I demonstrate how synthetic healthcare data can be generated to model realistic operational challenges and support downstream analytics initiatives. The resulting dataset provides a consistent foundation for showcasing database design, data engineering, analytics engineering, and cloud architecture skills within a healthcare-focused portfolio.

---

## Author

**Crystal Thomas**

Data Engineering Portfolio

Specialization Areas:

- Healthcare Analytics
- Data Engineering
- Data Warehousing
- Analytics Engineering
- Cloud Data Platforms
- Behavioral Health Operations
