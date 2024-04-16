import os # lib to handle files and folders
import glob # lib to list files

import pandas as pd

from typing import List

"""
Function to read all files from a folder (data/input)
and return a dataframe list

args: input_path (str): path to input folder

return: list of dataframes
"""

path = "data/input/"
def extract_from_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path,  "*.xlsx"))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list

if __name__ == "__main__":
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)
