## This is a project I made to analyze the user behaviour and post creation patterns on the site Hacker News

Original dataset is - https://www.kaggle.com/datasets/hacker-news/hacker-news-posts

But I used a trimmed down dataset from Dataquest guided project - https://app.dataquest.io/c/62/m/356/guided-project%3A-exploring-hacker-news-posts/1/introduction 

## My learnings - 

### 1. Wrote code to classify/categorize month number (i.e. Jan = 1) into Quarters (Q1, Q2, Q3, Q4) and stored in DataFrame :- 
    b = []
    for i in range(len(hn['month_created'])):
      a = hn['month_created'].iloc[i]
      if a<4:
          b.append('Q1')
      elif a>=4 and a<7:
          b.append('Q2')
      elif a>=7 and a<10:
          b.append('Q3')
      elif a>=10 and a<12:
          b.append('Q4')
  
    qtr_df = pd.DataFrame({'qtr':b})
  
### 2. Used groupby to group the posts according to hour of the day they were posted on :-
    hn['num_points'].groupby(hn['created_at'].dt.hour).sum().sort_values(ascending=False)

## Conclusions - 

### 1. Most posts were added in Q3 i.e. July, August and September!

### 2. Most posts are created at 17:00 hours, while max. freq of posts being created b/w 13:00 to 19:00 hours 
