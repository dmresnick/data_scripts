import mysql.connector
import csv

def connector_db():

    db = mysql.connector.connect(
        host = 'localhost',

        user = 'root',
        password = 'nc5400041',
        db = 'country'
    )

    cursorObject = db.cursor()
    mycursor = db.cursor()




db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'nc5400041',
    db = 'country'
    )

cursorObject = db.cursor()
mycursor = db.cursor()

cursorObject = db.cursor()
mycursor = db.cursor()
sql_main = "INSERT into annualdata (country, indicator, year, amount) VALUES (%s,%s,%s,%s)"
sql_country = "INSERT into countries (countryname) VALUES ('%s')"

countries_clean = []
for i in countries:
    countries_clean.append(i)




for i in countries_clean:
    print(i)
    val_countries = i
    mycursor.execute(sql_country, val_countries)

    db.commit()

'''
for i in country_indicator_list:

    val_main = i
    mycursor.execute(sql_main, val_main)

    mydb.commit()
'''
print(mycursor.rowcount, "record inserted.")
