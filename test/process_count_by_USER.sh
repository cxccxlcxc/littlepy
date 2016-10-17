#!/bin/bash
ps -aux | tr -s " " | awk '{print $1,$2}' | py -d 'print X.groupby("USER").count()'
