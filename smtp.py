import os, sys, string
import smtplib
import traceback
from multiprocessing import Process,Queue
FOUND=Queue()
WHITE=["auth","error","bad","deny","denied","rejected"]
def white(s):
	for w in WHITE:
		if w in s:
			return False
	return True

def go(mailserver):
	try:
		yuming=mailserver[len(mailserver.split(".")[0])+1:]
		print yuming
		from_addr="hr@"+yuming
		to_addr="hr@"+yuming
		msg="test"
		svr=smtplib.SMTP(mailserver,timeout=10)
		#svr.set_debuglevel(1)
		svr.docmd("HELO localhost")
		x=svr.docmd("mail from:%s"%from_addr)
		if white(x[1].lower()):
			y=svr.docmd("rcpt to:%s"%to_addr)
			if white(y[1].lower()):
				print "-------------"
				print mailserver
				global FOUND
				FOUND.put(mailserver)
			#svr.docmd("data")
			#svr.send(msg+"\r\n")
			#svr.send(".\r\n")
			#print svr.getreply()
			svr.quit()
	except Exception,e:
		traceback.print_exc()
x=[]
for m in open("mail.txt").readlines():
	p=Process(target=go,args=[m.strip().rstrip(".")])
        p.start()
        x.append(p)
for i in range(len(x)):
	x[i].join()
while FOUND.empty()==False:
	print FOUND.get()
