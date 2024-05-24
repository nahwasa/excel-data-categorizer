import pandas as pd

df = pd.read_excel('C:/ff/input.xlsx')

excel_writer = pd.ExcelWriter("C:/ff/result.xlsx", engine='xlsxwriter')

for lane_number, group in df.groupby('구분'):
    group.to_excel(excel_writer, sheet_name=str(lane_number), index=False)

excel_writer.close()
