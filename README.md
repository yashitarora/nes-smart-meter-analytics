# NES Smart Meter Analytics

DLMS Smart Meter Data Analysis — Forecasting & Anomaly Detection for Power Distribution.

## Project Overview

- **Scope**: 5 meters x 12 months x 175,200 readings
- **Model**: LightGBM | MAPE = 0.72% | R2 = 0.9997
- **Anomaly Detection**: 4,255 anomalies (2.4%) | 6-algorithm ensemble
- **Health Score Range**: 85.6 - 88.5 | No critical meters

## Repository Contents

| File | Description |
|------|-------------|
| `NES_UC1_UC2_Integrated_final.ipynb` | Main Jupyter Notebook — UC1 + UC2 analysis (184 cells, 0 errors) |
| `NES_UC1_UC2_Integrated_final.html` | HTML export of the notebook |
| `NES_UC1_UC2_ppt.pdf` | Executive presentation (16 slides) |
| `build_corporate_ppt.py` | Python script to generate the PPTX presentation |

## Pipeline

1. Data Quality Assessment
2. Per-Meter Behaviour Analysis
3. Monthly Analysis
4. Feature Engineering
5. Model Selection (LightGBM)
6. Forecast Validation
7. UC2 Anomaly Detection
8. UC2 to UC1 Handoff
9. UC1 Investigation
10. Meter Health Assessment
11. Root Cause Analysis
12. Conclusions & Recommendations

## Key Results

- **LightGBM** selected over Linear Regression (61% better) and Random Forest (79% better)
- **Per-meter modelling** required — each meter has distinct daily load profile
- **No theft detected** — all DLMS events are firmware artifacts
- **MTR001** needs voltage monitoring (Health Score = 85.6)

## Author

Yashit Arora
