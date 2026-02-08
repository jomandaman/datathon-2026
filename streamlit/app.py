import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="Healthcare Datathon 2026",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# SIDEBAR NAVIGATION
# ============================================
st.sidebar.image("https://cdn.prod.website-files.com/695f0a813d30515fd86c17a9/69601d7ecc8b441509b8a014_Final%20Wordmark.png", width=200)
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Overview", "🔍 Exploration", "📊 Analysis", "🤖 Model", "📤 Export & Extend"]
)

# ============================================
# LOAD DATA
# ============================================
@st.cache_data
def load_data():
    """
    Load the cleaned dataset.
    Update this path once your cleaned data is ready.
    """
    try:
        df = pd.read_csv("data/cleaned_data.csv")
        return df
    except FileNotFoundError:
        return None

df = load_data()


# ============================================
# PAGE: OVERVIEW
# ============================================
if page == "🏠 Overview":
    st.title("🏥 Healthcare Data Analysis")
    st.markdown("### DubsTech Datathon 2026 — Team [Name]")
    
    st.markdown("---")
    
    st.markdown("""
    ## The Problem
    
    *Replace this with the actual problem statement from the hackathon prompt.*
    
    We analyzed [describe dataset] to uncover insights about [topic]. 
    Our approach involved data cleaning, exploratory analysis, and [modeling/statistical testing].
    """)
    
    # Key metrics row
    if df is not None:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Records", f"{len(df):,}")
        with col2:
            st.metric("Features", f"{len(df.columns)}")
        with col3:
            st.metric("Placeholder", "—")  # Replace with a real metric
        with col4:
            st.metric("Placeholder", "—")  # Replace with a real metric
    else:
        st.warning("⚠️ No data loaded yet. Place your `cleaned_data.csv` in the `data/` folder.")
    
    st.markdown("---")
    st.markdown("""
    ## Our Approach
    
    1. **Data Cleaning** — Handled missing values, standardized formats, removed duplicates
    2. **Exploratory Analysis** — Identified distributions, correlations, and trends  
    3. **Deep Dive** — [Describe your specific analysis or model]
    4. **Insights** — Key findings that could inform healthcare decisions
    """)


# ============================================
# PAGE: EXPLORATION
# ============================================
elif page == "🔍 Exploration":
    st.title("🔍 Data Exploration")
    
    if df is not None:
        st.markdown("### Dataset Preview")
        st.dataframe(df.head(50), use_container_width=True)
        
        st.markdown("---")
        st.markdown("### Column Explorer")
        
        # Let user pick a column to visualize
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        categorical_cols = df.select_dtypes(include='object').columns.tolist()
        
        col1, col2 = st.columns(2)
        
        with col1:
            if numeric_cols:
                selected_num = st.selectbox("Select a numeric column", numeric_cols)
                fig = px.histogram(df, x=selected_num, title=f"Distribution of {selected_num}")
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if categorical_cols:
                selected_cat = st.selectbox("Select a categorical column", categorical_cols)
                value_counts = df[selected_cat].value_counts().head(15)
                fig = px.bar(x=value_counts.index, y=value_counts.values,
                           title=f"Top values in {selected_cat}",
                           labels={"x": selected_cat, "y": "Count"})
                st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### Correlation Heatmap")
        if len(numeric_cols) > 1:
            corr = df[numeric_cols].corr()
            fig = px.imshow(corr, text_auto=".2f", title="Feature Correlations",
                          color_continuous_scale="RdBu_r", zmin=-1, zmax=1)
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ No data loaded yet.")


# ============================================
# PAGE: ANALYSIS
# ============================================
elif page == "📊 Analysis":
    st.title("📊 Deep Dive Analysis")
    
    st.markdown("""
    *This is where you put your team's specific analysis and visualizations.*
    
    Pull in the charts you marked with ✅ in the Colab notebook.
    """)
    
    if df is not None:
        # PLACEHOLDER: Replace these with your actual analysis charts
        
        st.markdown("### Finding 1: [Title]")
        st.markdown("*Explain the insight here...*")
        # fig = px.scatter(df, x='col1', y='col2', color='col3', title='Your Chart')
        # st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        st.markdown("### Finding 2: [Title]")
        st.markdown("*Explain the insight here...*")
        
        st.markdown("---")
        
        st.markdown("### Finding 3: [Title]")
        st.markdown("*Explain the insight here...*")
    else:
        st.warning("⚠️ No data loaded yet.")


# ============================================
# PAGE: MODEL (optional)
# ============================================
elif page == "🤖 Model":
    st.title("🤖 Predictive Model")
    
    st.markdown("""
    *If your team builds an ML model, showcase it here.*
    
    You can show:
    - Model performance metrics
    - Feature importance
    - Interactive predictions
    """)
    
    # PLACEHOLDER: Example interactive prediction
    st.markdown("### Try a Prediction")
    st.info("🚧 Model not yet trained. This section will be populated once the model is ready.")
    
    # Example of what this could look like:
    # with st.form("prediction_form"):
    #     age = st.slider("Age", 18, 100, 45)
    #     feature2 = st.selectbox("Feature 2", ["Option A", "Option B"])
    #     submitted = st.form_submit_button("Predict")
    #     if submitted:
    #         st.success(f"Predicted outcome: ...")


# ============================================
# PAGE: EXPORT & EXTEND
# ============================================
elif page == "📤 Export & Extend":
    st.title("📤 Export & Extend This Analysis")
    
    st.markdown("""
    Our analysis pipeline is designed to be **extensible**. 
    Download the cleaned data, explore the full notebook, or fork the code to build on our work.
    """)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📊 Tableau / Power BI")
        st.markdown("""
        Export our cleaned, analysis-ready dataset 
        to visualize in Tableau, Power BI, or Excel.
        """)
        if df is not None:
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Download CSV",
                data=csv_data,
                file_name="healthcare_cleaned_data.csv",
                mime="text/csv"
            )
        else:
            st.info("Data not yet available.")
    
    with col2:
        st.markdown("### 📓 Jupyter / Colab")
        st.markdown("""
        View our full analysis notebook with 
        all code, methodology, and commentary.
        """)
        # UPDATE THIS LINK with your actual Colab notebook link
        st.link_button(
            "🔗 Open in Google Colab",
            "https://colab.research.google.com/drive/YOUR_NOTEBOOK_ID_HERE"
        )
    
    with col3:
        st.markdown("### 🐙 GitHub")
        st.markdown("""
        Clone the repo to extend our pipeline,
        add new models, or integrate new data.
        """)
        # UPDATE THIS LINK with your actual GitHub repo
        st.link_button(
            "🔗 View on GitHub",
            "https://github.com/YOUR_USERNAME/datathon-2026"
        )
    
    st.markdown("---")
    
    # Bonus: Show data schema for anyone extending
    st.markdown("### 📋 Data Schema")
    st.markdown("For anyone looking to extend this analysis, here's what the cleaned dataset contains:")
    
    if df is not None:
        schema_df = pd.DataFrame({
            "Column": df.columns,
            "Type": df.dtypes.astype(str).values,
            "Non-Null Count": df.notnull().sum().values,
            "Sample Value": [str(df[col].dropna().iloc[0]) if not df[col].dropna().empty else "N/A" for col in df.columns]
        })
        st.dataframe(schema_df, use_container_width=True)
    else:
        st.info("Schema will appear once data is loaded.")


# ============================================
# FOOTER
# ============================================
st.sidebar.markdown("---")
st.sidebar.markdown("""
**Built for DubsTech Datathon 2026**  
Team: [Name]  
Feb 7-8, 2026
""")
