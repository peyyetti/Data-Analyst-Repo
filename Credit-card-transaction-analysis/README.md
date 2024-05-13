This project involved cleaning and analysing a Credit Card transaction dataset. This dataset was present in `.xlsx` format and was connected to `PostGreSQL` database to be analyzed in full.
This uploaded dataset was then connected to `PowerBI` to draw insights by creating interactive Visualizations on the data.

I learned many new techniques and methodologies and have made a short list of them as follows :

- connecting sql to `.csv` file using the following command:

`COPY table_name
FROM 'file_path_of_csv'
DELIMITER ','
CSV HEADER;`

- used `DAX` query to create a new column of `Age Group` using the query:

`SWITCH( TRUE(),
	age_col < age_val1, 'age_val1_bucket',
	age_col>= age_val1 && age_col<age_val2, 'age_val2_bucket',
	'default_val'
)`

- using `DAX` query to extract week number using the command:
	
	`WEEKNUM(date_col)`

- using filter function using:

	`FILTER( ALL(column_name), <filter_column condition>)`

- finding week over week revenue ->
	
	`DIVIDE((current_week_revenue - previous_week_revenue), previous_week_revenue)`

The tutorial followed for this project is : https://www.youtube.com/watch?v=8XoDVwWdaqI&ab_channel=RishabhMishra
