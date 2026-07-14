# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.0] - 2025-07-14

### Added

#### Core Analysis
- Data quality assessment with DLMS artifact detection (87,387 issues)
- Per-meter behaviour analysis with daily load profiles
- Consumer classification using 4 evidence dimensions
- Monthly peak load analysis across 12 months
- Feature engineering: 25 features across 5 groups (lag, interaction, weather, calendar, rolling)

#### Machine Learning
- LightGBM forecasting model (MAPE=0.72%, R²=0.9997)
- Model comparison: LightGBM vs Random Forest vs Linear Regression
- Per-meter accuracy validation on 14,400 test readings
- Forecast error analysis with root cause identification

#### Anomaly Detection
- 6-algorithm ensemble: Isolation Forest, LOF, OneClassSVM, DBSCAN, Z-score, IQR
- 4,255 anomalies detected (2.4% of readings)
- Anomaly severity scoring (0-4 scale)
- Night concentration analysis (31.5%)

#### Investigation Pipeline
- UC2 → UC1 handoff workflow
- Electrical trend analysis (V, I, PF, kW)
- Before → Event → After comparison
- Root cause analysis: Top 10 peak events

#### Health Assessment
- 6-component health score: Commercial, Voltage, PF, Anomaly, Tamper, Forecast
- Weighted formula with business-prioritized factors
- Per-meter health status: HEALTHY (≥88) / MONITOR (85-88) / CRITICAL (<85)

#### Presentation
- 16-slide executive presentation (PDF)
- Chart readability improvements for projector display
- Professional dark navy theme

#### Repository
- GitHub Actions CI workflow
- MIT License
- Comprehensive README with chart screenshots
- Data format documentation
- Contributing guidelines

### Technical Details
- **Dataset**: 5 meters × 12 months × 175,200 readings
- **Model**: LightGBM (n_estimators=300, learning_rate=0.1)
- **Anomalies**: 4,255 (2.4%) — MTR005 highest at 1,284 (3.66%)
- **Health Scores**: MTR001=85.6, MTR002=87.9, MTR003=88.5, MTR004=88.3, MTR005=86.4
- **Root Cause**: Industrial Activity (26.6%), Commercial Behaviour (22.2%)
