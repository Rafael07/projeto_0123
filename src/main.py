from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_dataframe

if __name__ == '__main__':

    dataframe_list = extract_from_excel('data/input/')
    print(type(dataframe_list))
    data_frame = concat_dataframe(dataframe_list)
    print(type(data_frame))
    load_excel(data_frame, 'data/output/', 'output')
