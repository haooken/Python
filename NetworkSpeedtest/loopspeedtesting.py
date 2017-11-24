import speedtest
import time

s = speedtest.Speedtest()
s.get_best_server()

for i in range(50):
    print "Run speed test - " + str(i)
    result = "" + str(s.download()) + "," + str(s.upload())
    print "Save Values: " + result
    f = open('log.csv', 'a')
    f.write(result + '\n')
    f.close()
    print "Sleeping for 1 min..."
    time.sleep(60)
    