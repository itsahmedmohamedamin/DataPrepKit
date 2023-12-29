# categorical_encoding.py
import pandas as pd

def encode_categorical(df):
    return pd.get_dummies(df)
