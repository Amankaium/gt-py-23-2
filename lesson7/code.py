from openpyxl import Workbook

# save
class MyExcel(Workbook):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)
        self.use_first_page()
        self.save(name)

    def use_first_page(self):
        self.first_page = self[self.sheetnames[0]]

    def write_in_cell(self, cell, value):
        self.first_page[cell] = value
        self.save(self.name)

# input
name = input()

# save
my_excel_2 = MyExcel("names.xlsx")
my_excel_2.write_in_cell("A2", name)

# excel_book = Workbook()
# page = excel_book.active
# page["A1"] = name
# excel_book.save()
