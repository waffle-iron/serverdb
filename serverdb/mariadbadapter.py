import PyMySQL as mariadb

def exsist(curdb):


def parseout(que):
    try:
        a = "()',"
	for char in a:
            que = str(que).replace(char," ")
        que = que.split()
        return que

class dbm(object):
    self.username = username
    self.password = password
    self.curdb = curdb
    def __init__(self, username, password,curdb):
        try:
            db = mariadb.connect(host, username, password, curdb)
            if db.is_connected():
                print("Connected!")
                cursor = db.cursor()
            else:
                return False
        except Error as e:
            return e
    def input(self, que):
	
        cursor.execute(que)
    def output(self, que):
	cursor.execute(que)
	data = cursor.fetchall()
	data = data.parseout
