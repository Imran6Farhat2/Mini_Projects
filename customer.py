#Q1:- read the csv file and display the data frame 
import pandas as pd

#read the csv file
df = pd.read_csv("customers.csv")
print(df)

#Q2:-Display the first 5 rows 
import pandas as pd
df = pd.read_csv("customers.csv")
print(df.head())


#Q3:- Display the last 5 rows 
import pandas as pd
df = pd.read_csv("customers.csv")
print(df.tail())

#Q4:- Display the last two rows
import pandas as pd 
df = pd.read_csv("customers.csv")
print(df.tail(2))

#Q5:- Display the information about dat frame
import pandas as pd
df = pd.read_csv("customers.csv")
print(df.info())


#Q7 :- Display the statistical information about the data frame
import pandas as pd
df = pd.read_csv("customers.csv")
print(df.describe())