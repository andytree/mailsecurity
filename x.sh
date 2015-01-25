#!/bin/bash
while read oneline  
do  
  a=`nslookup -type=mx $oneline|grep "mail exchanger"|awk -F' ' '{print $6}'`
  echo $oneline
  echo $a
done < yuming.txt
