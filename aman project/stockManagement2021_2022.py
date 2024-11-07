# STOCK MANAGEMENT
import os
import mysql.connector
import datetime
now = datetime.datetime.now()
#print(now)
def product_mgmt( ):
        while True :
                print("\t\t\t 1. Add New Product")
                print("\t\t\t 2. List Product")
                print("\t\t\t 3. Update Product")
                print("\t\t\t 4. Delete Product")
                print("\t\t\t 5. Back (Main Menu)")
                ch=int (input("\t\tEnter Your Choice (1-5):"))
                if ch==1:
                        add_product()
                elif ch==2:
                        search_product()
                elif ch==3:
                        update_product()
                elif ch==4:
                        delete_product()
                elif ch== 5 :
                        break

def purchase_mgmt( ):
        while True :
                print("\t\t\t 1. Add Order")
                print("\t\t\t 2. List Order")
                print("\t\t\t 3. Back (Main Menu)")
                ch=int (input("\t\tEnter Your Choice (1-3) :"))
                if ch==1 :
                        add_order()
                elif ch==2 :
                        list_order()
                elif ch== 3 :
                        break

def sales_mgmt( ):
        while True :
                print("\t\t\t 1. Sale Items")
                print("\t\t\t 2. List Sales")
                print("\t\t\t 3. Back (Main Menu)")
                ch=int (input("\t\tEnter Your Choice (1-3):"))
                if ch== 1 :
                        sale_product()
                elif ch== 2 :
                        list_sale()
                elif ch== 3 :
                        break

def user_mgmt( ):
        while True :
                print("\t\t\t 1. Add user")
                print("\t\t\t 2. List user")
                print("\t\t\t 3. Back (Main Menu)")
                ch=int (input("\t\tEnter Your Choice (1-3):"))
                if ch==1:
                        add_user()
                elif ch==2:
                        list_user()
                elif ch==3:
                        break

def create_database():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock")
        mycursor=mydb.cursor()
        
        sql = "CREATE TABLE if not exists product (\
        pcode int(4) PRIMARY KEY,\
        pname char(30) NOT NULL,\
        pprice float(8,2) ,\
        pqty int(4) ,\
        pcat char(30));"
        mycursor.execute(sql)
        print(" PRODUCT table created")                             
       
        sql = "CREATE TABLE if not exists orders (\
        orderid int(4)PRIMARY KEY ,\
        orderdate DATE ,\
        pcode char(30) NOT NULL , \
        pprice float(8,2) ,\
        pqty int(4) ,\
        supplier char(50),\
        pcat char(30));"
        mycursor.execute(sql)
        print(" ORDERS table created")
                                     
        sql = "CREATE TABLE if not exists sales (\
        salesid int(4) PRIMARY KEY ,\
        salesdate DATE ,\
        pcode char(30) references product(pcode), \
        pprice float(8,2) ,\
        pqty int(4) ,\
        Total double(8,2)\
        );"
        mycursor.execute(sql)
        print(" SALES table created")
        
        sql = "CREATE TABLE if not exists user (\
        uid char(6) PRIMARY KEY,\
        uname char(30) NOT NULL,\
        upwd char(30));"
        mycursor.execute(sql)
        print(" USER table created")

def list_database():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock") 
        mycursor=mydb.cursor()
        sql="show tables;"
        mycursor.execute(sql)
        for i in mycursor:
                print(i)

def add_order():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock") 
        mycursor=mydb.cursor()
        now = datetime.datetime.now()
        sql="INSERT INTO orders (orderid, orderdate, pcode, pprice, pqty,supplier, pcat)\
                values (%s,%s,%s,%s,%s,%s,%s)"
        code=int(input("Enter product code :"))
        oid=now.year+now.month+now.day+now.hour+now.minute+now.second #to generate unique orderID
        qty=int(input("Enter product quantity : "))
        price=float(input("Enter Product unit price: "))
        cat=input("Enter product category: ")
        supplier=input("Enter Supplier details: ")
        val=(oid,now,code,price,qty,supplier,cat)
        mycursor.execute(sql,val)
        mydb.commit()

def list_order():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql", database="stock")
        mycursor=mydb.cursor()
        sql="SELECT * from orders"
        mycursor.execute(sql)
        print("\t\t\t\t ORDER DETAILS")
        print("-"*110)
        print("Order ID \t  Date \t     Product Code \tPrice\tQuantity \t  Supplier \tCategory")
        print("-"*110)
        for i in mycursor:
                print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t ",i[5],"\t",i[6])
        print("-"*110)

def db_mgmt( ):
        while True :
                print("\t\t\t 1. Database Creation")
                print("\t\t\t 2. List Database")
                print("\t\t\t 3. Back (Main Menu)")
                ch=int (input("\t\tEnter Your Choice (1-3):"))
                if ch==1 :
                        create_database()
                elif ch==2 :
                        list_database()
                elif ch== 3 :
                        break

def add_product():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock")
        mycursor=mydb.cursor()
        sql="INSERT INTO product(pcode,pname,pprice,pqty,pcat) values(%s,%s,%s,%s,%s)"
        code=int(input("\t\tEnter product code :")) #finding total no. of records of this code
        search="SELECT count(*) FROM product WHERE pcode=%s;" 
        val=(code,)
        mycursor.execute(search,val)
        for x in mycursor:
                cnt=x[0]
        if cnt==0:
                name=input("\t\tEnter product name :")
                qty=int(input("\t\tEnter product quantity :"))
                price=float(input("\t\tEnter product unit price :"))
                cat=input("\t\tEnter Product category :")
                val=(code,name,price,qty,cat)
                mycursor.execute(sql,val)
                mydb.commit()
        else:
                print("\t\tProduct already exists")

def update_product():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock")
        mycursor=mydb.cursor()
        code=int(input("Enter the product code :"))
        qty=int(input("Enter the quantity :"))
        sql="UPDATE product SET pqty=pqty+%s WHERE pcode=%s"
        val=(qty,code)
        mycursor.execute(sql,val)
        mydb.commit()
        print("\t\tProduct details updated")

def delete_product():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock")
        mycursor=mydb.cursor()
        code=int(input("Enter the product code :"))
        sql="DELETE FROM product WHERE pcode = %s"
        val=(code,)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount," record(s) deleted");

def search_product():
        while True :
                print("\t\t\t 1. List all product")
                print("\t\t\t 2. List product code wise")
                print("\t\t\t 3. List product categoty wise")
                print("\t\t\t 4. Back (Main Menu)")
                ch=int (input("\t\tEnter Your Choice (1-4):"))
                if ch==1 :
                        list_product()
                elif ch==2 :
                        list_prcode()
                elif ch==3 :
                        list_prcat()
                elif ch== 4 :
                        break

def list_product():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock")
        mycursor=mydb.cursor()
        sql="SELECT * from product"
        mycursor.execute(sql)
        print("\t\t\t\t PRODUCT DETAILS")
        print("\t\t","-"*60)
        print("\t\t code \tname \tprice \tquantity \tcategory")
        print("\t\t","-"*60)
        for i in mycursor:
                print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t ",i[3],"\t",i[4])
        print("\t\t","-"*60)

def list_prcode():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock")
        mycursor=mydb.cursor()
        code=int(input(" Enter product code :"))
        sql="SELECT * from product WHERE pcode=%s"
        val=(code,)
        mycursor.execute(sql,val)
        print("\t\t\t\t PRODUCT DETAILS")
        print("\t\t","-"*60)
        print("\t\t code \tname \tprice \tquantity \tcategory")
        print("\t\t","-"*60)
        for i in mycursor:
                print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t ",i[3],"\t",i[4])
        print("\t\t","-"*60)

def sale_product():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock")
        mycursor=mydb.cursor()
        pcode=input("Enter product code: ")
        sql="SELECT count(*) from product WHERE pcode=%s;"
        val=(pcode,)
        mycursor.execute(sql,val)
        for x in mycursor:
                                     cnt=x[0]
        if cnt !=0 :
                sql="SELECT * from product WHERE pcode=%s;"
                val=(pcode,)
                mycursor.execute(sql,val)
                for x in mycursor:
                        print(x)
                        price=int(x[2])
                        pqty=int(x[3])
                        qty=int(input("Enter quantity to sell :"))# qty is the quantity for sale
                if qty <= pqty: #pqty is the actual quantity(qoh)in the table, must be>=qty for sale
                        total=qty*price;
                        print ("Collect Rs. ", total)
                        sql="INSERT into sales values(%s,%s,%s,%s,%s,%s)"
                        sid=now.year+now.month+now.day+now.hour+now.minute+now.second #to generate unique salesID
                        val=(sid,datetime.datetime.now(),pcode,price,qty,total)
                        mycursor.execute(sql,val)
                        sql="UPDATE product SET pqty=pqty-%s WHERE pcode=%s"
                        val=(qty,pcode)
                        mycursor.execute(sql,val)
                        mydb.commit()
                else:
                        print("Quantity not Available..!! Please enter qty<=quantity on hand")
        else:
                print("Product is not avalaible")

def list_sale():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock")
        mycursor=mydb.cursor()
        sql="SELECT * FROM sales"
        mycursor.execute(sql)
        print(" \t\t\t\tSALES DETAIL")
        print("-"*100)
        print("SalesID \t    Date \t    Product Code \tPrice\t\tQuantity \tTotal Amount")
        print("-"*100)  
        for x in mycursor:
                                     print(x[0],"\t",x[1],"\t",x[2],"\t ",x[3],"\t\t",x[4],"\t",x[5])
                                     print("-"*100)

def list_prcat():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock")
        mycursor=mydb.cursor()
        #print (cat)
        cat=input("Enter category :")
        sql="SELECT * from product WHERE pcat =%s"
        val=(cat,)
        mycursor.execute(sql,val)
        #clrscr()
        print("\t\t\t\t PRODUCT DETAILS")
        print("\t\t","-"*60)
        print("\t\t code \tname \tprice \tquantity \tcategory")
        print("\t\t","-"*60)
        for i in mycursor:
                                     print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t ",i[3],"\t",i[4])
                                     print("\t\t","-"*60)

def add_user():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock")
        mycursor=mydb.cursor()
        uid=input("Enter User Id (max. 6 chars):")
        name=input("Enter Name :")
        paswd=input("Enter Password :")
        sql="INSERT INTO user values (%s,%s,%s);"
        val=(uid,name,paswd)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, " user created")

def  list_user():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="sql",database="stock")
        mycursor=mydb.cursor()
        sql="SELECT uid,uname from user"
        mycursor.execute(sql)
        print("\t\t\tUSER DETAILS")
        print("\t\t","-"*27)
        print("\t\t UID \tUser Name ")
        print("\t\t","-"*27)
        for i in mycursor:
                                     print("\t\t",i[0],"\t",i[1])
                                     print("\t\t","-"*27)
def team():
        print("""
                                                          Dynasty Modern Gurukul Academy 
                                                           STOCK MANAGEMENT SYSTEM 
                                --------------------------------------------------------------------------
                                                          Designed and Maintained By: 
                                Shivani Bhatt     - CLASS XII A - ROLL NO - 25640382[2021-2022]
                                Shivani Samant  - CLASS XII A - ROLL NO - 25640384[2021-2022]
                                Nikita Verma      - CLASS XII A - ROLL NO - 25640335[2021-2022]
                                Suraj Singh        - CLASS XII C - ROLL NO - 25640391[2021-2022]
                                ---------------------------------------------------------------------------
                """)
#__main()__
team()
print("Please run DATABASE SETUP at first")
#create_database()
while True:
        print("\t\t             STOCK MANAGEMENT")
        print("\t\t **************************")
        print("\t\t 1. PRODUCT MANAGEMENT")
        print("\t\t 2. PURCHASE MANAGEMENT")
        print("\t\t 3. SALES MANAGEMENT")
        print("\t\t 4. USER MANAGEMENT")
        print("\t\t 5. DATABASE SETUP")
        print("\t\t 6. EXIT\n")
        n=int(input("Enter your choice (1-6):"))
        if n== 1:
                product_mgmt()
        elif n== 2:
                purchase_mgmt()
        elif n== 3:
                sales_mgmt()
        elif n== 4:
               user_mgmt()
        elif n==5:
                db_mgmt()
        elif n== 6:
                break
print("Thank You...")
