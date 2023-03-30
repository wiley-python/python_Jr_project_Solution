# STOCK MANAGEMENT

import os
import mysql.connector
import datetime
import numpy as np
import matplotlib.pyplot as plt

now = datetime.datetime.now()


class database:
    def create_database(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root",database="stock")
        mycursor = mydb.cursor()
        print("Creating database")
        sql="create database if not exists stock"
        mycursor.execute(sql)
        print(" Creating PRODUCT table")
        sql = "CREATE TABLE if not exists product (\
                      pcode int(4) PRIMARY KEY,\
                      pname char(30) NOT NULL,\
                      pprice float(8,2) ,\
                      pqty int(4) ,\
                      pcat char(30));"
        mycursor.execute(sql)
        print(" Creating ORDER table")
        sql = "CREATE TABLE if not exists orders (\
                      orderid int(4)PRIMARY KEY ,\
                      orderdate DATE ,\
                      pcode char(30) NOT NULL , \
                      pprice float(8,2) ,\
                      pqty int(4) ,\
                      supplier char(50),\
                      pcat char(30));"
        mycursor.execute(sql)
        print(" ORDER table created")

    def list_database(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        sql = "show tables;"
        mycursor.execute(sql)
        for i in mycursor:
            print(i)


db = database()
db.create_database()
db.list_database()


class order:
    def add_order(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        now = datetime.datetime.now()
        sql = "INSERT INTO orders(orderid,orderdate,pcode,pprice,pqty,supplier,pcat) values (%s,%s,%s,%s,%s,%s,%s)"
        code = '1'
        oid = now.year + now.month + now.day + now.hour + now.minute + now.second
        qty = '10'
        price = '200.30'
        cat = 'clothing'
        supplier = 'anutex'
        val = (oid, now, code, price, qty, supplier, cat)
        mycursor.execute(sql, val)
        mydb.commit()
        res = mycursor.rowcount
        print(res, "rows inserted")
        return res

    def list_order(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        sql = "SELECT * from orders"
        mycursor.execute(sql)
        res = mycursor.rowcount
        return res

    def drop_order(selfself):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        sql = "drop table orders"
        mycursor.execute(sql)
        print("drop table orders successfully")


order = order()
order.add_order()
order.list_order()
order.drop_order()


class product:
    def add_product(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        sql = "INSERT INTO product(pcode,pname,pprice,pqty,pcat) values (%s,%s,%s,%s,%s)"
        code = '1'
        search = "SELECT count(*) FROM product WHERE pcode=%s;"
        val = (code,)
        mycursor.execute(search, val)
        for x in mycursor:
            cnt = x[0]
        if cnt == 0:
            name = 'dress'
            qty = '10'
            price = '200.30'
            cat = 'clothing'
            val = (code, name, price, qty, cat)
            mycursor.execute(sql, val)
            mydb.commit()
            res = mycursor.rowcount
            print(res, "rows inserted")
            return res
        else:
            print("\t\t Product already exist")

    def update_product(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        code = 1
        qty = 10
        sql = "UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
        val = (qty, code)
        mycursor.execute(sql, val)
        mydb.commit()
        print("\t\t Product details updated")
        res = mycursor.rowcount
        print(res, "rows updated")
        return res

    def list_product(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        sql = "SELECT * from product"
        mycursor.execute(sql)
        res = mycursor.rowcount
        print(res)
        return res

    def delete_product(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        code = '1'
        sql = "DELETE FROM product WHERE pcode = %s;"
        val = (code,)
        mycursor.execute(sql, val)
        mydb.commit()
        res = mycursor.rowcount
        print(res, " record(s) deleted");
        return res

    def drop_product(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        sql = "drop table product"
        mycursor.execute(sql)
        print("drop table product successfully")


product = product()
product.add_product()
product.list_product()
product.update_product()
product.list_product()
product.delete_product()
product.drop_product()


class StudentDatabase:
    def db_setup(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        print(" Creating student table")
        sql = "CREATE TABLE if not exists Students( Id int, Name varchar(20), M1 int, M2 int, M3 int);"
        mycursor.execute(sql)
        print("table created")
        print("inserting student details")
        sql = "INSERT INTO Students (Id,Name,M1,M2,M3) VALUES (%s, %s, %s, %s,%s);"
        val = [(1, 'Neha', 90, 80, 90),
               (2, 'Sahil', 50, 60, 80),
               (3, 'Rohan', 70, 70, 80),
               (4, 'Ankita', 80, 40, 75),
               (5, 'Rahul', 65, 50, 70),
               (6, 'Swati', 55, 70, 65),
               (7, 'Alka', 75, 80, 75)]
        mycursor.executemany(sql, val)
        mydb.commit()
        print("inserted data")

    def report_generation(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()

        print("Report Card Analysing...")
        sql = '''select Id, Name , M1,M2,M3, (M1+M2+M3) as sum, 
              concat(round((((M1+M2+M3) / 300) * 100 ),2), '%') as percentage
              from Students;'''
        mycursor.execute(sql)

        result = mycursor.fetchall()

        for x in result:
            print(x)
        return result

    def drop_db(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        sql = "drop table Students"
        mycursor.execute(sql)
        print("drop table Students successfully")

    def report_M1(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
        mycursor = mydb.cursor()
        mycursor.execute("select Name, M1 from Students")
       # result = mycursor.fetchall
        Names = []
        M1 = []

        for i in mycursor:
            Names.append(i[0])
            M1.append(i[1])

        print("Name of Students = ", Names)
        print("Marks of Students = ", M1)

        # Visualizing Data using Matplotlib
        plt.bar(Names, M1)
        plt.ylim(0, 100)
        plt.xlabel("Name of Students")
        plt.ylabel("M1 Marks of Students")
        plt.title("Student's Information")
        plt.show()


stu = StudentDatabase()
stu.db_setup()
stu.report_generation()
stu.report_M1()
stu.drop_db()
