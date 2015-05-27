import datetime, time

while 1:
    print "ZCZC-EAS-DMO-024005+0015+{0}-KC2AEI-".format(
        datetime.datetime.utcnow().strftime("%j%H%M")
        )
    time.sleep(60)

