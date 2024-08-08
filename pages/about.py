import streamlit as st

# Title of your Streamlit app
st.title("Coronary Artery Disease Prediction Project")

# Introduction section
st.header("Introduction")
st.write("""
Our goal was to develop a model for predicting coronary artery disease (CAD) and to compare the performance of various machine learning algorithms. Additionally, we aimed to analyze the explainability of the chosen machine learning algorithm.
""")

# Dataset Description section
st.header("Dataset Description")
st.subheader("Z-Alizadeh Sani Dataset")
st.markdown("""
The **Z-Alizadeh Sani dataset** is available on the [UCI Machine Learning repository](https://doi.org/10.24432/C5Q31T). It comprises 303 medical records from patients who visited Shaheed Rajaei hospital in Iran due to chest pain. Each record contains 55 features, categorized into:

1. **Demographic Features**
2. **Symptoms and Physical Examination**
3. **ECG (Electrocardiogram)**
4. **Echocardiography Features**

### Class Distribution
- **CAD Class**: 216 instances (71.29%)
- **Normal Class**: 87 instances (28.71%)

A sample is classified as CAD if the stenosis of coronary arteries lumen reaches or exceeds 50%; otherwise, it is classified as normal. Both ECG and echocardiography features are obtained by professional doctors.
""")

# Exploratory Data Analysis section
st.header("Exploratory Data Analysis")
st.write("""
In this part, we analyzed the data distribution and examined the basic statistical properties of the data. This included understanding the types of variables, checking for missing values, and visualizing the distribution of various features and the target variable. This step helped us identify trends, anomalies, patterns, and relationships within the data.
""")

# Predictive Analysis section
st.header("Predictive Analysis")
st.write("""
We processed the data by splitting it into training and test sets, and oversampled the data using SMOTENC. We then developed predictive models with hyperparameter tuning using Optuna.

We built nine models including: CatBoost, XGBoost, LightGBM, and three ensemble models.  We compared these models using various metrics and selected CatBoost for further explainability analysis.

CatBoost, Ensemble3, XGBoost, and LightGBM achieved 100% recall, meaning all CAD patients were correctly identified as CAD class by these models. Since predicting CAD class as normal class is dangerous, reducing false negatives is crucial. CatBoost and Ensemble3 stood out with 91.8% accuracy and a 0.945 F1 score and thus we selected **CatBoost** for further explainability analysis and deployment.
""")

# Explainable AI using SHAP section
st.header("Explainable AI Using SHAP")
st.write("""
We interpreted the CatBoost model using SHAP values. By plotting Feature Importance, Summary, and Dependence plots, we gained insights into the global interpretability of the model.

For local interpretability, we analyzed specific cases, such as Patient No. 77 and Patient No. 7 from the training dataset. Using SHAP Waterfall and Force plots, along with current clinical guidelines, we made recommendations for coronary angiography.

Explainable AI (XAI) methods like SHAP, LIME, ELI5, CAM, and Grad-CAM help reduce human errors in the medical field. Our model, CatBoost with SHAP, aligns well with current decision-making processes and can significantly aid in making accurate and efficient decisions. This method is applicable to other medical datasets and can be utilized across various areas of the medical field.
""")

# Footer or additional information
st.markdown("---")
st.write("For more information, visit the [UCI Machine Learning repository](https://doi.org/10.24432/C5Q31T) to explore the Z-Alizadeh Sani dataset in detail.")
st.write("We have documented our findings and methodology in a research paper, which can be accessed [here](https://doi.org/10.1007/978-3-031-65392-6_24)")
