# Data Dictionary

## DLMS Meter Data (`DLMS_5_Meters_Apr2025_Mar2026.csv`)

| Column | Type | Description | Unit | Range |
|--------|------|-------------|------|-------|
| `Meter_ID` | string | Unique meter identifier | - | MTR001-MTR005 |
| `Timestamp` | datetime | Reading timestamp (15-min intervals) | - | 2025-04-01 to 2026-03-31 |
| `Import_Energy_kWh` | float | Cumulative imported energy | kWh | 0-99999 |
| `Voltage_L1_V` | float | Line-to-neutral voltage | V | 200-260 |
| `Current_L1_A` | float | Line current | A | 0-50 |
| `Power_Factor` | float | Power factor (displacement) | - | 0-1 |

### Derived Columns (Created in Notebook)

| Column | Formula | Description |
|--------|---------|-------------|
| `Active_Power_kW` | `V × I × PF / 1000` | Instantaneous active power |
| `Energy_Diff_kWh` | `Δ Import_Energy` | Interval energy consumption |
| `Hour` | `Timestamp.hour` | Hour of day (0-23) |
| `DayOfWeek` | `Timestamp.dayofweek` | Day of week (0=Mon, 6=Sun) |
| `Month` | `Timestamp.month` | Month (1-12) |
| `Is_Weekend` | `DayOfWeek >= 5` | Weekend flag |

---

## DLMS Event Log (`meter_event_5_Meters_DLMS.xlsx`)

| Column | Type | Description |
|--------|------|-------------|
| `Meter_ID` | string | Unique meter identifier |
| `Timestamp` | datetime | Event timestamp |
| `Event` | string | Event type |

### Event Types

| Event | Description | Impact |
|-------|-------------|--------|
| `magnet` | Magnetic tamper detected | Security concern |
| `tamper` | Physical tamper detected | Security concern |
| `bypass` | Bypass attempt detected | Security concern |
| `power_failure` | Power outage | Operational |
| `low_battery` | Battery low | Maintenance |
| `clock_error` | RTC clock error | Operational |

---

## Weather Data (`weather_2025_2026.csv`)

| Column | Type | Description | Unit |
|--------|------|-------------|------|
| `date` | date | Observation date | - |
| `temperature` | float | Average temperature | °C |
| `humidity` | float | Average humidity | % |

---

## Meter IDs

| Meter | Consumer Type | Base Load | Load Factor | Night/Day Ratio |
|-------|---------------|-----------|-------------|-----------------|
| MTR001 | Residential | 0.993 kW | 0.472 | 0.40 |
| MTR002 | Small Commercial | 1.486 kW | 0.498 | 0.49 |
| MTR003 | Workshop | 2.000 kW | 0.543 | 0.55 |
| MTR004 | Office | 2.507 kW | 0.581 | 0.60 |
| MTR005 | Industrial | 3.021 kW | 0.609 | 0.64 |

---

## Health Score Components

| Component | Weight | Formula | Range |
|-----------|--------|---------|-------|
| Commercial Fit | 20% | `Peak / Mean ratio` | 0-100 |
| Voltage Quality | 20% | `100 - (std × 5)` | 0-100 |
| Power Factor | 20% | `Average PF × 100` | 0-100 |
| Anomaly Score | 20% | `100 - (anomaly_rate × 5)` | 0-100 |
| Tamper Score | 10% | `100 - (events × 5)` | 0-100 |
| Forecast Error | 10% | `100 - (MAPE × 5)` | 0-100 |

### Health Status Thresholds

| Status | Score Range | Action |
|--------|-------------|--------|
| HEALTHY | ≥ 88 | No action required |
| MONITOR | 85 - 88 | Monitor periodically |
| CRITICAL | < 85 | Immediate investigation |
