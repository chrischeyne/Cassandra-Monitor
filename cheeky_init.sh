#!/usr/bin/env bash

# just a little script to get me editing quickly

HD=/opt/cassandra-dev/PROJECTS/Cassandra-Monitor

pip freeze > $HD/pip_freeze.txt
echo `date` >> $HD/date.txt

gst
gca
gp

SD=${HD}/src
vim -p $SD/src/base.py $SD/src/mytornado/ $SD/src/mytornado/core*.py \
$SD/src/djangotornado.py 
