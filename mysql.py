import  pymysql

db = pymysql.connect ("localhost","example","username","example_table")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("Database version : %s " % data)
db.close()

