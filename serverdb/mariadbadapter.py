import pymysql as mariadb
from pymysql import Error

def exsist(curdb):
    ex = "SHOW DATABASES"
    cursor.execute(ex)
    a = "()',"
    b = cursor.fetchall()
    for char in a:
        b = str(b).replace(char," ")
    b = b.split()
    if (database == False):
        print("Company not found!")
        return False
    else:
        return True


def parsein(que):
    try:
        a = "()',"
    for char in a:
            que = str(que).replace(char," ")
        que = que.split()
        return que

    def connectdb(host, username, password, curdb):
        try:
            db = mariadb.connect(host, username, password)
            if db.is_connected():
                print("Connected!")
                cursor = db.cursor()
            else:
                return False
        except Error as e:
            return e
    def outputs(self, que):
    
        cursor.execute(que)
    def inputs(self, que):
    cursor.execute(que)
    data = cursor.fetchall()
    data = parsein(data)

    def updates(self,que):
        updateque="UPDATE %s (SET sn='%s', \
                   SET model='%s', \
                   SET builddate='%d', \
                   SET rma='%d', \
                   SET casemake='%s', \
                   SET casemodel='%s', \
                   SET mobomake='%s', \
                   SET mobomodel='%s', \
                   SET mobosn='%s', \
                   SET processormake='%s', \
                   SET processormodel='%s', \
                   SET processorsn='%s', \
                   SET processorspeed='%d', \
                   SET memorymake='%s', \
                   SET memorytype='%s', \
                   SET memorysize='%d', \
                   SET memorynum='%s', \
                   SET memorysn='%s', \
                   SET hd0make='%s', \
                   SET hd0model='%s', \
                   SET hd0sn='%s', \
                   SET hd0size='%d', \
                   SET hd1make='%s', \
                   SET hd1model='%s', \
                   SET hd1sn='%s', \
                   SET hd1size='%d', \
                   SET vcardmake='%s', \
                   SET vcardmodel='%s', \
                   SET vcardsn='%s', \
                   SET 





    def close():
        database.close()


