# BigData-
This is Challenge16 test


## Overview of the analysis 
##### This  purpose it to use new tools to store data and then compare it. We learned in the module that Big Data requires huge cpmputer power and so we need to borrow computers from the internet to process it. New tools and old tools are going to be used: Google colab, Amazon Web Services, pgAdmin, SparkFiles.
##### In this case the data is not huge, though we are going to use the tools to practice using them. 
##### We are going to compare data and check if there is a vias. In this case we are going to retrieve data from AWS. This AWS data will then be transformed into dataframes. 

## 1

#### Data from AWS
<img width="839" alt="Screen Shot 2021-10-17 at 11 25 14 PM" src="https://user-images.githubusercontent.com/25726054/137664693-0d0f3e05-d029-45ab-a471-7e06ff4b3bc1.png">


#### Four different dataframes are created:

###### customers_table DataFrame
<img width="789" alt="Screen Shot 2021-10-17 at 11 27 54 PM" src="https://user-images.githubusercontent.com/25726054/137664916-9c044c4f-bd2b-49aa-89dd-6f4d74959ac4.png">

###### products_table DataFrame and drop duplicates
<img width="661" alt="Screen Shot 2021-10-17 at 11 29 22 PM" src="https://user-images.githubusercontent.com/25726054/137665013-92655986-bc4a-44ed-9f36-31bc7953a41c.png">

###### review_id_table DataFrame. 
<img width="812" alt="Screen Shot 2021-10-17 at 11 30 12 PM" src="https://user-images.githubusercontent.com/25726054/137665097-a894393c-0be8-4a5b-b2aa-cc67699ad0ba.png">

###### vine_table. DataFrame
<img width="797" alt="Screen Shot 2021-10-17 at 11 30 26 PM" src="https://user-images.githubusercontent.com/25726054/137665115-5008ea3b-d305-40fe-823c-27f590f35cd9.png">


##### The final step is to get our transformed raw data into our database. PySpark can easily connect to a database to load the DataFrames into the table. The following is what we need to do, similar to the Bootcamp instruction. 
<img width="563" alt="Screen Shot 2021-10-17 at 11 59 41 PM" src="https://user-images.githubusercontent.com/25726054/137667300-98926d8b-b130-4123-868c-9a4d3dd35311.png">

<img width="757" alt="Screen Shot 2021-10-18 at 12 04 04 AM" src="https://user-images.githubusercontent.com/25726054/137667636-20fe680c-59eb-4ba8-9ba4-0b7f11347b60.png">


## 2

##### Checking if there is any bias towards reviews. The goal is to check if a paid Vine review makes a difference in the percentage of the 5-star review


##### We first generate a DataFrame that the count of reviews is equal or greater than 20.
<img width="564" alt="Screen Shot 2021-10-18 at 1 44 39 AM" src="https://user-images.githubusercontent.com/25726054/137675308-faeb1227-aa19-4707-acad-d4adc663c34f.png">

##### We then filter the tables in two (paid and unpaids reviews)
<img width="612" alt="Screen Shot 2021-10-18 at 1 46 00 AM" src="https://user-images.githubusercontent.com/25726054/137675420-ee75c1b4-32a2-4f21-90c8-fac514967e38.png">
<img width="579" alt="Screen Shot 2021-10-18 at 1 46 10 AM" src="https://user-images.githubusercontent.com/25726054/137675442-125ebbc9-b805-47c2-bea4-0cb30bd6b88d.png">

##### The count and percentage of paid and unpaid are calculated. 
<img width="502" alt="Screen Shot 2021-10-18 at 1 59 09 AM" src="https://user-images.githubusercontent.com/25726054/137676733-007d1917-4e13-412e-97c2-71879064925a.png">
<img width="526" alt="Screen Shot 2021-10-18 at 1 59 37 AM" src="https://user-images.githubusercontent.com/25726054/137676775-3e9bd444-ba92-4e2e-971a-674c512fb44a.png">


