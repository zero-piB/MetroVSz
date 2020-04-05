import pymysql
conn = pymysql.connect(host='localhost',user="root",password="Ling0.0",db="bus",charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
def check(lineName):
    validName = lineName+'%'
    sql = f"""
    select count(distinct line) as nums from bus_record
    where line like '{validName}'
    """
    cursor.execute(sql)
    nums = cursor.fetchall()[0]['nums']
    if nums != 1:
        validName = lineName+'_'
        sql = f"""
        select count(distinct line) as nums from bus_record
        where line like '{validName}'
        """
        cursor.execute(sql)
        nums = cursor.fetchall()[0]['nums']

    if nums != 1:
        validName = lineName+'路'
        sql = f"""
        select count(distinct line) as nums from bus_record
        where line like '{validName}'
        """
        cursor.execute(sql)
        nums = cursor.fetchall()[0]['nums']

    if nums != 1:
        validName = lineName+'路'
        sql = f"""
        select count(distinct line) as nums from bus_record
        where line like '{validName}'
        """
        cursor.execute(sql)
        nums = cursor.fetchall()[0]['nums']

    if nums != 1:
        validName = lineName
        sql = f"""
        select count(distinct line) as nums from bus_record
        where line like '{validName}'
        """
        cursor.execute(sql)
        nums = cursor.fetchall()[0]['nums']
        
    if nums != 1:
        return False

    return True,validName