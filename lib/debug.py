#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.pihole_info import pihole_info as pi # where pihole information is gathered
from lib.sys_info import sys_info as si # where system information is gathered
from lib.speed_test import speedtest_ip as sip # where speedtest information is gather

from lib.pihole_info import reach_pihole as rp # test pihole reachability
from lib.get_api import get_api as ga # where we interact with the Twitter API

from lib.get_config  import get_cfgt as cfgt # twitter keys
from lib.get_config  import get_cfgp as cfgp # pi-hole address

import lib.construct_tweet as ct # where the tweet is put together

from emoji import UNICODE_EMOJI # where we get our emoji dictionary from
from argparse import ArgumentParser # how we parse command line when/if they are passed

# parse command line arguements, IF any are passed
parser = ArgumentParser()
parser.add_argument('-db', dest='db', type=int, nargs='?', default=0, const=10, help='Will print all variables to console including a contructed tweet')
parser.add_argument('-dbl', dest='dbl', type=int, nargs='?', default=0, const=11, help='test twitter login')
parser.add_argument('-dbp', dest='dbp', type=int, nargs='?', default=0, const=12, help='test pi-hole api reachability')
parser.add_argument('-dbt', dest='dbt', type=int, nargs='?', default=0, const=13, help='test tweet ceation')
parser.add_argument('-dbv', dest='dbp', type=int, nargs='?', default=0, const=14, help='test ability to get a variables needed for tweet')

args = parser.parse_args()

db = args.db
dbp = args.dbp
dbl = args.dbl
dbt = args.dbt
dbv = args.dbv

d1 = db + dbl + dbp + dbt + dbv # add our args together for better handling of each case

class debugSwitch:

    # Print number used to determine debug output
    print("Debug Variable = " + str(d1) + "\ntweetStats.py -h for more info")

    # Where the switching happens
    def switch(self, dbm):
        return getattr(self, 'case_' + str(dbm), lambda: parser.print_help())()
    def case_10(self): # -db (print all variables and test tweet creation)
        debug_tweet()
        return
    def case_11(self): # -dbl (test twitter login)
        ga()
        return
    def case_12(self): # -dbp (test pihole reachability)
        print(rp()[1])
        return
    def case_13(self): # -dbt (test tweet creation)
        tweet_creation()
        return
    def case_14(self): # -dbv (print all variables needed to create tweet)
        variable_check()
        return

s = debugSwitch()

def variable_check():

    # print all variables and test logins/reachability
    print('\nTwitter Keys')
    print(cfgt())

    print("\nCheck Twitter Login")
    ga()

    print('\nPihole Address')
    print(cfgp())

    print("\nPiHole Status")
    print(rp()[1])

    print('\nPihole Stats')
    print(pi())

    print('\nSystem Stats')
    print(si())

    print('\nSpeedTest Info')
    print(sip())


def tweet_creation():

    print('\nThe tweets that where created.')
    # build tweet
    PHtweet = ct.PHtweet(pi())
    SYtweet = ct.SYtweet(si())
    NETtweet =  ct.NETtweet(sip())
    tweet = '\n\n Tweet 1\n' + PHtweet + '\n\n Tweet 2\n' + SYtweet + '\n\n Tweet 3\n' + NETtweet + '\n'
    print(tweet)

    print('\nNumber of characters in tweet +/- 1 or 2') # will try and nail this down to a more accurate number
    num_emoji = (sum(tweet.count(emoji) for emoji in UNICODE_EMOJI)) # accurately count and track emoji
    ignored_chars = UNICODE_EMOJI.copy() # thanks to https://stackoverflow.com/q/56214183/11456464

    PHnum_other = sum(0 if char in ignored_chars else 1 for char in PHtweet)
    totalS = (num_emoji * 2 + PHnum_other)
    print(str(num_emoji) + '(<- individual emjoi * 2) + ' + str(PHnum_other) + '(<- # of characters that aren\'t emoji\'s) = ' +  str(totalS))

    SYnum_other = sum(0 if char in ignored_chars else 1 for char in SYtweet)
    totalS = (num_emoji * 2 + SYnum_other)
    print(str(num_emoji) + '(<- individual emjoi * 2) + ' + str(SYnum_other) + '(<- # of characters that aren\'t emoji\'s) = ' +  str(totalS))

    Netnum_other = sum(0 if char in ignored_chars else 1 for char in NETtweet)
    totalS = (num_emoji * 2 + Netnum_other)
    print(str(num_emoji) + '(<- individual emjoi * 2) + ' + str(Netnum_other) + '(<- # of characters that aren\'t emoji\'s) = ' +  str(totalS))
    return