# Telecom Customer Churn Analysis Dashboard

## Live App
https://churnanalysiss.streamlit.app/

An interactive **Streamlit dashboard** to analyze customer churn in a telecom company.  
Users can explore patterns, filter data, and gain insights into why customers leave.

---

## Dataset
- **Source:** Telco Customer Churn Dataset (Kaggle)
- **Size:** 7,043 rows × 21 columns

---

## Tech Stack
- **Python**
- **Streamlit** — interactive dashboard
- **Pandas** — data manipulation
- **NumPy** — numerical operations
- **Matplotlib** — basic plotting
- **Seaborn** — advanced visualizations

---

## Features
- Interactive filters (Gender, Contract Type, Internet Service)
- Real-time KPI updates (Total Customers, Churn Rate, etc.)
- Clean and responsive dashboard UI
- Data cleaning and preprocessing handled inside app

---

## Visualizations
1. Churn Distribution (Pie Chart)
2. Churn by Contract Type
3. Tenure Distribution by Churn
4. Churn by Gender
5. Churn by Senior Citizen Status
6. Churn by Internet Service
7. Monthly Charges vs Churn (Box Plot)
8. Churn by Payment Method
9. Monthly Charges vs Total Charges (Scatter Plot)
10. Churn by Support Services (Tech Support, Online Security)

---

## Key Insights
- **26% customers churned**
-  Higher monthly charges → higher churn probability
-  Month-to-month contracts have the highest churn
-  Lack of tech support & online security increases churn risk
-  New customers (low tenure) are more likely to churn

---

##  Data Cleaning
- Converted `TotalCharges` to numeric (handled missing values)
- Transformed `SeniorCitizen` (0/1 → Yes/No)
- Removed duplicate records
- Checked and handled null values

---

## Run Locally

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
streamlit run app.py
