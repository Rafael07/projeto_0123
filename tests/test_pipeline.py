import pandas as pd

from src.pipeline.transform import concat_dataframe

df_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df_2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})


def test_concat_dataframe_list():
    """
    use arrange, act and assert to test the function concat_dataframe
    """
    # arrange
    dataframe_list = [df_1, df_2]
    dataframe_list2 = pd.concat(dataframe_list, ignore_index=True)

    # act
    result = concat_dataframe(dataframe_list)

    # assert
    assert result.shape == (4, 2)
    assert dataframe_list2.equals(result)
    assert result.shape != (5, 2)
