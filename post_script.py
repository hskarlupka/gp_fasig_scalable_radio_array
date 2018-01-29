#!/usr/bin/env python
import os
import sys
from optparse import OptionParser
from subprocess import check_output, STDOUT
from time import sleep

usage = "usage: %prog [options] OUTDIR JOB"
parser = OptionParser(usage)

(options, args) = parser.parse_args()

outdir = args[0]
job = args[1]

cmd = ['globus-url-copy', '-list', 'gsiftp://gridftp.icecube.wisc.edu/{}/'.format(outdir)]
for i in range(1, 5):
    try:
        output = check_output(cmd, shell=False, env=os.environ, stderr=STDOUT)
        for line in output.split('\n'):
            if job in line:
                sys.exit(0)
        sys.exit(1)
    except Exception as e:
        print e
        sleep(30)
