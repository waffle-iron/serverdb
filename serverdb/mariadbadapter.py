import pymysql as mariadb
from pymysql import Error

def dexsist(curdb):
    """checks for database exsistance"""
    ex = "SHOW DATABASES"
    cursor.execute(ex)
    temp1 = cursor.fetchall()
    temp1 = parsein(temp1)
    if curdb not in temp1:
        return False
    else:
        return True

def texsist(curdb, curtable):
    """checks for table exsistance"""
    ex = "USE '%s'; SHOW TABLES" % (curdb)
    cursor.execute(ex)
    temp1 = cursor.fetchall()
    temp1 = parsein(temp1)
    if curtable not in temp1:
        return False
    else:
        return True

def snexsist(cursn, curtable, curdb):
    """checks for already exsisting entry"""
    ex = "USE '%s'; SELECT sn FROM '%s' WHERE sn = '%s'" % (curdb, curtable, cursn)
    cursor.execute(ex)
    temp1 = cursor.fetchall()
    temp1 = parsein(temp1)
    if curtable not in temp1:
        return False
    else:
        return True

def parsein(que):
    """removes extraneous characters and splits into indexable tuple"""
    a = "()',"
    for char in a:
        que = str(que).replace(char," ")
        que = que.split()
        return que

    def connectdb(host, username, password):
        """connects to sql instance and returns true on no errors"""
        try:
            dab = mariadb.connect(host, username, password)
            if dab.is_connected():
                cursor = dab.cursor()
                return True
            else:
                return False
        except Error as e:
            return e
    def outputs(que):
    
        cursor.execute(que)
    def inputs(que):
        """takes sql query, fetches all returned info and returns tuple"""
        cursor.execute(que)
        data = cursor.fetchall()
        data = parsein(data)
        return data

    def newdb(curdb, curtable):
        """creates new company db and creates new table from template"""
        text = "CREATE DATABASE '%s'; \
                CREATE TABLE '%s'; \
                INSERT INTO '%s' SELECT * FROM template.mach_template" % (curdb, curtable, curtable)
         try:
            cursor.execute(text)
            dab.commit()
            return True
        except:
            dab.rollback()
            return False        

    def updates(que):
        """turns list into sql query and commits to db"""
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
                             WHERE sn='%s'" % (que)
        try:
            cursor.execute(updateque)
            dab.commit()
            return True
        except:
            dab.rollback()
            return False




    def close():
        """close connection to database"""
        dab.close()


