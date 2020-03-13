import xlrd

# 设置好输入和输出文件
path = '/Users/alpha/Desktop/business/keywords/20200310.xlsx'
f = xlrd.open_workbook(path)

# 获取Excel中的sheet名字，这里我们只获取第一个sheet
name = f.sheet_names()[0]

# 选择指定sheet进行操作
sheet = f.sheet_by_name(name)


for i in range(20000, 200000):
    v = sheet.cell(i, 0).value
    # print(v)
    if '窗帘' in v or '防蚊' in v:
        print(v)

print('Output successfully.')
