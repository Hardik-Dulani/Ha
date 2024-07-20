import streamlit as st
import pickle
import helper
# Full forms and descriptions of each point
descriptions = {
    'Name': "Full name of the patient",
    'Sex': "Sex of the patient",
    'Typical Chest Pain': "Typical chest pain associated with heart conditions (0: No, 1: Yes)",
    'Atypical': "Atypical chest pain that is not typical for heart conditions (0: No, 1: Yes)",
    'EF-TTE': "Ejection Fraction from Transthoracic Echocardiogram (% range: 0-100)",
    'Age': "Age of the patient (years)",
    'Region RWMA': "Regional Wall Motion Abnormality (0: No, 1: Yes)",
    'HTN': "Hypertension (0: No, 1: Yes)",
    'BP': "Blood Pressure (mm Hg range: 80-200)",
    'ESR': "Erythrocyte Sedimentation Rate (mm/hr range: 0-100)",
    'FBS': "Fasting Blood Sugar (mg/dL range: 70-130)",
    'Nonanginal': "Non-anginal chest pain (0: No, 1: Yes)",
    'DM': "Diabetes Mellitus (0: No, 1: Yes)",
    'Tinversion': "T wave inversion in ECG (0: No, 1: Yes)",
    'K': "Potassium level in blood (mEq/L range: 3.5-5.5)",
    'TG': "Triglycerides (mg/dL range: 0-150)",
    'Na': "Sodium level in blood (mEq/L range: 135-145)",
    'Length': "Height of the patient (cm range: 50-250)",
    'Weight': "Weight of the patient (kg range: 10-200)",
    'Lymph': "Lymphocyte count (cells/uL range: 1000-4000)",
    'PLT': "Platelet count (cells/uL range: 150,000-450,000)",
    'Dyspnea': "Shortness of breath (0: No, 1: Yes)",
    'BMI': "Body Mass Index (kg/m² range: 10-50)"
}

# Function to calculate BMI


# Setting the title
st.markdown("<h1 style='font-size: 36px;'>Medical Information </h1>", unsafe_allow_html=True)
st.write("We're collecting basic information needed for our model to work. If you have this information, please provide it. If not, simply press 'Don't Know' and we will use the most probable input based on our training data to give predictions.")

# Creating the form
my_data = {}

with st.form(key='medical_info_form'):
    name = st.text_input("**Name:**", help=descriptions['Name'])
    my_data['Sex']=st.selectbox("**Sex:**", ["Male","Female","Other"], help=descriptions['Sex'])
    my_data['Age'] = st.number_input("**Age (years):**", min_value=0, max_value=120, help=descriptions['Age'])
    my_data['Weight'] = st.number_input("**Weight (kg):**", min_value=10.0, max_value=200.0, help=descriptions['Weight'])
    my_data['Length'] = st.number_input("**Height (Length) (cm):**", min_value=50.0, max_value=250.0, help=descriptions['Length'])
    my_data['Typical_chest_pain'] = st.selectbox("**Typical Chest Pain:**", ["No", "Yes"], help=descriptions['Typical Chest Pain'])
    my_data['Atypical'] = st.selectbox("**Atypical Chest Pain:**", ["No", "Yes"], help=descriptions['Atypical'])
    my_data['Region_rwma'] = st.selectbox("**Region RWMA:**", ["No", "Yes"], help=descriptions['Region RWMA'])
    my_data['HTN'] = st.selectbox("**Hypertension (HTN):**", ["No", "Yes"], help=descriptions['HTN'])
    my_data['Nonanginal'] = st.selectbox("**Nonanginal Chest Pain:**", ["No", "Yes"], help=descriptions['Nonanginal'])
    my_data['DM'] = st.selectbox("**Diabetes Mellitus (DM):**", ["No", "Yes"], help=descriptions['DM'])
    my_data['Tinversion'] = st.selectbox("**T wave Inversion (Tinversion):**", ["No", "Yes"], help=descriptions['Tinversion'])
    my_data['Dyspnea'] = st.selectbox("**Dyspnea (Shortness of Breath):**", ["No", "Yes"], help=descriptions['Dyspnea'])
    my_data['EF-TTE'] = st.slider("**EF-TTE (%):**", min_value=0, max_value=100, help=descriptions['EF-TTE'])
    my_data['BP'] = st.number_input("**Blood Pressure (BP) (mm Hg):**", min_value=80, max_value=200, help=descriptions['BP'])
    my_data['ESR'] = st.slider("**Erythrocyte Sedimentation Rate (ESR) (mm/hr):**", min_value=0, max_value=100, help=descriptions['ESR'])
    my_data['FBS'] = st.slider("**Fasting Blood Sugar (FBS) (mg/dL):**", min_value=70, max_value=130, help=descriptions['FBS'])
    my_data['K'] = st.slider("**Potassium Level (K) (mEq/L):**", min_value=3.5, max_value=5.5, step=0.1, help=descriptions['K'])
    my_data['TG'] = st.slider("**Triglycerides (TG) (mg/dL):**", min_value=0, max_value=150, help=descriptions['TG'])
    my_data['Na'] = st.slider("**Sodium Level (Na) (mEq/L):**", min_value=135.0, max_value=145.0, step=0.1, help=descriptions['Na'])
    my_data['Lymph'] = st.slider("**Lymphocyte Count (cells/uL):**", min_value=1000.0, max_value=4000.0, help=descriptions['Lymph'])
    my_data['PLT'] = st.slider("**Platelet Count (PLT) (cells/uL):**", min_value=150000.0, max_value=450000.0, help=descriptions['PLT'])
    
    # Automatically calculate BMI
    my_data['BMI'] = helper.calculate_bmi(my_data['Weight'], my_data['Length'])
    # st.write(f"**Body Mass Index (BMI):** {bmi_value:.2f} kg/m²")

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Handling form submission
if submit_button:
    file_path = 'defaults.pkl'

# Load the pickle file
    with open(file_path, 'rb') as file:
        defaults = pickle.load(file)
    for i,j in defaults.items():
        if i not in my_data:
            my_data[i] = j
    st.dataframe(my_data)
