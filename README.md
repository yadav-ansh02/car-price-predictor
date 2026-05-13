# Car Price predictor 

Machine learning project that predicts used car prices through data preprocessing, feature engineering, and model optimization.

## Table of Contents 
- <a href="#overview">Overview</a>
- <a href="#business-problem">Business Problem</a> 
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="project-structure">Project Structure</a> 
- <a href="#data-cleaning--preparation">Data Cleaning Preparation</a>
- <a href="#exploratory-data-analysis-eda">Exploratory Data Analysis(EDA)</a> 
- <a href="#research-question--key-findings">Research Question & Key Findings</a>
- <a href="#how-to-run-this-project">How To Run This Project</a>
- <a href="#final-recommendation">Final Recommendations</a>
- <a href="#author-contact">Author & Contact</a>

--- 
<h2><a class="anchor" id="overview"></a>Overview</h2>  

This project is an end-to-end machine learning application that predicts used car prices based on features such as brand, fuel type, transmission, kilometers driven, and vehicle age.
The system includes data preprocessing, feature engineering, model comparison, and a Streamlit-based web interface for real-time price prediction.  

--- 
<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>  

Developed a machine learning solution to address inaccurate and inconsistent pricing in the used car market by predicting fair vehicle prices from historical data. 

<h2><a class="anchor" id="dataset"></a>Dataset</h2> 

<p>
The dataset used in this project contains information about used cars, including features such as car brand, model, year, fuel type,kilometers driven, and selling price.
</p>

--- 
<h2><a class="anchor" id="tools--tecnologies"></a>Tools & Technologies</h2>

- Python
- Pandas
- NumPy
- Scikit-learn
- Linear Regression
- Streamlit
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code
- Git & GitHub 

--- 
<h2><a class="anchor" id="project-structure"></a>Project Structure</h2> 

---
```text
car-price-predictor-ml/
│
├── data/ 
├── screenshots/
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── notebooks/
```
<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning preparation</h2> 

The dataset was cleaned and preprocessed to improve data quality and model performance. The following steps were performed:

- Converted the `year` column data type from object to integer
- Removed unwanted and inconsistent entries from the `price` column
- Removed commas from price values and converted the column to integer type
- Cleaned the `km_driven` column by removing commas from numerical values
- Converted the `km_driven` column from object type to integer
- Handled inconsistent formatting and prepared the dataset for machine learning models

h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis</h2>   

**Negative or zero values detected:**
- 
- 
- 

**Outliers Identified:** 
- 
- 
- 

**Correlation Analysis:** 
- 
- 
- 
- 

h2><a class="anchor" id="research-questions--key-findings"></a>Research Questions & Key Findings</h2> 
1. **Brands for promotions**: 198 brands with low sales but high profit margins 
2. **Top vendors**: Top 10 vendors = 65.69% of purchases - risk of over-reliance
3. **Bulk Purchasing Impact**: 72% cost savings per unit in large orders 
4. **Inventory turnover**: $2.71M worth of unsold inentory 

--- 
h2><a class="anchor" id="dashboard"></a>Dashboard</h2>  

-Power BI dashboard shows: 
 - Vendor-wise sales and margins
 - Inventory Turnover
 - Bulk Purchase Savings 
 - Performance Heatmaps 

![Vendor Perfomace Dashboard]{images/dashboard.png}

--- 
h2><a class="anchor" id="how-to-run-this-project"></a>How To Run This Project</h2> 
1. Clone the repository:
```bash 
git clone https://github.com/yourusername/vendor-performance-analysis.git
...
2.Load the CSVs and ingest into database:
```bash 
python scripts/ingestion_db.py 
... 
3.Create vender summary table:
```bash 
python scripts/get_vendor_summary.py
```
4. Open and run notebooks:
  - 'notebooks/esploaratory_data analysis.ipynb'
  - 'notebooks/vendor_performance_analysis.ipynb'
5. Open Power BI noteboks: 
  - 'dashboards/vendor_performance_dashboard.pbix'

---
h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>  
- Diversify vendor base to reduce risk
- optimize bulk order straegies 
- Reprice slow-moving , high-margin brands 
- Clear unsold inventory strategically 
- Improve marketing for underperforming vendors 

--- 
h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>  
**Ansh Yadav** 
Email : yadav.ansh.0224@gmail.com 
[LinkedIN](www.linkedin.com/in/ansh-yadav-4a7b04390)



