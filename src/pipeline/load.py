import pandas as pd
import os 

"""
receive a dataframe and save it in a csv file

args: 
    dataframe (pd.DataFrame): dataframe to be saved
    output_path (str): path to output folder
    file_name (str): name of the file

return: "File saved with success"
"""
def load_excel(dataframe: pd.DataFrame, output_path: str, file_name: str) -> str:

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    dataframe.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "File saved with success"