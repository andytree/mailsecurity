#!/bin/bash
for ((i=30;i<34;i++))
do
        curl http://www.wooyun.org/corps/page/$i|grep nofollow >> corp.txt
done
