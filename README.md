# python_Jr_project_Solution
Problem Statement
RV traders are into different business sectors. Their growth in business is well known and is one of the most popular business groups. As the business started to grow, RV Traders found it difficult to keep a track of  inventory levels, sales, and order fulfillment. Hence RV traders wanted to have a software which can track some of their business details. A stock management project can help businesses improve their inventory control and streamline their order fulfillment process, ultimately leading to increased customer satisfaction and profitability.
Current System
The current system for stock management in RV traders is manual tracking of inventory levels, sales, and order fulfilment using spreadsheets or paper-based records. The manual process of updating inventory levels and sales data also leads to delays in order processing and fulfilment, which impacts in customer satisfaction.
Project Scope/Functionalities
The Project should include the below functionality:
•	Order fulfilment system.
o	This system will track incoming orders and ensure that the necessary products are pulled from the inventory to fulfil the orders.
Table Structure
orderid	int	NO	PRI
orderdate	date	YES	
pcode	char(30)	NO	
pprice	float(8,2)	YES	
pqty	int	YES	
supplier	char(50)	YES	
pcat	char(30)	YES	

•	Sales Tracking System.
o	This system will record sales data for each product, including the number of units sold, the year of sale, and the price at which the product was sold.
Table Structure
salesid	int	YES
Productname	varchar(20)	YES
yr2021	int	YES
yr2022	int	YES
yr2023	int	YES

	Product Tracking System
o	This system will record product details including product code, price, product quantity, and category to generate the report as and when required.
Table Structure
pcode	int	NO	PRI
pname	char(30)	NO	
pprice	float(8,2)	YES	
pqty	int	YES	
pcat	char(30)	YES	

Files to be Edited:
In this project you need to implement: 
step-1: setup database in class - database 
with different methods - 
create_database - 
(Includes connecting to db with credentials host="localhost", user="root", passwd="root",database="stock")
create a db of name stock
create a table product
create a table order
list_database -
show tables 
functionality - shows the tables that you created 

step-2: implement order management in class order
with different methods
add_order -
functionality - adding order details to the database
list_order - 
functionality - list all the orders from the database
drop_order -
functionality - delete all data from the order table

step-3: implement product management in class product
with following methods
add_product -
functionality - add product details to the database
update_product -
functionality - update product details to the database
list_product -
functionality - list all the product details from database
delete_product -
functionality - delete product from database with where pcode 
drop_product -
functionality - drop product table from database
step - 4
setup student database with sales class 
with following methods
db_setup -
create table sales with columns of (salesid int, ProductName varchar(20), yr2021 int, yr2022 int, yr2023 int)
report_generation-
generate report of  sales with their total and percentage 
drop_db:
functionality: drop table sales
report_yr2021:
functionality: data visualization of yr2021  in a bar graph with (ProductNames and yr2021 marks as x and y axies )	
----------Steps to Solve the Problem---------
Step1: Make sure you have Required Tools:
	Python latest version
	VS Code IDE with Required Plugins for Python, GIT.
	Git
Step2: Accessing GITHUB Classroom and submiting Assignment:
	Get the Link for GITHUB Classroom.
	Click and Authorize from your GITHUB account.
	Clone the Repository / open through VSCODE IDE.
	Open SpringDITodosApp --> src --> main --> Java Files to complete code.
	Solve the Problem Statements through code as detailed in Step 3 below.
	Commit the changes to the repositories, labelling each commit numerically (Commit1, Commit2, etc.).
	Each commit will be tested automatically against the relevant testcases, so you may need to submit several commits as you refine your solution.
	Once you are finished with the assignment (either all test cases passed or not),  make sure to lable this commit as "final commit" (this may mean a previous commit passing and you making a slight edit to the latter in order to mark the next commit as being final).

Step3: Solving the Problem:
	Read the Problem Statement carefully
	Go to respective files to complete assignment
	Please follow below pattern in the files where you can complete the code
	AS TEST CASES ARE EXECUTED USING AUTOMATION TECHNIQUE, REQUEST TO STRICTLY FOLLOW BELOW MENTIONED RULE
	THE REST OF THE CODE PROVIDED TO YOU SHOULD BE KEPT STRICTLY UNTOUCHED.
	THE CLASS NAMES, INTERFACE NAMES, METHOD SIGNATURES AND ATTRIBUTE NAMES SHOULD NOT BE ALTERED OR MODIFIED AND KEPT STRICTLY UNTOUCHED.

Note: Every Assignment is being tested with Automation Technique. So Please do follow the points mentioned in comments of Java Code.
