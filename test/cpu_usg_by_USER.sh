#!/bin/bash
ps -aux | tr -s " " | awk '{print $1,$3}' | py -d 'print X.groupby("USER")["%CPU"].sum()'
