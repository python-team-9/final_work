import pymysql
db = pymysql.connect(host="47.99.201.114", user="root", passwd="Aa123456", db="jobOfferinformation", port=3306,charset="utf8",)
cursor = db.cursor()
sql = 'delete from  a using jobOfferDetail  as a where a.jobOfferid not in (select * from (select max(jobOfferid) from jobOfferDetail group  by jobDescribe ) a)'
cursor.execute(sql)
db.close()