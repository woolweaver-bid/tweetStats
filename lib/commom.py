#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.pihole_info import combinator as pi # where pihole information is gathered

from lib.pihole_info import reach_pihole as rp # test pihole reachability

from lib.get_api import get_keysANDapi as gka # where we interact with the Twitter API

from lib.speed_test import check_ipstack as cip # check ipstack key

from lib.get_config  import get_cfg as cfg # twitter keys

from lib.construct_tweet import build_tweets as bt

    # where we interact with the Twitter API
from lib.get_api import get_keysANDapi as gka


cfgD = cfg()

keysANDapi = gka(cfgD[0])
k_a = cfgD[0]
rpia = cfgD[1]

rpi = rp(rpia)

phs = pi(rpi[0], rpi[1])

ipstack_key = cfgD[2]

cips = cip(ipstack_key)[2]


