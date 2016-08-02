#-*- coding:utf-8 -*-
import sqlite3 as dbapi

def get_db_conn(db_file_path):
    con=dbapi.connect(db_file_path)
    #print 'Opened database sucessfully.'
    return con

def execute_sql(con,db_sql_str):
    try:
        cursor=con.execute(db_sql_str)
    except Exception,e:
        print 'Excute database sql failed.\nException:',str(e)
        print 'SQL: %s '%(db_sql_str)
        return None
    print 'SQL: %s '%(db_sql_str)
    # if db_sql_str[0]=='C':
    #     print 'CREATE TABLE SUCESSFULLY.'
    # elif db_sql_str[0]=='I':
    #     con.commit()
    #     print 'INSERT TABLE SUCESSFULLY.'
    # elif db_sql_str[0]=='U':
    #     con.commit()
    #     print "Total number of rows updated :", con.total_changes
    #     print 'UPDATE TABLE SUCESSFULLY.'
    # elif db_sql_str[0]=='D':
    #     con.commit()
    #     print "Total number of rows deleted :", con.total_changes
    #     print 'DELETE TABLE SUCESSFULLY.'
    # elif db_sql_str[0]=='S':
    #     print 'SELECT TABLE SUCESSFULLY.'
    # else:
    #     print 'UNKOWN SQL:'+db_sql_str
    return cursor

if __name__ == '__main__':
    DB_SQL_TYPE=['CREATE','INSERT','UPDATE','SELECT','DELETE'];
    db_con_str="sqlite_db.db"
    # db_sql_str='''CREATE TABLE COMPANY
    #       (ID INT PRIMARY KEY     NOT NULL,
    #       NAME           TEXT    NOT NULL,
    #       AGE            INT     NOT NULL,
    #       ADDRESS        CHAR(50),
    #       SALARY         REAL);'''
    db_sql_str="SELECT * from COMPANY "
    # db_sql_str='''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #      VALUES (1, 'Mark1', 20, 'Mond ', 60000.00 )'''
    #db_sql_str="UPDATE COMPANY set SALARY = 25000.00 where ID=1"
    con=get_db_conn(db_con_str)
    cursor=execute_sql(con,db_sql_str)
    #print type(cursor)
    if cursor==None:
        print 'EXECUTE SQL AND RETURN NONE RESULT.'
    else:
        res = cursor.fetchall()
        print '总记录数:',len(res)
        #print res
        c=1
        for r in res:
            print '记录 '+str(c)+':',
            for k in r:
                print k,
            print '\n',
            c+=1
    con.close()




    