# Who Falls Through the Cracks?

**Healthcare Access Barriers Analysis · DubsTech Datathon 2026**

[![View Live Site](https://img.shields.io/badge/View-Live%20Site-2a9d8f?style=for-the-badge)](https://your-username.github.io/datathon-2026/)
[![Download Data](https://img.shields.io/badge/Download-Tableau%20Data-e63946?style=for-the-badge)](data/tableau_exports/)

---

## Team: Accessible Infinity Tunnel

| Member | Role | GitHub |
|--------|------|--------|
| **AJ Plumlee** | ML Lead (2026 Forecasts) | [@ajplumlee33](https://github.com/ajplumlee33) |
| **Alanna Koser** | ML Lead (2025 Forecasts) | [@0-1deathtouch](https://github.com/0-1deathtouch) |
| **Josiah Zacharias** | Visualization Lead | [@jomandaman](https://github.com/jomandaman) |

---

## Project Overview

An analysis of healthcare access barriers across race, income, and education — examining how the pandemic temporarily narrowed gaps that are now at risk of widening again.

**Three Core Questions:**
1. **Disparities Snapshot** — Which subgroups have the highest rates of delayed/unmet care?
2. **COVID Impact** — Did disparities widen during COVID? Have they recovered?
3. **Predictive Modeling** — Who's most at risk of falling through the cracks next year?

**Key Findings:**
- Uninsured adults face barriers **3-5× higher** than those with private insurance
- COVID-era policies temporarily cut the poverty gap in half (10.3pp → 5.0pp)
- Bisexual adults and AI/AN populations predicted to face **significant worsening** by 2026

---

## Live Demo

**[View the Interactive Site →](https://jomandaman.github.io/datathon-2026/)**

Features:
- Scroll-based narrative with interactive Plotly visualizations
- Dual ML forecasting (2025 short-term + 2026 long-term predictions)
- Explore disparities across 5 demographic lenses
- COVID impact analysis with gap-closing metrics
- Download Tableau-ready CSV exports

---

## Project Structure

```
datathon-2026/
├── index.html                              # Main GitHub Pages site
├── notebooks/
│   ├── ait_datathon.ipynb                 # AJ's ML notebook (2026 forecasts)
│   └── Accessible_Infinity_Tunnel_*.ipynb # Alanna's ML notebook (2025 forecasts)
├── data/
│   ├── Access_to_Care_Dataset.csv         # Raw CDC NHIS data (2019-2024)
│   └── tableau_exports/                   # Cleaned CSVs for Tableau/Power BI
│       ├── healthcare_access_barriers_full.csv
│       ├── time_series_trends.csv
│       ├── disparities_2024_snapshot.csv
│       ├── disparity_gaps.csv
│       ├── ml_forecasts_2025_2026.csv
│       └── yearly_summary_statistics.csv
├── scripts/
│   └── export_for_tableau.py              # Generates Tableau-ready CSVs
├── TABLEAU_GUIDE.md                       # Guide for Tableau Public integration
└── README.md                              # You are here
```

---

## Methodology

### Data Source
**CDC National Health Interview Survey (NHIS)** — Adult Summary Health Statistics, 2019-2024
- 26,208 total records → 23,609 after cleaning (removed unreliable estimates)
- 54 health topics across demographic, socioeconomic, and geographic classifications
- Focused on 4 access barrier types:
  - Delayed getting medical care due to cost
  - Did not get needed medical care due to cost
  - Did not get needed mental health care due to cost
  - Did not take medication as prescribed to save money

### Machine Learning Models

**Model 1: Short-term (2025 Forecast)** — *Alanna's Gradient Boosting Model*
- **R² Score:** 0.87
- **Features:** Lag values, rolling averages, year-over-year changes, confidence interval widths
- **Training:** 2019-2024 data with engineered temporal features
- **Output:** 1-year predictions for all demographic subgroups

**Model 2: Long-term (2026 Forecast)** — *AJ's XGBoost Model*
- **R² Score:** 0.87
- **Training Strategy:** 2-year jump patterns (2019→2021, 2020→2022, etc.)
- **Output:** 2-year projections identifying most at-risk populations with interpretability analysis

---

## Key Visualizations

### 1. Disparities Snapshot
- **Bubble plot** showing all 5 demographic categories simultaneously
- **Interactive time series** with scroll-based animation (2019→2024)
- **Heatmap** of barrier rates by subgroup (2024)
- **Area plot** showing gaps between highest/lowest subgroups

### 2. COVID Impact
- **Gap-closing analysis** — Poverty-based disparities narrowed during pandemic
- **Gap-not-closing analysis** — Racial insurance disparities remained entrenched
- Shaded regions marking COVID-era policy interventions

### 3. Predictive Modeling
- **Dual forecast visualization** — Compare 2025 vs 2026 predictions
- **Demographic lens filters** — View by race, income, disability, sexual orientation, or geography
- **Change annotations** — Red for worsening, green for improving
- **Model transparency** — Show R² scores and training status

---

## Running Locally

### Prerequisites
- Python 3.8+
- Modern web browser

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/jomandaman/datathon-2026.git
   cd datathon-2026
   ```

2. **View the site**
   ```bash
   # Option 1: Python HTTP server
   python -m http.server 8000

   # Option 2: Open directly
   open index.html
   ```

3. **Visit:** http://localhost:8000

### Regenerate Tableau Exports

```bash
python scripts/export_for_tableau.py
```

This creates 6 CSV files in `data/tableau_exports/` ready for Tableau Public, Power BI, or Excel.

---

## Data Downloads

All datasets are available in the **"Extend This Analysis"** section of the live site.

**Quick links:**
- [Full Dataset (CSV)](data/tableau_exports/healthcare_access_barriers_full.csv) — 1,807 rows
- [Time Series Trends](data/tableau_exports/time_series_trends.csv) — 1,783 rows
- [2024 Snapshot](data/tableau_exports/disparities_2024_snapshot.csv) — 307 rows
- [Disparity Gaps](data/tableau_exports/disparity_gaps.csv) — 480 rows
- [ML Forecasts (2025 & 2026)](data/tableau_exports/ml_forecasts_2025_2026.csv) — 30 rows
- [Summary Statistics](data/tableau_exports/yearly_summary_statistics.csv) — 24 rows

**For Tableau users:** See [TABLEAU_GUIDE.md](TABLEAU_GUIDE.md) for step-by-step instructions on recreating our visualizations.

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **Plotly.js** | Interactive data visualizations |
| **GitHub Pages** | Static site hosting |
| **Python (Pandas, NumPy)** | Data cleaning and feature engineering |
| **scikit-learn** | Gradient Boosting, Random Forest models |
| **XGBoost** | Ensemble modeling for 2026 forecasts |
| **Google Colab** | Collaborative notebook environment |

---

## Design Philosophy

Our visualization approach prioritizes:
- **Narrative clarity** — Scroll-based storytelling guides users through insights
- **Data honesty** — Show confidence intervals, gaps, and model limitations
- **Accessibility** — High contrast, readable fonts, semantic HTML
- **Interactivity** — Dropdowns, hover tooltips, and responsive charts
- **Reproducibility** — All code and data are open for extension

---

## Extending This Analysis

### Use Our Data in Tableau/Power BI
1. Download CSV exports from the site or `data/tableau_exports/`
2. Follow our [Tableau Guide](TABLEAU_GUIDE.md)
3. Recreate visualizations or build your own dashboards

### Explore the Notebooks
- **AJ's Notebook** — 2026 forecasting with ensemble methods
- **Alanna's Notebook** — 2025 predictions + feature engineering

### Fork and Extend
```bash
git clone https://github.com/YOUR_USERNAME/datathon-2026.git
# Add new models, data sources, or visualizations
# Submit a PR to share your improvements!
```

---

## Acknowledgments

**Data Source:** CDC National Health Interview Survey (NHIS), 2019-2024

**Built for:** [DubsTech Datathon 2026](https://datathon-2026.webflow.io/) — University of Washington, February 7-8, 2026

**Inspiration:** Winning projects from previous datathons that emphasized visual storytelling and data accessibility

---

## License

This project is open source and available under the MIT License.

**Citation:**
```
Accessible Infinity Tunnel (2026). "Who Falls Through the Cracks?
Healthcare Access Barriers Analysis 2019-2024."
DubsTech Datathon 2026, University of Washington.
```

---

## Contact

Questions or want to collaborate?

- **AJ Plumlee** — [GitHub](https://github.com/ajplumlee33)
- **Alanna Koser** — [GitHub](https://github.com/0-1deathtouch)
- **Josiah Zacharias** — [GitHub](https://github.com/jomandaman)

---

<p align="center">
  <strong>Built with ❤️ for DubsTech Datathon 2026</strong><br>
  Accessible Infinity Tunnel · University of Washington
</p>
