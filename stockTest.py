
import mysql.connector
import stockmanagement


def test_before_add_order():
        stockmanagement.db.create_database()
        act = stockmanagement.order.list_order()
        exp = 0
        assert act == exp
        stockmanagement.order.drop_order()

def test_after_add_order():
    stockmanagement.db.create_database()
    act1 = stockmanagement.order.add_order()
    exp1 = 1
    assert act1 == exp1
    stockmanagement.order.drop_order()

def test_before_add_product():
    stockmanagement.db.create_database()
    act = stockmanagement.product.list_product()
    exp = 0
    assert act == exp
    stockmanagement.product.drop_product()

def test_after_add_product():
    stockmanagement.db.create_database()
    act = stockmanagement.product.add_product()
    exp = 1
    assert act == exp
    stockmanagement.product.drop_product()

def test_after_update_product():
    stockmanagement.db.create_database()
    stockmanagement.product.add_product()
    act = stockmanagement.product.update_product()
    exp = 1
    assert  act == exp
    stockmanagement.product.drop_product()

def test_after_delete_product():
    stockmanagement.db.create_database()
    stockmanagement.product.add_product()
    stockmanagement.product.delete_product()
    act = stockmanagement.product.list_product()
    exp = 0
    assert act == exp
    stockmanagement.product.drop_product()


def test_report_generation():
    stockmanagement.s.db_setup()

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="stock")
    mycursor = mydb.cursor()

    print("Report  Analysing...")
    sql = '''select salesid, ProductName , yr2021,yr2022,yr2023, (yr2021+yr2022+yr2023) as sum, 
              concat(round((((yr2021+yr2022+yr2023) / 300) * 100 ),2), '%') as percentage
              from sales;'''
    mycursor.execute(sql)

    exp = mycursor.fetchall()
    act = stockmanagement.s.report_generation()
    assert exp == act
