#! /usr/bin/python

# a friendly caterpillar says hi (and other things). in a terminal, run as
#   python friendly-caterpillar.py
# or, if this file has executable permission,
#   ./friendly-caterpillar.py
# exit by typing control-c.

import sys, time, random, signal

def scoot_back(n):
    sys.stdout.write('{:c}{:c}{:c}'.format(8, 32, 8) * n)

# the friendly caterpillar says:
def get_message():
    msgs = ['hi!','nom nom nom...dee-licious!','meep meep','hello!',
            'what a pretty autumn day!','streeeetch','*achoo*','good job!',
            'hmmm, what shall i have for lunch?',
            'i shall hop on my bi-cy-clee and be a speedy caterpillar!',
            'type control-c and i will go do my grocery shopping']
    return msgs[random.randint(0,len(msgs)-1)]

def bye(a,b):
    sys.stdout.write(' bye!')
    sys.stdout.flush()
    time.sleep(0.5)
    scoot_back(80)
    sys.exit(0)
signal.signal(signal.SIGINT, bye)

cs = '/\\'
tu = 0.3
wlen = 12
while True:
    for j in xrange(wlen):
        scoot_back(2)
        sys.stdout.write('{:s}8{:s}'.format(cs[j % len(cs)],
                                            'D' if j == wlen-1 else ')'))
        sys.stdout.flush()
        time.sleep(tu)
    time.sleep(0.5*tu)
    msg = get_message()
    sys.stdout.write(' ' + msg)
    sys.stdout.flush()
    time.sleep(4*tu*max(1,(len(msg)//15)))
    scoot_back(len(msg))
    for j in xrange(wlen+1):
        scoot_back(3)
        sys.stdout.write('8)'.format(cs[j % len(cs)]))
        sys.stdout.flush()
        time.sleep(tu)
