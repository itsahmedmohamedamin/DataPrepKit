# data_summary.py
import pandas as pd

def data_summary(df):
    print("Data Summary:")
    print(df.describe())
    print("\nMost Frequent Values:")
    print(df.mode().iloc[0])
