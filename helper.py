import pandas as pd
def clean_df(df):
    temp_df=df
    new_df=temp_df.dropna(inplace=True)
    return new_df



