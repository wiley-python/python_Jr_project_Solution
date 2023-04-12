# python_Jr_project_Solution
## Problem Statement

RV traders are into different business sectors. Their growth in business is well known and is one of the most popular business groups. As the business started to grow, RV Traders found it difficult to keep a track of  inventory levels, sales, and order fulfillment. Hence RV traders wanted to have a software which can track some of their business details. A stock management project can help businesses improve their inventory control and streamline their order fulfillment process, ultimately leading to increased customer satisfaction and profitability.

## Current System

The current system for stock management in RV traders is manual tracking of inventory levels, sales, and order fulfilment using spreadsheets or paper-based records. The manual process of updating inventory levels and sales data also leads to delays in order processing and fulfilment, which impacts in customer satisfaction.

## Project Scope/Functionalities

**The Project should include the below functionality:**

Order fulfilment system.
      _This system will track incoming orders and ensure that the necessary products are pulled from the inventory to fulfil the orders._
      
Sales Tracking System.
      _This system will record sales data for each product, including the number of units sold, the year of sale, and the price at which the product was sold._
      
Product Tracking System
      _This system will record product details including product code, price, product quantity, and category to generate the report as and when required._

### Files to be Edited:
In this project you need to implement:

**step-1**: setup database in class - **database** 
   with different methods - 
     **create_database** - 
           _(Includes connecting to db with credentials host="localhost", user="root", passwd="root",database="stock")_
            _create a db of name stock
            create a table product with columns of 
                 (pcode int(4) PRIMARY KEY,
                  pname char(30) NOT NULL,
                  pprice float(8,2),
                  pqty int(4),
                  pcat char(30))
            create a table order with columns of 
                   (orderid int(4)PRIMARY KEY,
                   orderdate DATE ,
                   pcode char(30) NOT NULL ,
                   pprice float(8,2) ,
                   pqty int(4) ,
                   supplier char(50),
                   pcat char(30))_
      **list_database** -
           show tables  -  _functionality - shows the tables that you created _
 **step-2**: implement order management in class **order**
           with different methods
              **add_order** - _functionality - adding order details to the database_
              **list_order** - _functionality - list all the orders from the database_
              **drop_order** - _functionality - delete all data from the order table_
     **step-3**: implement product management in class **product**
            with following methods
               **add_product** - _functionality - add product details to the database_
               **update_product** - _functionality - update product details to the database_
               **list_product** - _functionality - list all the product details from database_
               **delete_product** - _functionality - delete product from database with where pcode _
               **drop_product **- _functionality - drop product table from database_
     **step - 4**: setup sales database with **sales class **
             with following methods
             **db_setup** - _create table sales with columns of 
                       (salesid int, 
                       ProductName varchar(20), 
                       yr2021 int, 
                       yr2022 int, 
                       yr2023 int)_
             **report_generation** - _generate report of  sales with their total and percentage _
             **drop_db** : functionality: _drop table sales_
             **report_yr2021**: functionality: _data visualization of yr2021  in a bar graph with 
                     (ProductNames and yr2021 marks as x and y axies )_
                     
# --------Steps to Solve the Problem---------

## Step1: Make sure you have Required Tools:

                Python latest version

                VS Code IDE with Required Plugins for Java, GIT.

                Git

## Step2: Accessing GITHUB Classroom and submiting Assignment:

                  Get the Link for GITHUB Classroom.

                  Click and Authorize from your GITHUB account.

                  Clone the Repository / open through VSCODE IDE.

                  Open stockmanagement.py File to complete code.

                  Solve the Problem Statements through code as detailed in Step 3 below.

                  Commit the changes to the repositories, 
                  labelling each commit numerically (Commit1, Commit2, etc.).

                  Each commit will be tested automatically against the relevant testcases, 
                  so you may need to submit several commits as you refine your solution.

                  Once you are finished with the assignment (either all test cases passed or not), 
                  make sure to lable this commit as "final commit" 
                  (this may mean a previous commit passing and 
                  you making a slight edit to the latter in order to mark 
                  the next commit as being final).

## Step3: Solving the Problem:

      Read the Problem Statement carefully

      Go to respective files to complete assignment
      
      AS TEST CASES ARE EXECUTED USING AUTOMATION TECHNIQUE, REQUEST TO
      
      STRICTLY FOLLOW BELOW MENTIONED RULES
      
      1. THE REST OF THE CODE PROVIDED TO YOU SHOULD BE KEPT STRICTLY UNTOUCHED.
      
      2. YOUR OWN CODE WOULD COME ONLY INSIDE CLASSES AND METHODS WHICH ARE MENTIONED.
      
      3. THE CLASS NAMES, INTERFACE NAMES, METHOD SIGNATURES AND ATTRIBUTE NAMES SHOULD
      
        NOT BE ALTERED OR MODIFIED AND KEPT STRICTLY UNTOUCHED.
          
    
Note: Every Assignment is being tested with Automation Technique. So Please do follow the points mentioned.

