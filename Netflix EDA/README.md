## Performed Exploratory Data analysis on Netflix dataset 
{Dataset taken from kaggle - https://www.kaggle.com/datasets/swatikhedekar/exploratory-data-analysis-on-netflix-data/data?select=netflix_titles_2021.csv}

### Tools/Libraries used - 
    1. Pandas
    2. Numpy
    3. Seaborn
    4. Matplotlib

### What new I learnt - 
####  1. Null/missing values in the data can be studied using % method i.e. by analyzing how much % of data is NaN :- 
        This can be done using the following code block - 
        `(df.isnull().sum()/len(df))*100`

###   2. Seaborn-based Heatmap is useful to visualize how much of data is missing values :- 
        Code - 
        `sns.heatmap(df.isnull().sum())`

###   3. Converting `object` type to `date_time` can be done using :-
        Code - 
        `df['date_col'] = pd.to_datetime(df['date_col'], format='mixed OR %d/%m/%y')`
