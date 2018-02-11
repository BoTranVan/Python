try:
    import urllib2
    import threading
except BaseException as e:
    print e

try:
    threads = []
    url = "https://smartcloud.vn"
except BaseException as e:
    print e
    
def send_request(url):
    for i in range(10000):
        try:
            httpd = urllib2.urlopen(url)
##            print httpd.info()
            if i%500 == 0:
                print i
        except BaseException as e:
            print e

for i in range(10):
    t = threading.Thread(send_request(url))
    t.start()
    
