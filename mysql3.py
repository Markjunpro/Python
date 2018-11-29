import pymysql
db = pymysql.connect("localhost","example","example_password","example_table")
cursor = db.cursor()
sql = """select * from password """
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[1]
        name = row[1]
        password = row[2]
        other = row[3]
        print("id : %s,name: %s,password : %s,other : %s " % (id ,name ,password ,other))
except:
    print ( " Error : unable to fetch data")

db.close()


