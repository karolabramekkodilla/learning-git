import pandas as pd
import numpy as np

# df = pd.read_csv('myCsvFile.csv')
# df.to_csv('myNewCsvFile.csv', index=False)
df = pd.read_excel('myExcelFile.xlsx', sheet_name='my_data')
print(df)
df.to_excel('myNewExcelFile.xlsx', sheet_name='my_new_data')
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='my_dfs')
df.to_excel(writer, sheet_name='my_dfs', startcol=6, startrow=5, index=False)
writer.close()

writer = pd.ExcelWriter('many_sheets.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='my_df1')
df.to_excel(writer, sheet_name='my_df2')

writer.close()

writer = pd.ExcelWriter('add_chart.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='my_chart')
workbook = writer.book
worksheet = writer.sheets['my_chart']
chart = workbook.add_chart({'type':'line'})

def grab_series(df, sheet_name, colname, startcol=0, startrow=0):

    col_index = df.columns.tolist().index(colname)
    col_letter = chr(ord('@')+(col_index+2+startcol))
    first_row = startrow + 2
    last_row = startrow + 1 + len(df)
    return f"='{sheet_name}'!{col_letter}{first_row}:{col_letter}{last_row}"

chart.add_series({'values':grab_series(df,'my_chart','B')})
chart.set_x_axis({
    'name': 'x^2',
    'name_font': {'size': 14, 'bold': True},
    'num_font':  {'italic': True },
})
chart.set_legend({'none': True})
worksheet.insert_chart('F2', chart)
writer.close()
