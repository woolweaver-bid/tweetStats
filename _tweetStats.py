#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Tweet it!
def tweet_it():

    from lib.commom import keysANDapi, ipstack_key, rpi, bt

    # actually make tweets
    tweets = bt(rpi, ipstack_key)

    # used to send tweets
    from threader import Threader
    
    # send tweets
    th = Threader(tweets, keysANDapi, wait=2, end_string=False)
    th.send_tweets()
    
    # print tweet id's to console
    print(th.tweet_ids_)

# Make it Happen!!
def main():

    # All the deugging happens here && parses for passed arguements
    from lib.debug import d1, s

    d = int(d1)
    if d != 0: # checks for any passed args
        s.switch(d)
    else: # if no args send it!!
        tweet_it()

# action really happens down here tho
if __name__ == '__main__':
    main()
