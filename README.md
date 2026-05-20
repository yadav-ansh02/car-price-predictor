# Car Price Predictor 

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
 
 The project includes:
 - Data Cleaning & Preprocessing
 - Exploratory Data Analysis (EDA)
 - Model Training & Evaluation
 - Streamlit Web Application for real-time predictions

--- 
<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>  

 This project aims to solve that problem by building a machine learning model that predicts fair market prices for used cars using historical vehicle data

 The solution can help:
 - Buyers estimate fair car prices
 - Sellers price vehicles competitively 
 - Dealerships automate valuation processes

--- 
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
├── .gitignore
└── notebooks/

```

--- 
<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning preparation</h2> 

The dataset was cleaned and preprocessed to improve data quality and model performance. The following steps were performed:

- Converted the `year` column data type from object to integer
- Removed unwanted and inconsistent entries from the `price` column
- Removed commas from price values and converted the column to integer type
- Cleaned the `km_driven` column by removing commas from numerical values
- Converted the `km_driven` column from object type to integer
- Handled inconsistent formatting and prepared the dataset for machine learning models

--- 

<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis</h2>   

**Outliers Identified:** 
- Extremely high-priced luxury vehicles 
- Invalid year entries 
- Cars with unusually high kilometers driven

**Correlation Analysis:** 
- Selling price negatively correlates with car age
- Brand reputation strongly influences pricing


--- 
 
<h2><a class="anchor" id="model-performance"></a>Model Performance</h2>
Evaluation Metrics Used:
 - R² Score 
 - Mean Absolute Error (MAE) 
 - Mean Squared Error (MSE) 

**Best Performing Model:**
Random Forest Regressor achieved the highest prediction accuracy compared to other models.

--- 
<h2><a class="anchor" id="how-to-run-this-project"></a>How To Run This Project</h2> 

1. Clone the repository:
```bash 
git clone https://github.com/yadav-ansh02/car-price-predictor.git
```


2.Navigate to the project directory:
```bash 
  cd car-price-predictor
```


3.install dependencies:
```bash 
pip install -r requirements.txt
```

4.Run the Streamlit application
```bash 
streamlit run app.py
```

---
<h2><a class="anchor" id="future-improvements"></a>Future Improvements</h2>
- Deploy the application on Streamlit Cloud or Render
- Improve UI/UX of the web application

--- 
<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>  
**Ansh Yadav**    

Email : yadav.ansh.0224@gmail.com 
[LinkedIn](https://www.linkedin.com/in/ansh-yadav-4a7b04390)



