#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
      csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
      employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
      employee_list = []
      for data in employee_file:
          employee_list.append(data)
      return employee_list

employee_list = read_employees('/home/student-04-8b2d0ed74e60/data/employees.csv')
print(employee_list)
