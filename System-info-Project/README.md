This is a project I prepared by using Python, PostGreSQL and PowerBI

Intent behind the making of the project is as follows:
  - Learn and understand how live system data is accessed using `psutil` library
  - Learn how `time` module of Python can be used to create desired time intervals for recording data
  - Learn how data can be funneled from Python into PostGreSQL database using `psycopg2` library
  - Learn how PowerBI can be connected to PostGreSQL to access live system data
  - Learn how dashboard for live monitoring of `CPU Usage`, `Memory Usage`, `Disk Usage` and `Bytes sent vs Bytes recieved` can be created

The files uploaded contain the following details:
  - `.py` file -> Contains the script for accessing the system info using `psutil` and `time` modules and funneling this data into the PostGreSQL database using `psycopg2` module
  - `.pbix` file -> PowerBI file that contains the dashboard prepared to visualize the obtained system info
  - `.sql` file -> Contains the commands to create a table with relevant column names and datatypes within PostGreSQL. This table will contain the system info data generated and sent by Python file. 

Tutorial followed for this project is : https://www.youtube.com/watch?v=9VtkwH6iLL0&ab_channel=ViSIT
