#!/usr/bin/env python
import sys
import pandas as pd
import optparse

def parseArgs():
    usage = """%prog [options] python script"""
    parser = optparse.OptionParser(usage)
    parser.add_option('-d', "--dataset", help = "parse stdin into pandas dataframe X", action = "store_true")
    parser.add_option('-e', "--execute", help = "execute python script", action = "store_true")
    parser.add_option('-s', "--sep", help = "column seperator, default to white space", default = " ")
    (opts, args) = parser.parse_args()
    return (opts, args)
    
def run():
    (opts, args) = parseArgs()

    if opts.dataset:
        X = pd.read_table(sys.stdin, sep = opts.sep)
    if opts.execute:
        exec(args[0])
            





