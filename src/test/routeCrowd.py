
import pymysql
import checkName
import pymongo
conn = pymysql.connect(host='localhost',user="root",password="Ling0.0",db="bus",charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

mongodbClient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = mongodbClient["MetroVSz"]
routes = mydb["routes"]
crowdRoutes = mydb["crowdRoutes"]

#查询一天,线路的拥挤度
def mySQLQuery(matchPattern):
    res = []
    for i in range(0,24):
        startTime = f"{i}:00:00"
        endTime = f"{i+1}:00:00" if ((i + 1)%24 != 0) else "23:59:59"
        sql = f"""
        select '{i}-{i+1}点' as '时间', count(*) as 总数
        from bus_record where line like '{matchPattern}' and 
        card_t between '2017-04-04 {startTime}' and '2017-04-04 {endTime}'
        """
        # 执行SQL语句
        cursor.execute(sql)
        res.append(cursor.fetchall()[0]['总数'])
    return res

i = 0
validRoutes = routes.find({'matchPattern':{'$not':{'$eq':''}}},{'_id':0,'name':1,'new_name':1,'startTime':1,'endTime':1,'matchPattern':1})
totalNums = validRoutes.count()
for route in validRoutes:
    i+=1
    data = mySQLQuery(route['matchPattern'])
    crowdRoutes.insert_one({
        'date':'2017-04-04',
        'line_name': route['name'],
        'new_name':route['new_name'],
        'startTime':route['startTime'],
        'endTime':route['endTime'],
        'matchPattern':route['matchPattern'],
        'data':data,
    })
    print(f"当前为{i}条,共{totalNums}条")
    

# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()