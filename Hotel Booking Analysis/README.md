# Hotel booking analysis

Dataset taken from this tutorial - https://www.youtube.com/watch?v=obJZ1rB7TKc&t=1440s&ab_channel=TechClasses

## Steps followed in brief - 

1. Importing Libraries and Loading the dataset
2. Checking for right datatypes and formats in columns
3. EDA and data cleaning (removing unnecessary columns)
4. Data visualizations using Seaborn library

## What I learnt new - 

1. Code for finding all the unique values in CATEGORICAL columns -
   
        for col in df.describe(include = 'object').columns:
          print(col)
          print(df[col].unique())
          print('-'*50)

2. Finding % contribution of each unique value in a column using `value_counts()`

        (df['is_canceled'].value_counts(normalize=True))*100
