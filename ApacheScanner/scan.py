#!/usr/bin/python
"""
 apacheScan

"""
import sys
import os

class bcolors:
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    NEUTRAL = '\033[94m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def checkVulns(banner, filename):
    vulns = []
    start = False
    f = open(filename, 'r')
    for line in f.readlines():
        if start == True:
            if line != "\n":
                vulns.append(line)
            if not line.startswith('\t'):
                start = False
                break
        if line.strip("\n") == banner:
            start = True

    if (len(vulns) != 0):
        varVuln = 'vulnerabilities!'
        if (len(vulns) == 1):
            varVuln = 'vulnerability!'
        print(bcolors.SUCCESS + bcolors.BOLD + '\n[+]' + bcolors.ENDC + ' Found' + bcolors.FAIL + bcolors.BOLD, len(vulns), bcolors.ENDC + varVuln)
        print(bcolors.SUCCESS + bcolors.BOLD + '\n[+]' + bcolors.ENDC + ' Apache ' + bcolors.NEUTRAL + bcolors.BOLD + banner + bcolors.ENDC + ' is vulnerable to the following:')
        print(bcolors.FAIL + "".join(vulns))
    else:
        print(bcolors.FAIL + bcolors.BOLD + '\n[-]' + bcolors.ENDC + ' I am sorry but we could\'t find any vulnerabilities in our database for ' + bcolors.NEUTRAL + bcolors.BOLD + 'Apache ' + banner + bcolors.ENDC + '.')

def main():
    if len(sys.argv) == 2:
        version = sys.argv[1]
        filename = 'apache_CVE.txt'
        print('Filename: = ' + filename)
        print('Apache Version = ' + version)
        if not os.path.isfile(filename):
            print('[-] ' + filename + ' does not exist.')
            exit(0)
        if not os.access(filename, os.R_OK):
            print('[-] ' + filename + ' access denied.')
            exit(0)
        checkVulns(version, filename)
    else:
        print('\nUsage:')
        print('\tpython scan.py [Apache version]')
        print('\nExample:')
        print('\tpython scan.py 2.0.29\n')

if __name__ == '__main__':
    main()