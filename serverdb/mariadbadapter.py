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
    if curdb not in b:
        print("Company not found!")
        return False
    else:
        return True


def parsein(que):
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
                   SET nic0make='%s', \
                   SET nic0model='%s', \
                   SET nic0macadd='%s', \
                   SET nic0sn='%s', \
                   SET nic1make='%s', \
                   SET nic1model='%s', \
                   SET nic1macadd='%s', \
                   SET nic1sn='%s', \
                   SET cdmake='%s', \
                   SET cdmodel='%s', \
                   SET cdsn='%s', \
                   SET cdid='%s', \
                   SET floppymake='%s', \
                   SET floppymodel='%s', \
                   SET floppysn='s%', \
                   SET fannum='%d', \
                   SET hdaddaptermake='%s', \
                   SET hdaddaptermodel='%s', \
                   SET hdaddaptersn='%s', \
                   SET testrun='%s', \
                   SET linuxdistro='%s', \
                   SET linuxvernum='%s', \
                   timezone varchar(20) not null default '',
timedst char(1) not null default '',
nic0ip varchar(20) not null default '',
nic0netmask varchar(20) not null default '',
nic0gw varchar(20) not null default '',
nic0dns varchar(20) not null default '',
nic1ip varchar(20) not null default '',
nic1netmask varchar(20) not null default '',
nic1gw varchar(20) not null default '',
nic1dns varchar(20) not null default '',
ups char(1) not null default '',
pstarver varchar(10) not null default '',
pstartype varchar(10) not null default '',
upgrade char(1) not null default '',
upver varchar(10) not null default '',
lastbackup date not null default '00000000',
auth varchar(30) not null default '',
checklist char(1) not null default '',
comments text null,





    def close():
        database.close()


