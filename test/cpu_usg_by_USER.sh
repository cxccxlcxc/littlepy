#!/bin/bash
ps -aux | tr -s " " | awk '{print $1,$3}' | py -de 'print X.groupby("USER")["%CPU"].sum()'
