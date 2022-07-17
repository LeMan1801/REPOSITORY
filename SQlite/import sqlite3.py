import sqlite3
from sqlite3.dbapi2 import connect

conn = sqlite3.connect('car.db')

c = conn.cursor()

sql_create_table = """
    CREATE TABLE cars(
        name text,
        brand text,
        year integer
    )
"""
sql_insert = """
    INSERT INTO cars VALUES ('c300', 'Mercedes', 1969)
"""
sql_select = """
    SELECT *FROM cars WHERE brand = 'Mercedes'
"""
sql_update = """
    UPDATE cars set name = 'e200' WHERE brand = 'Mercedes'
"""
try:
    # c.execute(sql_insert)
    # conn.commit()
    # c.execute(sql_select)
    # print(c.fetchmany(2)) # Lấy dữ liệu tới hàng thứ 2
    # print(c.fetchone()) # chỉ lấy được dữ liệu của 1 hàng
    # print(c.fetchall())
    # conn.commit()

    c.execute(sql_update)
    conn.commit()
    c.execute(sql_select)

except:
    print("Query error!")
conn.close()