#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.commom import k_a, rpia, ipstack_key, rpi, phs, cips, bt

# from lib.pihole_info import combinator as pi # where pihole information is gathered
from lib.sys_info import sys_info as si # where system information is gathered
from lib.speed_test import speedtest_ip as sip # where speedtest information is gather
# from lib.pihole_info import reach_pihole as rp # test pihole reachability
from lib.get_api import get_keysANDapi as gka # where we interact with the Twitter API
# from lib.speed_test import check_ipstack as cip # check ipstack key
# from lib.get_config  import get_cfg as cfg # twitter keys
# import lib.construct_tweet as ct # where the tweet is put together
# from lib.construct_tweet import build_tweets as bt
from emoji import UNICODE_EMOJI # where we get our emoji dictionary from
from argparse import ArgumentParser # how we parse command line arguments when/if they are passed

# parse command line arguments, IF any are passed
parser = ArgumentParser()
parser.add_argument('-dbl', dest='dbl', type=int, nargs='?', default=0, const=11, help='test twitter login')
parser.add_argument('-dbp', dest='dbp', type=int, nargs='?', default=0, const=12, help='test pi-hole api reachability')
parser.add_argument('-dbs', dest='dbs', type=int, nargs='?', default=0, const=13, help='test ipstack.com key')
parser.add_argument('-dbt', dest='dbt', type=int, nargs='?', default=0, const=14, help='test tweet creation')
parser.add_argument('-dbv', dest='dbv', type=int, nargs='?', default=0, const=15, help='test ability to get all variables needed for tweet')

args = parser.parse_args()

dbp = args.dbl
dbl = args.dbp
dbs = args.dbs
dbt = args.dbt
dbv = args.dbv

d1 = dbl + dbp + dbs + dbt + dbv # add our args together for better handling of each case

def variable_check():

    # print all variables and test logins/reachability
    print("\nTwitter Keys")
    print(k_a)

    print("\nCheck Twitter Login")
    gka(k_a)

    print("\nPihole Address")
    print(rpia)

    print("\nPiHole Reachability")
    print(rpi[2], rpi[3])

    print("\nIPstack.com Key")
    print(ipstack_key)

    print("\nIPstack.com Reachability")
    print(cips)

    print("\nPihole Stats")
    print(phs)

    print("\nSystem Stats")
    s = si()
    print(s)

    print("\nNetwork Stats")
    t = sip(ipstack_key)
    print(t)

class debugSwitch:

    # Where the switching happens
    def switch(self, dbm):
        # Print number used to determine debug output for debug help
        print("Debug Variable = " + str(d1) + "\ntweetStats.py -h for more info")
        return getattr(self, 'case_' + str(dbm), lambda: parser.print_help())()

    def case_11(self): # -dbl (test twitter login)
        gka(k_a)
        return
    def case_12(self): # -dbp (test pihole reachability)
        print(rpi)
        return
    def case_13(self): # -dbs (test test ipstack.com key)
        print(cips)
        return
    def case_14(self): # -dbt (test tweet creation)
        b = bt(rpi, ipstack_key)
        print ('\nTweet made successfully.\n')
        print (b[0] + "\n\n" + b[1] + "\n\n" + b[2])
        return
    def case_15(self): # -dbv (print all variables needed to create tweet)
        variable_check()
        return

s = debugSwitch()