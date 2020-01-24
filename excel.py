from openpyxl import load_workbook
from openpyxl import Workbook

twb=Workbook()
#twb=load_workbook('t.xlsx')

tws=twb.active
tws.title='tws'
tws['A1']=42
tws['E5']=42
tws.append([1,2,3,4])

tws1=twb.create_sheet('newSheet1')
tws2=twb.create_sheet('newSheet2')
tws3=twb.create_sheet('newSheet3')
tws4=twb.create_sheet('newSheet4')

tws5=twb['newSheet1']

'''for row in tws.iter_cols(1,4,2,3):
    for cell in row:
        print(cell)'''

print(tuple(tws.rows))
twb.save('t.xlsx')
