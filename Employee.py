import pandas as pd
#Read the csv file
emp = pd.read_csv("employees.csv")
print(emp)

att = pd.read_csv("employee_Attendance.csv")
print(att)

#Q1:- Display only employees working in the HR department
import pandas as pd
print("\n1. Employees working in HR department")
print(emp[emp["Department"]=="HR"])

#Q2:- Display the salary whose salary is greater than 50000
import pandas as pd
print("\n2 Employees whose salary is greater than 50000")
print(emp[emp["Salary"]>50000])


#Q3:- Display employees who belongs to delhi

import pandas as pd
print("\n3.employees who belongs to delhi")
print(emp[emp["City"]=="Delhi"])

#Q4 DIsplay the employees who belongs to mohali and have experience greater than 2 year
print("\n4. Employees who belongs to mohali and have experience > 2")
print(emp[(emp["City"]=="Mohali") & (emp["Experience"]>2)])

#Q5:- Sort the emp according to salary in descending order

import pandas as pd 
print("\n5. Employee salary in descending order")
print(emp.sort_values(by="Salary",ascending=False))

# 6. Sort the employees according to Experience in ascending order.
import pandas as pd 
print("\n6. Experience in Ascending Order")
print(emp.sort_values(by="Experience", ascending=True))

# 7. Find the average salary of each department.
import pandas as pd 
print("\n7. Average Salary of Each Department")
print(emp.groupby("Department")["Salary"].mean())

# 8. Find the maximum salary in each department.
import pandas as pd 
print("\n8. Maximum Salary of Each Department")
print(emp.groupby("Department")["Salary"].max())

# 9. Find the minimum salary in each department.
import pandas as pd 
print("\n9. Minimum Salary of Each Department")
print(emp.groupby("Department")["Salary"].min())

# 10. Find the total salary of employees department-wise.
import pandas as pd 
print("\n10. Total Salary Department-wise")
print(emp.groupby("Department")["Salary"].sum())

# 11. Count the number of employees in each city.
import pandas as pd
print("\n11. Number of Employees in Each City")
print(emp["City"].value_counts())

# 12. Display the number of missing values in each column.
import pandas as pd
print("\n12. Missing Values in Each Column")
print(emp.isnull().sum())

# 13. Replace the missing salary with 0.

emp["Salary"] = emp["Salary"].fillna(0)
print("\n13. Salary after replacing missing values with 0")
print(emp)

#Q14:- Merge the employees.csv and attendance.csv file
merged = pd.merge(emp,att,on= "Emp_id")
print("\n14. Merged Data")
print(merged)

#Q15:- display only those employees whose attendance is present
print("\n15.Present Employees")
print(merged[merged["Attendance"]=="Present"])
