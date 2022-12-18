Q1. How do you load a CSV file into a Pandas DataFrame?
-	import pandas as pd
df = pd.read_csv(r'Path where the CSV file is stored\File name.csv')
print(df)

Q2. How do you check the data type of a column in a Pandas DataFrame?
-	result = df.dtypes

Q3. How do you select rows from a Pandas DataFrame based on a condition?
-	df[['PassengerId','Name', 'Sex']]

Q4. How do you rename columns in a Pandas DataFrame?
-	df.rename(columns = {'old_col1':'new_col1', 'old_col2':'new_col2'}, inplace = True
            
Q5. How do you drop columns in a Pandas DataFrame?
-	df.drop('new_col')
            
Q6. How do you find the unique values in a column of a Pandas DataFrame?
-	df['Pclass'].unique()

Q7. How do you find the number of missing values in each column of a Pandas DataFrame?
-	df.isna().sum().sum()
            
Q8. How do you fill missing values in a Pandas DataFrame with a specific value?
-	fillna() Method
            
Q9. How do you concatenate two Pandas DataFrames?
frames = [df1, df2]
  
result = pd.concat(frames)
display(result)

Q10. How do you merge two Pandas DataFrames on a specific column?
-	pandas.merge()
            
Q11. How do you group data in a Pandas DataFrame by a specific column and apply an aggregation function?
-	df.groupby(['Name']).sum()
            
Q12. How do you pivot a Pandas DataFrame?
-	table = pd.pivot_table(data=df,index=['Sex'])
            
Q13. How do you change the data type of a column in a Pandas DataFrame?
-	astype() 
            
Q14. How do you sort a Pandas DataFrame by a specific column?
-	df = df.reindex(sorted(df.columns), axis=1)
            
Q15. How do you create a copy of a Pandas DataFrame?
-	DataFrame.copy(deep=True)
     true - deep copy 
false - shallow copy

Q16. How do you filter rows of a Pandas DataFrame by multiple conditions?
-	Using Loc
            
Q17. How do you calculate the mean of a column in a Pandas DataFrame?
-	df2 = df[["column name","column name"]].mean()
            
Q18. How do you calculate the standard deviation of a column in a Pandas DataFrame?
-	std() function 
            
Q19. How do you calculate the correlation between two columns in a Pandas DataFrame?
-	corr() function
            
Q20. How do you select specific columns in a DataFrame using their labels?
-	loc[] is used with column labels/names 
            
Q21. How do you select specific rows in a DataFrame using their indexes?
-	iloc[] is used with column index/position
            
Q22. How do you sort a DataFrame by a specific column?
-	df2 = df.sort_values(column name)
            
Q23. How do you create a new column in a DataFrame based on the values of another column?
df = pd.DataFrame({
                    'Event':['value', 'value', 'value', 'value'],
                    'Cost':[10000, 5000, 15000, 2000]})
df['Discounted_Price'] = df['Cost'] - (0.1 * df['Cost'])
print(df)
            
Q24. How do you remove duplicates from a DataFrame?
-	drop_duplicates() method
            
Q25. What is the difference between .loc and .iloc in Pandas?

-	The main difference between pandas loc[] vs iloc[] is loc gets DataFrame rows & columns by labels/names and iloc[] gets by integer Index/position. 
-	For loc[], if the label is not present it gives a key error. For iloc[], if the position is not present it gives an index error
