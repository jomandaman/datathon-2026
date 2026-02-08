"""
Export cleaned data to Tableau-ready CSV formats
Creates multiple CSV files optimized for Tableau Public dashboards
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Create output directory
output_dir = Path(__file__).parent.parent / 'data' / 'tableau_exports'
output_dir.mkdir(exist_ok=True)

print("Loading raw data...")
df = pd.read_csv('data/Access_to_Care_Dataset.csv')

# Clean the data (same process as in notebooks)
essential_cols = [
    'TOPIC', 'TAXONOMY', 'CLASSIFICATION', 'GROUP', 'SUBGROUP',
    'TIME_PERIOD', 'ESTIMATE', 'ESTIMATE_LCI', 'ESTIMATE_UCI'
]
df = df[essential_cols].dropna(subset=['ESTIMATE'])

# Focus on access barrier topics
access_topics = [
    'Delayed getting medical care due to cost among adults',
    'Did not get needed medical care due to cost',
    'Did not get needed mental health care due to cost',
    'Did not take medication as prescribed to save money'
]
df_access = df[df['TOPIC'].isin(access_topics)].copy()

print(f"Cleaned data: {len(df_access):,} rows")

# ============================================================
# EXPORT 1: Full Access Barriers Dataset
# ============================================================
print("\n1. Exporting full access barriers dataset...")
df_access.to_csv(output_dir / 'healthcare_access_barriers_full.csv', index=False)
print(f"   ✓ Saved: healthcare_access_barriers_full.csv ({len(df_access):,} rows)")

# ============================================================
# EXPORT 2: Time Series View (for trend charts)
# ============================================================
print("\n2. Exporting time series view...")
# Keep only non-overlapping demographic groups
time_series_classifications = ['Demographic Characteristic', 'Socioeconomic Characteristic', 'Geographic Characteristic']
df_timeseries = df_access[df_access['CLASSIFICATION'].isin(time_series_classifications)].copy()

# Add barrier type category
df_timeseries['Barrier_Type'] = df_timeseries['TOPIC'].map({
    'Delayed getting medical care due to cost among adults': 'Delayed Care',
    'Did not get needed medical care due to cost': 'No Medical Care',
    'Did not get needed mental health care due to cost': 'No Mental Health Care',
    'Did not take medication as prescribed to save money': 'Skipped Medication'
})

df_timeseries.to_csv(output_dir / 'time_series_trends.csv', index=False)
print(f"   ✓ Saved: time_series_trends.csv ({len(df_timeseries):,} rows)")

# ============================================================
# EXPORT 3: 2024 Snapshot (for current disparities)
# ============================================================
print("\n3. Exporting 2024 snapshot...")
df_2024 = df_access[df_access['TIME_PERIOD'] == 2024].copy()
df_2024['Barrier_Type'] = df_2024['TOPIC'].map({
    'Delayed getting medical care due to cost among adults': 'Delayed Care',
    'Did not get needed medical care due to cost': 'No Medical Care',
    'Did not get needed mental health care due to cost': 'No Mental Health Care',
    'Did not take medication as prescribed to save money': 'Skipped Medication'
})

df_2024.to_csv(output_dir / 'disparities_2024_snapshot.csv', index=False)
print(f"   ✓ Saved: disparities_2024_snapshot.csv ({len(df_2024):,} rows)")

# ============================================================
# EXPORT 4: Disparity Gaps (Max - Min per group)
# ============================================================
print("\n4. Calculating disparity gaps...")
gaps_data = []

for year in df_access['TIME_PERIOD'].unique():
    for topic in access_topics:
        for group in df_access['GROUP'].unique():
            subset = df_access[
                (df_access['TIME_PERIOD'] == year) &
                (df_access['TOPIC'] == topic) &
                (df_access['GROUP'] == group)
            ]

            if len(subset) > 1:  # Need at least 2 subgroups to calculate gap
                max_val = subset['ESTIMATE'].max()
                min_val = subset['ESTIMATE'].min()
                gap = max_val - min_val

                max_subgroup = subset.loc[subset['ESTIMATE'].idxmax(), 'SUBGROUP']
                min_subgroup = subset.loc[subset['ESTIMATE'].idxmin(), 'SUBGROUP']

                gaps_data.append({
                    'Year': year,
                    'Barrier_Type': topic.replace(' among adults', '').replace('Did not get needed ', 'No ').replace('Did not take ', 'Skipped '),
                    'Demographic_Group': group,
                    'Highest_Subgroup': max_subgroup,
                    'Highest_Rate': max_val,
                    'Lowest_Subgroup': min_subgroup,
                    'Lowest_Rate': min_val,
                    'Disparity_Gap': gap
                })

df_gaps = pd.DataFrame(gaps_data)
df_gaps.to_csv(output_dir / 'disparity_gaps.csv', index=False)
print(f"   ✓ Saved: disparity_gaps.csv ({len(df_gaps):,} rows)")

# ============================================================
# EXPORT 5: 2025 & 2026 Forecasts (from models)
# ============================================================
print("\n5. Exporting forecast predictions...")

# 2025 predictions (Alanna's model)
forecast_2025 = [
    # Demographic
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Demographic', 'Subgroup': 'Bisexual adults', 'Actual_2024': 19.7, 'Predicted': 21.8, 'Change': 2.1},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Demographic', 'Subgroup': 'American Indian/Alaska Native', 'Actual_2024': 10.3, 'Predicted': 11.6, 'Change': 1.3},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Demographic', 'Subgroup': 'Black only, non-Hispanic', 'Actual_2024': 8.7, 'Predicted': 9.8, 'Change': 1.1},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Demographic', 'Subgroup': 'Hispanic adults', 'Actual_2024': 9.5, 'Predicted': 10.4, 'Change': 0.9},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Demographic', 'Subgroup': 'Living with a partner', 'Actual_2024': 13.1, 'Predicted': 11.9, 'Change': -1.2},
    # Socioeconomic
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Socioeconomic', 'Subgroup': 'High social vulnerability', 'Actual_2024': 8.8, 'Predicted': 10.1, 'Change': 1.3},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Socioeconomic', 'Subgroup': 'Uninsured', 'Actual_2024': 26.8, 'Predicted': 28.1, 'Change': 1.3},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Socioeconomic', 'Subgroup': 'Living with a partner', 'Actual_2024': 10.4, 'Predicted': 11.5, 'Change': 1.1},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Socioeconomic', 'Subgroup': 'Some college', 'Actual_2024': 9.1, 'Predicted': 8.6, 'Change': -0.5},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Socioeconomic', 'Subgroup': 'Married', 'Actual_2024': 6.7, 'Predicted': 5.9, 'Change': -0.8},
    # Geographic
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Geographic', 'Subgroup': 'South region', 'Actual_2024': 9.2, 'Predicted': 10.1, 'Change': 0.9},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Geographic', 'Subgroup': 'West region', 'Actual_2024': 8.5, 'Predicted': 9.2, 'Change': 0.7},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Geographic', 'Subgroup': 'Midwest region', 'Actual_2024': 7.8, 'Predicted': 8.3, 'Change': 0.5},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Geographic', 'Subgroup': 'Northeast region', 'Actual_2024': 7.1, 'Predicted': 7.5, 'Change': 0.4},
    {'Year': 2025, 'Model': 'Gradient Boosting', 'Classification': 'Geographic', 'Subgroup': 'Rural areas', 'Actual_2024': 8.6, 'Predicted': 9.0, 'Change': 0.4},
]

# 2026 predictions (AJ's model)
forecast_2026 = [
    # Demographic
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Demographic', 'Subgroup': 'Bisexual adults', 'Actual_2024': 23.1, 'Predicted': 25.8, 'Change': 2.7},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Demographic', 'Subgroup': 'American Indian/Alaska Native', 'Actual_2024': 13.8, 'Predicted': 15.9, 'Change': 2.1},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Demographic', 'Subgroup': 'Native Hawaiian/Pacific Islander', 'Actual_2024': 14.6, 'Predicted': 16.4, 'Change': 1.8},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Demographic', 'Subgroup': 'Hispanic adults', 'Actual_2024': 10.5, 'Predicted': 11.9, 'Change': 1.4},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Demographic', 'Subgroup': 'Gay or Lesbian adults', 'Actual_2024': 10.4, 'Predicted': 11.6, 'Change': 1.2},
    # Socioeconomic
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Socioeconomic', 'Subgroup': 'Below 100% FPL', 'Actual_2024': 13.1, 'Predicted': 15.2, 'Change': 2.1},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Socioeconomic', 'Subgroup': 'No high school diploma', 'Actual_2024': 12.4, 'Predicted': 14.1, 'Change': 1.7},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Socioeconomic', 'Subgroup': '100-200% FPL', 'Actual_2024': 11.8, 'Predicted': 13.2, 'Change': 1.4},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Socioeconomic', 'Subgroup': 'Some college, no degree', 'Actual_2024': 9.8, 'Predicted': 11.0, 'Change': 1.2},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Socioeconomic', 'Subgroup': 'Unemployed', 'Actual_2024': 11.5, 'Predicted': 12.6, 'Change': 1.1},
    # Geographic
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Geographic', 'Subgroup': 'South region', 'Actual_2024': 9.8, 'Predicted': 11.3, 'Change': 1.5},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Geographic', 'Subgroup': 'West region', 'Actual_2024': 8.9, 'Predicted': 10.2, 'Change': 1.3},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Geographic', 'Subgroup': 'Midwest region', 'Actual_2024': 8.2, 'Predicted': 9.3, 'Change': 1.1},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Geographic', 'Subgroup': 'Northeast region', 'Actual_2024': 7.5, 'Predicted': 8.4, 'Change': 0.9},
    {'Year': 2026, 'Model': 'XGBoost', 'Classification': 'Geographic', 'Subgroup': 'Rural areas', 'Actual_2024': 9.1, 'Predicted': 10.0, 'Change': 0.9},
]

df_forecasts = pd.DataFrame(forecast_2025 + forecast_2026)
df_forecasts.to_csv(output_dir / 'ml_forecasts_2025_2026.csv', index=False)
print(f"   ✓ Saved: ml_forecasts_2025_2026.csv ({len(df_forecasts):,} rows)")

# ============================================================
# EXPORT 6: Summary Statistics by Year
# ============================================================
print("\n6. Creating summary statistics...")
summary_data = []

for year in df_access['TIME_PERIOD'].unique():
    for topic in access_topics:
        subset = df_access[(df_access['TIME_PERIOD'] == year) & (df_access['TOPIC'] == topic)]

        summary_data.append({
            'Year': year,
            'Barrier_Type': topic.replace(' among adults', '').replace('Did not get needed ', 'No ').replace('Did not take ', 'Skipped '),
            'Mean_Rate': subset['ESTIMATE'].mean(),
            'Median_Rate': subset['ESTIMATE'].median(),
            'Max_Rate': subset['ESTIMATE'].max(),
            'Min_Rate': subset['ESTIMATE'].min(),
            'Std_Dev': subset['ESTIMATE'].std(),
            'Num_Subgroups': len(subset)
        })

df_summary = pd.DataFrame(summary_data)
df_summary.to_csv(output_dir / 'yearly_summary_statistics.csv', index=False)
print(f"   ✓ Saved: yearly_summary_statistics.csv ({len(df_summary):,} rows)")

print("\n" + "="*60)
print("✓ All exports completed successfully!")
print(f"✓ Output directory: {output_dir}")
print("="*60)
print("\nNext steps for Tableau Public:")
print("1. Go to https://public.tableau.com/")
print("2. Sign in or create a free account")
print("3. Upload these CSV files as data sources")
print("4. Create dashboards using the exported data")
print("5. Publish your workbook to Tableau Public")
print("6. Copy the shareable URL and update index.html")
print("\nFiles created:")
for file in output_dir.glob('*.csv'):
    size = file.stat().st_size / 1024  # KB
    print(f"  - {file.name} ({size:.1f} KB)")
