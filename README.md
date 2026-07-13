# NES Smart Meter Analytics

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)

DLMS Smart Meter Data Analysis — Forecasting & Anomaly Detection for Power Distribution.

## Overview

This project analyzes smart meter data from NES Technologies to detect abnormal consumption patterns, forecast energy usage, and assess meter health across 5 commercial/industrial meters over 12 months.

| Metric | Value |
|--------|-------|
| Dataset | 5 meters x 12 months x 175,200 readings |
| Forecasting Model | LightGBM |
| MAPE | 0.72% |
| R² | 0.9997 |
| Anomalies Detected | 4,255 (2.4%) |
| Health Score Range | 85.6 - 88.5 |

## Repository Structure

```
nes-smart-meter-analytics/
├── notebooks/
│   └── NES_UC1_UC2_Integrated_final.ipynb   # Main analysis notebook
├── src/
│   └── build_corporate_ppt.py                # PPT generator
├── reports/
│   ├── NES_UC1_UC2_ppt.pdf                  # Executive presentation
│   └── NES_UC1_UC2_Integrated_final.html    # HTML notebook export
├── docs/
│   └── nes_logo_transparent.png              # Logo
├── requirements.txt                          # Python dependencies
├── LICENSE                                   # MIT License
└── README.md                                 # This file
```

## Setup

### Prerequisites

- Python 3.10 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yashitarora/nes-smart-meter-analytics.git
cd nes-smart-meter-analytics

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Data

The analysis uses two data files (not included in repository due to size):

1. `DLMS_5_Meters_Apr2025_Mar2026.csv` — 175,200 interval readings from 5 DLMS meters
2. `meter_event_5_Meters_DLMS.xlsx` — DLMS event logs (tamper, magnet, bypass events)

Contact NES Technologies for data access.

## Usage

### Run the Notebook

```bash
jupyter notebook notebooks/NES_UC1_UC2_Integrated_final.ipynb
```

### Generate Presentation

```bash
cd src
python build_corporate_ppt.py
```

Output: `reports/NES_UC1_UC2_ppt.pdf`

## Pipeline

| Step | Description | Key Output |
|------|-------------|------------|
| 1. Data Quality | Identify DLMS firmware artifacts | 87,387 issues (all artifacts) |
| 2. Per-Meter Behaviour | Daily load profiles, consumer classification | 5 unique load shapes |
| 3. Monthly Analysis | Peak load trends per meter | Distinct peak months |
| 4. Feature Engineering | Lag, interaction, weather features | 25 features, 5 groups |
| 5. Model Selection | LightGBM vs RF vs Linear Regression | LightGBM selected |
| 6. Forecast Validation | Test on 14,400 readings | MAPE=0.72%, R²=0.9997 |
| 7. Anomaly Detection | 6-algorithm ensemble voting | 4,255 anomalies (2.4%) |
| 8. UC2 to UC1 Handoff | Select timestamps for investigation | MTR005 @ 2025-11-06 13:30 |
| 9. UC1 Investigation | Electrical trend analysis | Normal industrial activity |
| 10. Health Assessment | 6-component weighted score | 85.6 - 88.5 |
| 11. Root Cause | Top 10 peak event analysis | Industrial Activity #1 (26.6%) |
| 12. Recommendations | 4 prioritized actions | Deploy pilot, monitor MTR001 |

## Key Findings

### Forecasting
- **LightGBM** outperforms Linear Regression (61% better) and Random Forest (79% better)
- Per-meter modelling required — each meter has unique daily profile
- Night low-load causes highest % errors but absolute errors remain <0.2 kW

### Anomaly Detection
- 4,255 anomalies detected (2.4% of readings)
- MTR005 (industrial) has highest count: 1,284 (3.66%)
- 31.5% of anomalies occur during night hours

### Root Cause Analysis
- Industrial Activity (26.6%) is #1 cause across top 10 peaks
- Commercial Behaviour (22.2%) is #2
- No theft or tampering detected — all DLMS events are firmware artifacts

### Health Assessment
- MTR003 (88.5) and MTR004 (88.3) are HEALTHY
- MTR001 (85.6) needs voltage monitoring
- Tamper score (55) derived from 9 DLMS events per meter

## Technology Stack

- **Python 3.10+**
- **LightGBM** — Primary forecasting model
- **scikit-learn** — Isolation Forest, LOF, OneClassSVM, DBSCAN, Random Forest
- **pandas / numpy** — Data manipulation
- **matplotlib / seaborn / plotly** — Visualization
- **python-pptx** — Presentation generation
- **Jupyter Notebook** — Analysis environment

## Author

**Yashit Arora**
- GitHub: [@yashitarora](https://github.com/yashitarora)

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- NES Technologies for DLMS meter data
- Use Case 1 (UC1): Investigation & Root Cause
- Use Case 2 (UC2): Behaviour Analysis & Anomaly Detection
