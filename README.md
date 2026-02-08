# 🏥 DubsTech Datathon 2026 — Healthcare Track

**Team:** Josiah, [Teammate 2], [Teammate 3]

---

## 🗂 Project Structure

```
datathon-2026/
├── notebooks/
│   └── datathon_analysis.ipynb    ← Shared Colab workspace
├── streamlit/
│   ├── app.py                     ← Interactive web dashboard
│   ├── requirements.txt           ← Python dependencies
│   └── data/
│       └── cleaned_data.csv       ← Output from Colab (added during hackathon)
└── README.md                      ← You are here
```

---

## 🚀 Quick Start — Morning Setup (< 30 min)

### Step 1: Google Drive (shared data hub)

1. **One person** creates a Google Drive folder called `datathon-2026` with a `data` subfolder inside
2. Share it with all team members (Editor access)
3. When the dataset drops, upload it to `datathon-2026/data/`

### Step 2: Google Colab (shared analysis workspace)

1. Upload `notebooks/datathon_analysis.ipynb` to Google Drive
2. Open it with Google Colab
3. Share the Colab link with teammates (Editor access — just like Google Docs)
4. **Everyone runs the Setup cell first** to mount Drive and import libraries
5. Update the `DATA_PATH` variable to point to your dataset in Drive

### Step 3: Streamlit (one person sets this up)

While the other two start analyzing in Colab, one person:

1. Install Streamlit locally:
   ```bash
   pip install -r streamlit/requirements.txt
   ```
2. Run the app:
   ```bash
   cd streamlit
   streamlit run app.py
   ```
3. As analysis progresses, pull finished charts from Colab into `app.py`

---

## 🔄 Workflow During the Hackathon

```
    ┌─────────────────┐
    │   Google Drive   │  ← Dataset lives here
    │  /datathon-2026/ │
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │  Google Colab    │  ← All 3 teammates work here
    │  (shared notebook)│     Clean → Explore → Analyze → Model
    └────────┬────────┘
             │ exports cleaned_data.csv
    ┌────────▼────────┐
    │   Streamlit App  │  ← 1 teammate builds the dashboard
    │   (app.py)       │     Pulls in charts & insights from Colab
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │  GitHub + Deploy │  ← Final 2 hours: package & deploy
    └─────────────────┘
```

---

## 📤 Final Packaging (Last 2 Hours)

### Push to GitHub
```bash
git init
git add .
git commit -m "Datathon 2026 submission"
git remote add origin https://github.com/YOUR_USERNAME/datathon-2026.git
git push -u origin main
```

### Deploy Streamlit (free)
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Point it to your repo → `streamlit/app.py`
4. Click Deploy
5. You now have a live URL to share with judges! 🎉

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| Google Colab | Collaborative analysis notebook |
| Google Drive | Shared data storage |
| Streamlit | Interactive web dashboard |
| Plotly | Interactive charts |
| Pandas / NumPy | Data wrangling |
| scikit-learn | ML modeling (optional) |
| GitHub | Version control & submission |

---

## 📊 Extending This Analysis

- **Tableau / Power BI** — Download the cleaned CSV from the Export page
- **Jupyter** — Open the full analysis notebook in Colab
- **Developers** — Fork this repo and extend the pipeline

---

*Built for [DubsTech Datathon 2026](https://datathon-2026.webflow.io/) at the University of Washington*
