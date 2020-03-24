
import pymysql

conn = pymysql.connect(host='localhost',user="root",password="Ling0.0",db="bus",charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

line_name = 高峰专线12路(海岸 

sql = """
select * from busstops
where site_name = "风和日丽" &&
"""

# 执行SQL语句
cursor.execute(sql)

for item in cursor.fetchall():
    print(item)

# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()