import sys
import os

if sys.argv[1] == 'rakesh':
    print 'correct'
    os.system('exit 0')
else:
    print sys.argv[1]
    print 'not correct'
    os.system('exit 1')