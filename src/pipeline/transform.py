from typing import List

import pandas as pd

"""
function to transform a dataframe list into a single dataframe
"""


def concat_dataframe(dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dataframe_list, ignore_index= True)
