try:
    import requests
except BaseException as e:
    print e
    

url = "http://nginx.flatbase.com"
rq01, rq02, rq03 = 0, 0, 0

for i in range(20):
    try:
        httpd = requests.get(url, stream=True)
        sock = httpd.raw._fp.fp._sock.getpeername()
        if (sock):
            print "Send request to: ", sock
            result = httpd.text.split("Welcome to nginx on ")[1].split("!</h1>\n<p>")[0]
            print "Request ", i+1, " to host:", result
            if result == "db01":
                rq01 += 1
            elif result== "db02":
                rq02 += 1
            elif result == "db03":
                rq03 += 1
    except BaseException as e:
        print e
    
print "Request db01: ", rq01
print "Request db02: ", rq02
print "Request db03: ", rq03
