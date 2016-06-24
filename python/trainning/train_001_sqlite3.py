#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'baidw'

import sqlite3 as dbapi

con = dbapi.connect("sqllit3_mydb", timeout=10)
cur = con.cursor()


# create table
print '--begin create table--'
try:
    cur.execute("create table region(region_name TEXT,region_code INTEGER)")
except Exception, ex:
    print ex
print '--end create table--'
# select table
print '--select table--'
cur.execute('select * from region')
print cur.fetchall()
print '--end select table--'
# insert data
print 'insert table'
region_name = "cf"
region_code = 4716
try:
	#insert data
    cur.execute('insert into region(region_name,region_code) values(?,?)',
                (region_name, region_code))
    #make sure commit
    con.commit()
except Exception, ex:
    print ex
print 'end insert table'
##delete data 
print 'delete table data'
region_name = "hhht"
region_code = 4710
try:
	#delete data
    cur.execute('delete from region where region_code=:region_code',
                {"region_code":4710})
    #make sure commit
    con.commit()
except Exception, ex:
    print ex
print 'end delete table data'

# select table
print '--select table--'
cur.execute('select * from region')
print cur.fetchall()
print '--end select table--'
