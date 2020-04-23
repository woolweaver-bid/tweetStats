#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Get data from config.json
def load_config():

    import json as js

    try:
        with open('config.json') as data:
            cfg = js.load(data)
    except FileNotFoundError as e:
        print(str(e) + '\nPlease see the ReadMe for info on how to get going.')
        raise SystemExit
    return (cfg)

# Assign data from config file to proper places
def get_cfg():

# Actually load our data
    cfg = load_config()

# verify && set key info from config.json
    cfgP = cfg['pihole']
    try: # try to get api_path for pi-hole
        api1 = cfgP['api_path_1']
        api2 = cfgP['api_path_2']
    except KeyError as e:
        print(str(e) + '\nPi-hole web API address is missing.')
        raise SystemExit
    if not (api1 or api2): #verify api_path is not None
        print('Please check your config.ini. Pi-hole web API address is missing.')
        raise SystemExit

    api = (api1, api2)

# get data needed for twitter communication
    cfgT = cfg['twitter']
# verify && set key info from config.json
    try:
        keys = dict(consumer_key=cfgT['consumer_key'], consumer_secret=cfgT['consumer_secret'],
                    access_token_key=cfgT['access_token'], access_token_secret=cfgT['access_token_secret'])
    except KeyError as e:
        print(str(e) + '\nOne or more Twitter API keys are missing.')
        raise SystemExit
    if not (keys): #verify value is not None
        print('Please check your config.ini. One or more Twitter API keys are missing.')
        raise SystemExit


    cfgip = cfg['ipstack']
    try: # try to get api_key for ipstack.com
        ipstackKey = cfgip['access_key']
    except KeyError as e:
        print(str(e) + '\nipstack.com api key is missing.')
        raise SystemExit
    if not (ipstackKey): #verify value is not None
        print('Please check your config.ini. ipstack.com api key is missing.')
        raise SystemExit

    return (keys, api, ipstackKey)