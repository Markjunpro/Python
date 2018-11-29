import pymysql

db = pymysql.connect("localhost","example", "example_password","example_table")
cursor = db.cursor()
sql = """insert into password ( name,password) 
    values('example','exmaple')
    """
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()


