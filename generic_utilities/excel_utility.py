import xlrd

path = r'C:\Users\KIIT\PycharmProjects\Selenium_pycharm_kiit\POM_Project1_Demowebshop\files_\demo_testdata.xlsx'


def read_excel():
    workbook = xlrd.open_workbook(path)                     ## book obj
    worksheet = workbook.sheet_by_name("Sheet1")            ## sheet_obj
    rows = worksheet.get_rows()                             ## generator_obj
    header = next(rows)

    d = {}
    for ele in rows:
        d[ele[0].value] =  ele[1].value

    return d














































































