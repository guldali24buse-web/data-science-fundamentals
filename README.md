# Data Science Fundamentals

 End-to-End Salary & Experience Analysis Pipeline
<img width="402" height="282" alt="plot" src="https://github.com/user-attachments/assets/858a6f01-0883-4b1e-a705-dfb3b0bf1921" />

**Project Overview**
This module demonstrates a complete data science workflow, from raw data ingestion to machine learning classification. The primary objective is to analyze the relationship between user tenure and income, and predict account subscription status (Paid/Unpaid) using a multi-dimensional feature space.

** Tech Stack & Libraries**
* **Data Manipulation & Bucketing:** Pandas, NumPy
* **Data Visualization:** Matplotlib
* **Machine Learning:** Scikit-Learn (KNeighborsClassifier, LabelEncoder, model_selection, metrics)

** Methodology & Engineering Steps**
1. **Exploratory Data Analysis (EDA):** 
   * Mapped continuous variables (Salary vs. Years of Experience) to identify underlying correlations. 
   * Visualized the strong positive linear trend using Matplotlib scatter plots.
<img width="402" height="282" alt="plot" src="https://github.com/user-attachments/assets/858a6f01-0883-4b1e-a705-dfb3b0bf1921" />

2. **Feature Engineering (Statistical Bucketing):**
   * Replaced static, hard-coded `if-else` thresholds with data-driven statistical bucketing.
   * Utilized Pandas `qcut` to divide users into three equal-sized categorical quantiles (Junior, Mid, Senior), ensuring balanced segment representation and preventing model bias toward outliers.

3. **Data Preprocessing & Encoding:**
   * Transformed the categorical target variable (Account Status) into machine-readable numerical formats using `LabelEncoder`.
   * Designed a robust feature matrix ($X$) combining both continuous (Salary) and engineered categorical (Tenure Level) features.

4. **Predictive Modeling (K-Nearest Neighbors):**
   * Established a KNN classification model with $k=3$ to predict user status based on the integrated feature space.
   * Executed a standard 80/20 `train_test_split` to validate model performance on unseen data.

** Evaluation & Edge-Case Handling**
* **Zero-Division Management:** Due to the strictly constrained sample size (10 initial records) used for baseline algorithmic architecture, test sets occasionally lack representation for certain classes.
* **Proactive Exception Handling:** Instead of allowing systemic failure, `zero_division=0` parameters were strictly enforced within the `classification_report`. The resulting confusion matrix and F1-scores actively reflect the mathematical boundaries of micro-datasets rather than predictive failure.
