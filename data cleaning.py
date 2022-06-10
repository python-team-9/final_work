import pymysql
import pandas
import os
from sqlalchemy import create_engine
db = pymysql.connect(host="47.99.201.114", user="root", passwd="Aa123456", db="jobOfferinformation", port=3306,charset="utf8",)
#db = pymysql.connect(host="localhost", user="root", passwd="", db="jobOfferinformation", port=3306,charset="utf8")
sql = 'SELECT distinct jobName,jobCompany,jobSalary,jobPlace,jobDescribe,jobNumber,jobEducation,jobExperience FROM jobOfferinformation.jobOfferDetail;'
df = pandas.read_sql(sql, con=db)
df['jobEducation'] = df['jobEducation'].replace('','不限')
engine = create_engine("mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', 'Aa123456', '47.99.201.114:3306', 'jobOfferinformation','utf8'))
#engine = create_engine("mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', '', 'localhost:3306', 'jobOfferinformation','utf8'))
cursor = db.cursor()
clean = "truncate table jobOfferDetail"
cursor.execute(clean)
df.to_sql(name='jobOfferDetail', con=engine, if_exists='append', index=False)