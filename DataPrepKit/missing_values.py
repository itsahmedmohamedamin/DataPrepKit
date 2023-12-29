# missing_values.py
import pandas as pd
from sklearn.impute import SimpleImputer

def remove_missing_values(df):
    return df.dropna()

def impute_missing_values(df, strategy='mean'):
    imputer = SimpleImputer(strategy=strategy)
    return pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
