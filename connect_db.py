from mysql import connector
import threading


def insertData():
	for i in range(100):
		try:
		    connect = connector.connect(host="172.16.69.254", user="root", password="tranbo9x", database="test")
		    cur = connect.cursor()
		    str_command = ('insert into hixx(data) values(9)')
		    cur.execute(str_command)
		    connect.commit()
		    cur.close();
		    connect.close()
		    print "Added"
		except Exception as e:
		    print "Error: ", e

threads = []
attemp = 1

for i in range (10):
        t = threading.Thread(target=insertData)
        threads.append(t)
        t.start()
