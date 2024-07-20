from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_validate
import numpy as np
import pandas as pd

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