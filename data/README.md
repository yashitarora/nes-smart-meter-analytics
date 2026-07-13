# Data Directory

This directory contains the raw data files used for analysis.

## Required Files

| File | Description | Size |
|------|-------------|------|
| `DLMS_5_Meters_Apr2025_Mar2026.csv` | Interval readings from 5 DLMS meters | ~14 MB |
| `meter_event_5_Meters_DLMS.xlsx` | DLMS event logs (tamper, magnet, bypass) | ~16 KB |
| `weather_2025_2026.csv` | Weather data for the analysis period | ~14 KB |

## Data Source

Contact NES Technologies for data access.

## Usage

Place the data files in this directory before running the notebook.

```bash
cd data
# Place your data files here
cd ..
jupyter notebook notebooks/NES_UC1_UC2_Integrated_final.ipynb
```

## Data Format

### DLMS_5_Meters_Apr2025_Mar2026.csv

- **Meter_ID**: MTR001-MTR005
- **Timestamp**: 15-minute intervals
- **Import_Energy_kWh**: Cumulative energy
- **Voltage_L1_V**: Line voltage
- **Current_L1_A**: Line current
- **Power_Factor**: Power factor

### meter_event_5_Meters_DLMS.xlsx

- **Meter_ID**: MTR001-MTR005
- **Timestamp**: Event timestamp
- **Event**: Event type (tamper, magnet, bypass, etc.)
