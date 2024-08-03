from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_validate
import numpy as np
import pandas as pd
import pickle

imp_nums = ['Age',
 'Length',
 'BP',
 'FBS',
 'TG',
 'ESR',
 'K',
 'Na',
 'Lymph',
 'PLT',
 'EF-TTE']

imp_cats = ['DM',
 'HTN',
 'Typical Chest Pain',
 'Dyspnea',
 'Atypical',
 'Nonanginal',
 'Tinversion']


imp_ords = ['Region RWMA']

def preprocess(data):
    preprocessor = ColumnTransformer(transformers = [('OHE', OneHotEncoder(handle_unknown='ignore', sparse_output=False, drop='first', dtype=np.int64), imp_cats),
                                                 ('Scaler', StandardScaler(), imp_nums)],
                                 remainder = 'passthrough',
                                 verbose_feature_names_out = False).set_output(transform = 'pandas')
    return preprocessor.fit_transform(data)



# BMI Calculator
def calculate_bmi(weight, height):
    if height > 0:
        return weight / ((height / 100) ** 2)
    else:
        return 0
    


num_cols = ['Age','Weight', 'Length','BMI', 'BP', 'PR', 'FBS', 'CR', 'TG', 'LDL', 'HDL', 'BUN', 'ESR', 'HB', 'K', 'Na', 'WBC', 'Lymph', 'Neut', 'PLT', 'EF-TTE']

cat_cols = ['Sex', 'DM', 'HTN', 'Current Smoker', 'EX-Smoker', 'FH', 'Obesity', 'CRF', 'CVA', 'Airway disease', 'Thyroid Disease', 'CHF', 'DLP', 'Edema', 'Weak Peripheral Pulse', 'Lung rales', 'Systolic Murmur', 'Diastolic Murmur', 'Typical Chest Pain', 'Dyspnea', 'Atypical', 'Nonanginal', 'Exertional CP', 'LowTH Ang', 'Q Wave', 'St Elevation', 'St Depression', 'Tinversion', 'LVH', 'Poor R Progression']

ord_cols = ['Function Class', "Region RWMA", "VHD"]





# PREDICTION
def predict(data):
    file_path = 'cb_model.pkl'
    # Numerical variables:
    
    with open(file_path, 'rb') as file:
            model = pickle.load(file)
            pred = model.predict(data)
            return pred


# PREPROCESS

def preprocess(data):
    preprocessor = ColumnTransformer(transformers = [('OHE', OneHotEncoder(handle_unknown='ignore', sparse_output=False, drop='first', dtype=np.int64), cat_cols),
                                                 ('Scaler', StandardScaler(), num_cols)],
                                 remainder = 'passthrough',
                                 verbose_feature_names_out = False).set_output(transform = 'pandas')

    X_prep = preprocessor.fit_transform(data)
    return X_prep