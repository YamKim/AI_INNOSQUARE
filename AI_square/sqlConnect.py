import sqlite3 as s3  

conn = s3.connect("/mnt/d/dd")
cursor = conn.cursor()

cursor.execute('DROP TABLE if exists Man')
cursor.execute("CREATE TABLE Man( name char(20), age int)")

cursor.execute("INSERT INTO Man VALUES('철수', 47)")
cursor.execute("INSERT INTO Man VALUES('영희', 35)")

for i in range(3):
    name = input(" 이 름: ")
    age  = input(" 나 이: ")

    cursor.execute("INSERT INTO Man(name, age) VALUES(?, ?)", (name, age))

cursor.execute("SELECT * FROM Man")

rows = cursor.fetchall()
print("이름 나이")
print("==========================")

for row in rows:
    print(" {0} {1}".format(row[0], row[1]))

conn.commit()
cursor.close()

conn.close()
