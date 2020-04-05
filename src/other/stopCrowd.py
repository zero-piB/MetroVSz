
import pymysql
import pymongo
import json
from mytime import * 

timeDiff = 3600
conn = pymysql.connect(host='localhost',user="root",password="Ling0.0",db="bus",charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

mongodbClient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = mongodbClient["MetroVSz"]
routes = mydb["routes"]
crowdData = mydb["corwdData404"]

def getSite(lineName, direction=1):
    sql = f'''
    select site_name from sites
    where new_name = '{lineName}' and direction = {direction}
    '''
    cursor.execute(sql)
    route = []
    for each in cursor.fetchall():
        site = {}
        site['site_name'] = each['site_name']
        site['averageTime'] = []
        site['records'] = []
        route.append(site)
    return route 

def getSiteList(lineName, direction=1):
    sql = f'''
    select site_name,line_name from sites
    where new_name = '{lineName}' and direction = {direction}
    '''
    cursor.execute(sql)
    res = {'direction':direction}
    line_name5 = lineName
    for i, each in enumerate(cursor.fetchall()):
        res[each['site_name']]= i
        line_name5 = each['line_name']
    
    return res, line_name5

#得到某个new_name,和direction的所有数据
def getRecord(matchPattern,new_name,direction = 1):
    sql = f'''
        select aboard_site,alight_site,
        aboard_t,alight_t,tag,trip_times
        from bus_record,404_trip 
        where line like '{matchPattern}'
        and 404_trip.routes like '%-{new_name}-{direction}-%'
        and tsfer_times = 0
        and bus_record.card_id = 404_trip.card_id 
        and bus_record.card_t = 404_trip.aboard_t
        order by tag, aboard_t;
    '''
    #-----------选择线路------------------
    chosenRoute = False
    sitesList = []
    line1,line_name1 = getSiteList(new_name,1)
    line2,line_name2 = getSiteList(new_name,2)
    curLine = ''
    curLineName = ''
    #-----------选择线路------------------
    
    cursor.execute(sql)
    data =  cursor.fetchall()
    rowNums = cursor.rowcount
    k = 1
    for each in data:
        #----------获得当前数据-------------
        aboard_site = each['aboard_site']
        alight_site = each['alight_site']
        aboard_t = dateTotimeStamp(each['aboard_t'])
        #alight_t = dateTotimeStamp(each['alight_t'])
        trip_times = each['trip_times']
        tag = each['tag']
        #----------获得当前数据-------------

        #-----------从两条线中选一条来处理------------------
        if chosenRoute == False:
            if aboard_site in line1.keys() and alight_site in line1.keys():
                #试着选line1
                startIndex = line1[aboard_site]
                endIndex = line1[alight_site]
                if startIndex - endIndex==0:
                    continue
                elif startIndex - endIndex < 0:#选line1
                    curLine = line1
                    curLineName = line_name1
                    sitesList = getSite(new_name,1)
            if curLine == '' and aboard_site in line2.keys() and alight_site in line2.keys():
                #试着选line2
                startIndex = line2[aboard_site]
                endIndex = line2[alight_site]
                if startIndex - endIndex==0:
                    continue
                elif startIndex - endIndex < 0:#选line2
                    curLine = line2
                    curLineName = line_name2
                    sitesList = getSite(new_name,2)
            if curLine == '':
                continue
            chosenRoute = True
        
        #-----------选择线路------------------
        
        if aboard_site not in curLine.keys() or alight_site not in curLine.keys():
            #print(f"舍弃第{k}条数据,共{rowNums}条-----",new_name,"----",each['aboard_site'],"   ",each['alight_site'])
            #k+=1
            continue

        #--------站点的序号-------
        start = curLine[aboard_site]
        end = curLine[alight_site]
            
        #经过的站点数
        step = end - start
        if step == 0:
            #print(f"舍弃第{k}条数据,共{rowNums}条-----",new_name,"----",each['aboard_site'],"   ",each['alight_site'])
            #k+=1
            continue
        #平均每站的时间
        siteTime = minutesToSec(trip_times)/step

        for i in range(start,end+1):
            arriveTime = aboard_t + (i - start)*siteTime
            record = {
                'bus':tag,
                'arriveTime':arriveTime,
            }
            sitesList[i]['records'].append(record)
            sitesList[i]['averageTime'].append(siteTime)
    #---------------合并拥挤度数据--------------------------#
    for i, item in enumerate(sitesList):
            if len(item['averageTime']):
                item['averageTime'] = sum(item['averageTime'])/len(item['averageTime'])

            if len(item['records']) <= 1:
                continue
            
            records = item['records']
            recordsNum = len(records)
            newRecords = []
            k = 0
            while(k < recordsNum):
                c = k + 1
                avgArriveTime = records[k]['arriveTime']
                crowdNums = 1
                while(c < recordsNum and records[c-1]['bus'] == records[c]['bus'] and abs(records[c-1]['arriveTime']-records[c]['arriveTime']) < timeDiff):
                    avgArriveTime += records[c]['arriveTime']
                    crowdNums += 1
                    c += 1

                avgArriveTime /= (c-k)
                newRecords.append({'bus':records[k]['bus'],'arriveTime':avgArriveTime,'crowdNum':crowdNums})
                k = c

            sitesList[i]['records'] = newRecords
    #---------------合并拥挤度数据--------------------------#
    return sitesList,curLineName
    '''
    for stopRecord in sitesList:
        print(stopRecord['site_name'],stopRecord['averageTime'])
        for item in stopRecord['records']:
            item['arriveTime'] = timestampToDate(item['arriveTime'])
            print(item)
        #print(dateTotimeStamp(each['aboard_t']))
    '''

def main():
    ans = []
    i = 0
    validRoutes = routes.find({'matchPattern':{'$not':{'$eq':''}}},{'_id':0,'new_name':1,'startTime':1,'endTime':1,'matchPattern':1})
    toProcess = set()
    totalNums = validRoutes.count()
    for route in validRoutes:
        if route['new_name'] not in toProcess:
            # 处理route['new_name'](两条线路的数据)
            # 所有站点的数据  getSite(route['new_name'])
            #processData(route['new_name'])
            data, line_name = getRecord(route['matchPattern'],route['new_name'],1)
            if line_name != '':
                crowdData.insert_one({
                    'line_name':line_name,
                    'new_name':route['new_name'],
                    'startTime':route['startTime'],
                    'endTime':route['endTime'],
                    'route':data
                })
                i+=1
                print(f"已处理---{line_name}，为第{i}条,共{totalNums}条。。。")
            
            data, line_name = getRecord(route['matchPattern'],route['new_name'],2)
            if line_name != '':
                crowdData.insert_one({
                    'line_name':line_name,
                    'new_name':route['new_name'],
                    'startTime':route['startTime'],
                    'endTime':route['endTime'],
                    'route':data
                })
                i+=1
                print(f"已处理---{line_name}，为第{i}条,共{totalNums}条。。。")
            toProcess.add(route['new_name'])

    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()

if __name__=='__main__':
    main()