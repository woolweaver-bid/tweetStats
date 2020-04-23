#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Build the tweet
def PHtweet(ph):

    # First Tweet
    PHtweet = 'Pi-Hole Stats'
    PHtweet += '\nQueries:' # query stats
    PHtweet += '\n  Block\'d: ' + ph[0]
    PHtweet += '\n  Fwd\'d: ' + ph[1]
    PHtweet += '\n  Cached: ' + ph[2]
    PHtweet += '\n  Total: ' + ph[3] 
    PHtweet += '\nClients:' 
    PHtweet += '\n  ns1|ns2: ' + ph[4]
    PHtweet += '\nPrivacy Level:' # privacy level
    PHtweet += '\n  ns1|ns2: ' + ph[5]
    PHtweet += '\nAdlists Last Updated & Count:' # gravity last updated (your local time)
    PHtweet += '\n  ns1: ' + ph[6]
    PHtweet += '\n  ns2: ' + ph[7]

    return (PHtweet)

def SYtweet(sy):

    # Second Tweet
    SYtweet = 'System Stats'
    SYtweet += '\nCPU Load AVG: ' + sy[0] # CPU load average
    SYtweet += '\nRam Usage: ' + sy[1] # RAM usage
    SYtweet += '\nDisk Usage: ' + sy[2] # disk usage information
    SYtweet += '\nNetwork Interfaces: ' + sy[3] # network interface names (no loopback)
    SYtweet += '\nKernel && OS: ' + sy[4] # kernel && OS information
    SYtweet += '\nBoot Time: ' + sy[5] # time when system booted (your local time)

    return (SYtweet)

def NETtweet(stp):

    # Third Tweet
    Nettweet = 'Network Stats'
    Nettweet += '\nPing: ' + stp[0] # Ping via speedtest-cli
    Nettweet += '\nSpeed Achieved (ul/dl): ' + stp[1] # Speed (dl/ul) via speedtest-cli
    Nettweet += '\nData Used (ul/dl): ' + stp[2] # Data used (dl/ul) via speedtest-cli
    Nettweet += '\nIP: ' + stp[3] # IP address from speedtest-cli
    Nettweet += '\nISP: ' + stp[4] # ISP from speedtest-cli
    Nettweet += '\nRegion: ' + stp[5] # give region to preserve exact location
    Nettweet += '\nContinent: ' + stp[6] # give continent to preserve exact location
    Nettweet += '\nShare: ' + stp[7] # give sharable speedtest link

    return (Nettweet)

def build_tweets(api_pihole, ipstack_key):

    from lib.pihole_info import combinator as pi # where pihole information is gathered
    from lib.sys_info import sys_info as si # where system information is gathered
    from lib.speed_test import speedtest_ip as sip # where speedtest information is gathered

    p = pi(api_pihole[0], api_pihole[1])
    # build tweet
    PH_tweet = PHtweet(p)
    print("Pi-hole Tweet Made")
    SY_tweet = SYtweet(si())
    print("System Tweet Made")
    NET_tweet =  NETtweet(sip(ipstack_key))
    print("Speedtest Tweet Made")

    tweets = [PH_tweet, SY_tweet, NET_tweet]

    return(tweets)
