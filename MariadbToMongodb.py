import mysql.connector
import pymongo
import datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="study24X7"
)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mdb = myclient["mydatabase"]
mycol = mdb["Study"]
mycursor = mydb.cursor()
sql = "SELECT * FROM USER WHERE FIRST_NAME = %s"
u=str(input("Enetr First name: "))
adr = (u, )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
l=["USER_ID","USER_UUID","FIRST_NAME","LAST_NAME","USER_NAME","EMAIL,PASSWORD","GENDER","MOBILE","DOB","PROFILE_PHOTO_PATH","IS_PROFILE","LANGUAGE_ID,ISACTIVE","MOBILE_VERIFIED"
,"EMAIL_VERIFIED","VERIFICATION_CODE_EMAIL","VERIFICATION_CODE_MOBILE","COVER_PHOTO_PATH","FACEBOOK_ID,GOOGLE_ID","RFC,ADD_DATE_TIME","UPDATE_DATE_TIME"]
y=[]
for x in myresult:
    f=list(x)
    for n, i in enumerate(f):
        if (type(i) is datetime.datetime or datetime.date or None):
            f[n] = str(i)
    def countList(l, f):
        return [item for pair in zip(l, f + [0])
                for item in pair]
    a = (countList(l, f))
    y.append(a)
op = [item for elem in y for item in elem]
def Convert(a):
    it = iter(op)
    res_dct = dict(zip(it, it))
    return res_dct


data = (Convert(op))
x = mycol.insert_one(data)
print(x)

