import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('SQL_Money')
        print("Success")
        return con
        
    except Error:
        print(Error)


def sql_Employee(con):
    cursorObj = con.cursor()
    cursorObj.execute(    
        "CREATE TABLE Employee("
        "Id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "Name TEXT NOT NULL,"
        "Surname TEXT NOT NULL)"
    )
    
def sql_Currency(con):
    cursorObj = con.cursor()
    cursorObj.execute(    
        "CREATE TABLE Currency("
        "Id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "Name TEXT NOT NULL)"
    )
    
def sql_Exchange(con):
    cursorObj = con.cursor()
    cursorObj.execute(    
        "CREATE TABLE Exchange("
        "Id INTEGER NOT NULL,"
        "Price_sell INTEGER NOT NULL,"
        "Price_buy INTEGER NOT NULL,"
        "FOREIGN KEY (Id)  REFERENCES Currency (id))"
    )
def sql_Client(con):
    cursorObj = con.cursor()
    cursorObj.execute(    
        "CREATE TABLE Operations("
        "Id INTEGER PRIMARY KEY,"
        "Name TEXT,"
        "Surname TEXT)"
    )    
    
def sql_Operations(con):
    cursorObj = con.cursor()
    cursorObj.execute(    
        "CREATE TABLE Operations("
        "Id INTEGER PRIMARY KEY,"
        "Id_employee INTEGER NOT NULL,"
        "Id_currency INTEGER NOT NULL,"
        "Count INTEGER NOT NULL CHECK (Count > 0),"
        "Type TEXT NOT NULL CHECK (Type = 'Покупка' OR Type = 'Продажа'),"
        "FOREIGN KEY (Id_employee)  REFERENCES Employee (id),"
        "FOREIGN KEY (Id_currency)  REFERENCES Currency (id))"
    )
def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE Exchange SET Price_sell = 0 where Price_buy > 20')
    con.commit()


def sql_delete(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE from Employee where Name = "Alex" ')
    con.commit()

def sql_insert(con):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO Client "
        "VALUES(50,'Alex','Danilov')")
    con.commit()
    
    
def select(con):
    print("Command: insert, update, delete, exit")
    s = input()
    while s != "exit":
        if s == "insert":
            sql_insert(con)
        elif s == "delete":
            sql_delete(con)
        elif s == "update":
            sql_update(con)
        else:
            print("Please enter insert, update or delete!")
            
            
con = sql_connection()
#sql_insert(con)
#sql_Exhibition(con)
#sql_Excurse(con)
#sql_Stand(con)
#sql_StandMan(con)
#sql_ClientExcurse(con)
#sql_Client(con)

select(con)
