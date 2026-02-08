# Tableau Public Integration Guide

This guide will help you recreate your visualizations in Tableau Public and integrate them with your GitHub Pages site.

## 📁 Exported Data Files

Your data has been exported to `data/tableau_exports/` as 6 CSV files:

1. **healthcare_access_barriers_full.csv** (1,807 rows)
   - Complete dataset with all access barriers 2019-2024
   - Use for: comprehensive exploratory dashboards

2. **time_series_trends.csv** (1,783 rows)
   - Time series data with non-overlapping demographic groups
   - Use for: COVID impact trends, temporal analysis

3. **disparities_2024_snapshot.csv** (307 rows)
   - Current year data only
   - Use for: "Disparities Snapshot" dashboard

4. **disparity_gaps.csv** (480 rows)
   - Pre-calculated gaps between max/min subgroups per demographic
   - Use for: gap analysis, inequality metrics

5. **ml_forecasts_2025_2026.csv** (30 rows)
   - Predictions from both ML models (2025 & 2026)
   - Use for: "Predictive Modeling" dashboard

6. **yearly_summary_statistics.csv** (24 rows)
   - Summary stats by year and barrier type
   - Use for: overview metrics, KPIs

---

## 🎨 Recommended Tableau Dashboards

### Dashboard 1: Disparities Snapshot (2024)
**Data Source:** `disparities_2024_snapshot.csv`

**Visualizations to create:**
- **Horizontal bar chart**: Subgroups by barrier rate (colored by classification)
- **Heatmap**: Barrier types (columns) × Subgroups (rows)
- **Filters**: Classification, Barrier Type

**Match your Plotly version:** Section 02 - Disparities Snapshot

---

### Dashboard 2: COVID Impact & Recovery
**Data Source:** `time_series_trends.csv` + `disparity_gaps.csv`

**Visualizations to create:**
- **Line chart**: Barrier rates 2019-2024 by subgroup
- **Area chart**: Fill between max/min subgroups (like your gap charts)
- **Reference line**: Mark 2020 COVID zone
- **Calculated field**: Year-over-year % change
- **Filters**: Demographic Group, Barrier Type

**Match your Plotly version:** Section 03 - COVID Impact

---

### Dashboard 3: Predictive Modeling
**Data Source:** `ml_forecasts_2025_2026.csv`

**Visualizations to create:**
- **Grouped bar chart**: 2024 Actual vs. Predicted (2025/2026)
- **Diverging bar chart**: Change values (red = worsening, green = improving)
- **Parameters**: Year selection (2025 or 2026)
- **Filters**: Classification, Model

**Match your Plotly version:** Section 04 - Predictive Modeling

---

## 📝 Step-by-Step: Publishing to Tableau Public

### 1. Create Tableau Public Account
- Go to https://public.tableau.com/
- Click "Sign Up" (it's free!)
- Download and install Tableau Public Desktop

### 2. Upload Your Data
1. Open Tableau Public Desktop
2. Click "Connect to Data"
3. Select "Text file" → navigate to `data/tableau_exports/`
4. Upload all 6 CSV files
5. Create relationships/joins if needed (usually not necessary)

### 3. Create Your Dashboards
Follow the recommendations above for each dashboard. Tips:

**Design consistency:**
- Use your color scheme:
  - Primary accent: `#2a9d8f` (teal)
  - Warning/high: `#e63946` (red)
  - Good/low: `#2ecc71` (green)
- Font: Keep it clean (Arial or similar)
- Dark background: Use `#0a0e17` for background if possible

**Best practices:**
- Add titles and subtitles to each worksheet
- Include tooltips with details
- Add filters for interactivity
- Use calculated fields for custom metrics

### 4. Publish Your Workbook
1. Click "File" → "Save to Tableau Public As..."
2. Give it a name: "Healthcare Access Barriers Dashboard"
3. Add description: "Analysis of healthcare access disparities 2019-2024"
4. Click "Save"
5. Your workbook will upload to Tableau Public

### 5. Get Your Shareable URL
After publishing:
1. Tableau Public will open your workbook in the browser
2. Copy the URL (format: `https://public.tableau.com/app/profile/YOUR_NAME/viz/YOUR_WORKBOOK`)
3. Update `index.html` with this URL

---

## 🔗 Update Your Website

Replace the placeholder URL in `index.html`:

```html
<!-- Find this line (around line 751) -->
<a href="https://public.tableau.com/app/profile/YOUR_PROFILE/viz/YOUR_WORKBOOK" target="_blank">View on Tableau</a>

<!-- Replace with your actual Tableau Public URL -->
<a href="https://public.tableau.com/app/profile/accessible-infinity-tunnel/viz/HealthcareAccessBarriers2026" target="_blank">View on Tableau</a>
```

---

## 💡 Pro Tips

### Recreating Your Plotly Visualizations

**Bubble Plot:**
- Use a scatter plot with Size encoding
- Map circle size to average barrier rate
- Use different colors for each demographic category

**Time Series with COVID Zone:**
- Create a reference band from 2020-2021
- Color it light red with low opacity
- Add annotation: "COVID-19"

**Area Chart (Disparity Gap):**
- Use dual-axis with synchronized axes
- Plot max and min lines
- Use area fill between them

**Heatmap:**
- Use Matrix visualization
- Rows = Subgroups, Columns = Barrier Types
- Color by ESTIMATE value
- Use red-orange gradient

### Interactive Features to Add

1. **Year selector**: Parameter for filtering by year
2. **Demographic drill-down**: Click a demographic category to see subgroups
3. **Barrier type toggle**: Switch between the 4 barrier types
4. **Tooltips**: Show exact values, confidence intervals, and subgroup names
5. **Trend indicators**: ↑ for worsening, ↓ for improving

---

## 📊 Example Dashboard Layouts

### Layout 1: Single View (Recommended)
```
┌─────────────────────────────────────────────┐
│  FILTERS: [Year] [Classification] [Barrier] │
├─────────────────────────────────────────────┤
│                                             │
│          Main Visualization                 │
│          (e.g., Time Series)                │
│                                             │
├─────────────────────────────────────────────┤
│   Secondary Chart   │   Summary Stats       │
│   (e.g., Heatmap)   │   (KPIs)             │
└─────────────────────────────────────────────┘
```

### Layout 2: Multi-Tab Dashboard
- **Tab 1**: Disparities Snapshot
- **Tab 2**: COVID Impact
- **Tab 3**: Predictions
- **Tab 4**: Data Explorer (freestyle)

---

## ✅ Checklist

Before publishing, make sure:

- [ ] All 6 CSV files are uploaded as data sources
- [ ] Dashboards match the style of your Plotly charts
- [ ] Color scheme is consistent (`#2a9d8f`, `#e63946`, etc.)
- [ ] Tooltips show useful information
- [ ] Filters work correctly
- [ ] Titles and captions are added
- [ ] Data sources are cited (CDC NHIS 2019-2024)
- [ ] You've tested on different screen sizes
- [ ] Workbook is published to Tableau Public
- [ ] URL is updated in `index.html`

---

## 🎯 Final Result

When done, users will be able to:
1. View your beautiful GitHub Pages site (Plotly visualizations)
2. Click "View on Tableau" for interactive exploration
3. Download CSV files for their own analysis
4. Access your Colab notebooks for methodology

This gives judges **multiple ways to engage with your work**, showing versatility and thoroughness!

---

## 🆘 Need Help?

**Tableau Resources:**
- [Tableau Public Gallery](https://public.tableau.com/app/discover) - Browse examples
- [Tableau Training Videos](https://public.tableau.com/app/learn/how-to-videos) - Free tutorials
- [Tableau Community](https://community.tableau.com/) - Ask questions

**Quick troubleshooting:**
- **CSV won't upload?** Make sure there are no special characters in column names
- **Chart looks wrong?** Check your measure vs. dimension assignments
- **Colors not matching?** Use custom color palette with hex codes
- **Can't publish?** Ensure you're signed in to Tableau Public account

---

Good luck! 🚀 Your visualizations are going to look amazing in Tableau!
