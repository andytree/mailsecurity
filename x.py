#!/usr/local/bin/python
# -*- coding: utf8 -*-

import time
import dns.resolver
from multiprocessing import Process
import os

OK=[]
ERROR=[]
WHITE=["GOOGLEMAIL.COM","GOOGLE.COM","googlemail.com","qq.com","google.com","163.com","126.com"]
def white(s):
    for w in WHITE:
	if w in s:
		return False
    return True
def q(ym):
    try:
	if ym.startswith("www."):
		ym=ym.split("www.")[1]
        if ym.count(".")>1:
		#get the domain
		ym=ym.split(".")[-2]+"."+ym.split(".")[-1]
	tmp=dns.resolver
	tmp.timeout=1
        answers = tmp.query(ym, 'MX')
        for rdata in answers:
	    if white(str(rdata.exchange)):
		    #print "xxxx"
		    cmd="echo "+str(rdata.exchange)+" >> mail.txt"
		    #print cmd
		    os.system(cmd)
		    print rdata.exchange
		    OK.append(str(rdata.exchange))
    except Exception,e:
	print e
	ERROR.append(ym)

PATH = r"yuming.txt"
fp = open(PATH, "r")
x=[]
start=time.time()
for eachline in fp:
    #p=Process(target=q,args=(eachline.strip(),))
    #p.start()
    #x.append(p)
    q(eachline.strip())
#for i in range(len(x)):
#    x[i].join()
print OK
print ERROR
end=time.time()
print end-start
