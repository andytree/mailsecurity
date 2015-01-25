#!/usr/local/bin/python
# -*- coding: utf8 -*-

import time
import dns.resolver
from multiprocessing import Pool

def q(ym):
    try:
        answers = dns.resolver.query(ym, 'MX')
        for rdata in answers:
            print rdata.exchange
    except:
        print "Error"
        print "*****************\n"
def test(a):
    if a==2:
        time.sleep(10)
    return a

p=Pool(processes=100)
for a in range(0,100):
    r=p.apply_async(test,[a])
    print r.get()
