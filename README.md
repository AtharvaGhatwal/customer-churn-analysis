# Customer Churn Analysis (End-to-End ML + Power BI)
![GitHub stars](https://img.shields.io/github/stars/AtharvaGhatwal/customer-churn-analysis)
![GitHub issues](https://img.shields.io/github/issues/AtharvaGhatwal/customer-churn-analysis)

## 📌 Project Overview
This project analyzes customer churn using machine learning and visual analytics.
The goal is to identify **key drivers of churn** and present insights through an
**executive friendly Power BI dashboard**.

---

## 📊 Dashboard Preview
![Dashboard](images/dashboard_preview.png)

---

## 🧠 Business Questions Answered
- Which age groups churn the most?
- How does customer tenure affect churn?
- Does owning more products increase churn risk?
- Which countries have higher churn rates?
- How do financial indicators differ between churned vs retained customers?

---

## 🛠 Tech Stack
- **Python** (Pandas, Scikit-learn)
- **Machine Learning**: Logistic Regression, Random Forest
- **Visualization**: Power BI
- **Data**: Bank customer churn dataset

---

## 🔍 Key Insights
- Customers aged **50+** show the highest churn rate
- Churn decreases as **tenure increases**
- Customers with **3–4 products** churn significantly more
- **Germany** has the highest churn rate
- Churned customers have **higher average balances but shorter tenure**

---

## 📈 Results at a Glance
- Overall churn rate: **20.35%**
- Total customers analyzed: **2000**
- Churned customers: **407**
- Best performing model: **Random Forest**

---

## ⚙️ Workflow
1. Data cleaning & encoding (Python)
2. Model training & evaluation
3. Feature importance analysis
4. Export predictions for Power BI
5. Interactive dashboard creation

---

## 📁 Project Structure

```
churn-analysis/
├── data/
├── notebooks/
├── powerbi/
├── images/
├── README.md
└── requirements.txt
```

---

## ▶ How to Run

1. Clone repo
```
git clone https://github.com/AtharvaGhatwal/customer-churn-analysis.git
```
2. Install deps  
```
pip install -r requirements.txt
```
3. Run export script  
```
python data/data_check.py
```
4. Open dashboard  
```
Open the file in `powerbi/churn_dashboard.pbit` with Power BI Desktop
```

