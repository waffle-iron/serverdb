import pymysql as mariadb
from pymysql import Error

def dexsist(curdb):
    ex = "SHOW DATABASES"
    cursor.execute(ex)
    b = cursor.fetchall()
    c = parsein(b)
    if curdb not in c:
        return False
    else:
        return True

def texsist(curtable):
    ex = "SHOW TABLES"
    cursor.execute(ex)
    b = cursor.fetchall()
    c = parsein(b)
    if curtable not in c:
        return False
    else:
        return True


def parsein(que):
    a = "()',"
    for char in a:
        que = str(que).replace(char," ")
        que = que.split()
        return que

    def connectdb(host, username, password):
        try:
            db = mariadb.connect(host, username, password)
            if db.is_connected():
                cursor = db.cursor()
                return True
            else:
                return False
        except Error as e:
            return e
    def outputs(que):
    
        cursor.execute(que)
    def inputs(que):
        cursor.execute(que)
        data = cursor.fetchall()
        data = parsein(data)
        return data
    

    def updates(self,que):
        updateque="UPDATE %s SET sn='%s', \
                                 model='%s', \
                                 builddate='%d', \
                                 rma='%d', \
                                 casemake='%s', \
                                 casemodel='%s', \
                                 mobomake='%s', \
                                 mobomodel='%s', \
                                 mobosn='%s', \
                                 processormake='%s', \
                                 processormodel='%s', \
                                 processorsn='%s', \
                                 processorspeed='%d', \
                                 memorymake='%s', \
                                 memorytype='%s', \
                                 memorysize='%d', \
                                 memorynum='%s', \
                                 memorysn='%s', \
                                 hd0make='%s', \
                                 hd0model='%s', \
                                 hd0sn='%s', \
                                 hd0size='%d', \
                                 hd1make='%s', \
                                 hd1model='%s', \
                                 hd1sn='%s', \
                                 hd1size='%d', \
                                 vcardmake='%s', \
                                 vcardmodel='%s', \
                                 vcardsn='%s', \
                                 nic0make='%s', \
                                 nic0model='%s', \
                                 nic0macadd='%s', \
                                 nic0sn='%s', \
                                 nic1make='%s', \
                                 nic1model='%s', \
                                 nic1macadd='%s', \
                                 nic1sn='%s', \
                                 cdmake='%s', \
                                 cdmodel='%s', \
                                 cdsn='%s', \
                                 cdid='%s', \
                                 floppymake='%s', \
                                 floppymodel='%s', \
                                 floppysn='s%', \
                                 fannum='%d', \
                                 hdaddaptermake='%s', \
                                 hdaddaptermodel='%s', \
                                 hdaddaptersn='%s', \
                                 testrun='%s', \
                                 linuxdistro='%s', \
                                 linuxvernum='%s', \
                                 timezone='%s', \
                                 timedst='%s', \
                                 nic0ip='%s', \
                                 nic0netmas k='%s', \
                                 nic0gw='%s', \
                                 nic0dns='%s', \
                                 nic1ip='%s', \
                                 nic1netmask='%s', \
                                 nic1gw='%s', \
                                 nic1dns='%s', \
                                 ups='%s', \
                                 pstarver='%s', \
                                 pstartype='%s', \
                                 upgrade='%s', \
                                 upver='%s', \
                                 lastbackup='%d', \
                                 auth='%s', \
                                 checklist='%s', \
                                 comments='%s', \
                             WHERE sn='%s'"
        try:
            cursor.execute(updateque)
            db.commit()
            return True
        except:
            db.rollback()
            return False




    def close():
        database.close()


