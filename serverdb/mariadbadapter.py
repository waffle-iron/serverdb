import pymysql as mariadb
from pymysql import Error
import logging

def dexsist(curdb):
    """checks for database exsistance"""
    try:
        logging.debug('sending sql query')
        ex = "SHOW DATABASES"
        cursor.execute(ex)
        logging.debug('fetching data')
        temp1 = cursor.fetchall()
        temp1 = parsein(temp1)
        if curdb not in temp1:
            logging.info('database not found')
            return False
        else:
            logging.debug('database found')
            return True
    except Error as e:
        logging.critical('something went wrong with the database')
        return e

def texsist(curdb, curtable):
    """checks for table exsistance"""
    ex = "USE '%s'; SHOW TABLES" % (curdb)
    cursor.execute(ex)
    temp1 = cursor.fetchall()
    temp1 = parsein(temp1)
    if curtable not in temp1:
        logging.info('table not found')
        return False
    else:
        logging.debug('table found')
        return True

def snexsist(cursn, curtable, curdb):
    """checks for already exsisting entry"""
    ex = "USE '%s'; SELECT sn FROM '%s' WHERE sn = '%s'" % (curdb, curtable, cursn)
    cursor.execute(ex)
    temp1 = cursor.fetchall()
    temp1 = parsein(temp1)
    if cursn not in temp1:
        logging.info('serial number not found')
        return False
    else:
        logging.debug('serial number found')
        return True

def parsein(que):
    """removes extraneous characters and splits into indexable tuple"""
    try:
        a = "()',"
        logging.debug('removing extraneous chars')
        for char in a:
            que = str(que).replace(char," ")
            que = que.split()
        logging.debug('parsing complete')
        return que
    except:
        logging.critical('UNABLE TO PARSE STRING!')
        return False

    def connectdb(host, username, password):
        """connects to sql instance and returns true on no errors"""
        try:
            dab = mariadb.connect(host, username, password)
            if dab.is_connected():
                cursor = dab.cursor()
                logging.debug('connected to database')
                return True
            else:
                logging.critical('Unable to connect to host')
                return False
        except OperationalError as e:
            logging.critical('UNABLE TO CONNECT TO HOST')
            return e
    def outputs(que):
    
        cursor.execute(que)
    def inputs(que):
        """takes sql query, fetches all returned info and returns tuple"""
        logging.debug('sending query')
        cursor.execute(que)
        logging.debug('fetching data')
        data = cursor.fetchall()
        data = parsein(data)
        logging.debug('returning data to parent')
        return data

    def newdb(curdb, curtable):
        """creates new company db and creates new table from template"""
        text = "CREATE DATABASE '%s' % (curdb)
        logging.debug('setting sql query for db')
        text1 = tbtemplate(curdb, curtable)
        logging.debug('setting sql for table template')
        try:
            cursor.execute(text)
            dab.commit()
            logging.info('new database created')
            return True
        except:
            logging.critical('failed to create new company database')
            dab.rollback()
            return False
        try:
            cursor.execute(text1)
            dab.commit()
            logging.info('new table created')
            return True
        except:
            logging.critical('failed to create table')
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

    def tbtemplate(curdb, curtable):
        que = "create table '%s'.'%s' \
               (\
               sn varchar(10) not null default '', \
               model varchar(10) not null default '', \
               builddate date not null default '00000000', \
               rma int unsigned not null default '0', \
               casemake varchar(30) not null default '', \
               casemodel varchar(30) not null default '', \
               mobomake varchar(30) not null default '', \
               mobomodel varchar(30) not null default '', \
               mobosn varchar(30) not null default '', \
               processormake varchar(30) not null default '', \
               processormodel varchar(30) not null default '', \
               processorsn varchar(30) not null default '', \
               processorspeed decimal(10,2) not null default '0.00', \
               memorymake varchar(30) not null default '', \
               memorytype varchar(20) not null default '', \
               memorysize int(10) not null default '0', \
               memorynum varchar(10) not null default '', \
               memorysn varchar(30) not null default '', \
               hd0make varchar(30) not null default '', \
               hd0model varchar(30) not null default '', \
               hd0sn varchar(30) not null default '', \
               hd0size int(10) not null default '0', \
               hd1make varchar(30) not null default '', \
               hd1model varchar(30) not null default '', \
               hd1sn varchar(30) not null default '', \
               hd1size int(10) not null default '0', \
               vcardmake varchar(30) not null default '', \
               vcardmodel varchar(30) not null default '', \
               vcardsn varchar(30) not null default '', \
               nic0make varchar(30) not null default '', \
               nic0model varchar(30) not null default '', \
               nic0macadd varchar(13) not null default '', \
               nic0sn varchar(30) not null default '', \
               nic1make varchar(30) not null default '', \
               nic1model varchar(30) not null default '', \
               nic1macadd varchar(13) not null default '', \
               nic1sn varchar(30) not null default '', \
               cdmake varchar(30) not null default '', \
               cdmodel varchar(30) not null default '', \
               cdsn varchar(30) not null default '', \
               cdid varchar(30) not null default '', \
               floppymake varchar(30) not null default '', \
               floppymodel varchar(30) not null default '', \
               floppysn varchar(30) not null default '', \
               fannum int unsigned not null default '0', \
               hdaddaptermake varchar(30) not null default '', \
               hdaddaptermodel varchar(30) not null default '', \
               hdaddaptersn varchar(30) not null default '', \
               testrun char(1) not null default '', \
               linuxdistro varchar(20) not null default '', \
               linuxvernum varchar(10) not null default '', \
               timezone varchar(20) not null default '', \
               timedst char(1) not null default '', \
               nic0ip varchar(20) not null default '', \
               nic0netmask varchar(20) not null default '', \
               nic0gw varchar(20) not null default '', \
               nic0dns varchar(20) not null default '', \
               nic1ip varchar(20) not null default '', \
               nic1netmask varchar(20) not null default '', \
               nic1gw varchar(20) not null default '', \
               nic1dns varchar(20) not null default '', \
               ups char(1) not null default '', \
               pstarver varchar(10) not null default '', \
               pstartype varchar(10) not null default '', \
               upgrade char(1) not null default '', \
               upver varchar(10) not null default '', \
               lastbackup date not null default '00000000', \
               auth varchar(30) not null default '', \
               checklist char(1) not null default '', \
               comments text null, \
               primary key (sn) \
               );" % (curdb, curtable)
        return template




    def close():
        """close connection to database"""
        dab.close()


