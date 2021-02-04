import pandas as pd
import streamlit as st


def retrieve_train_element(df:pd.DataFrame, target_name:str, ignore_columns:None): 
    """retrieve the training element for online prediction
       extract the value type for each column
    Args:
        df (pd.DataFrame): the original X training dataset 
        target_name (str): the name of the target column
        ignore_columns (list) : the ignore columns from preprocessing
    """
    # if ignore columns, remove them
    
    input_dict = {}
    
    if ignore_columns:
        df = df.drop(ignore_columns, axis=1)
    # drop the label column
    df_X = df.drop(target_name,axis=1)
    for label, content in df_X.items():
        # numeric columns
        if content.dtype == "int64" or content.dtype == "float64":
            input = st.number_input(label, value=content.iloc[0])
        # categorical columns (object, bool)
        else:
            input = st.selectbox(label, options=list(set(content.values)))

        input_dict[label] = input
        
    return pd.DataFrame([input_dict])
