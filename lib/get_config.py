#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def load_config():
    import json as js  # Used to parse config.json

    # check for config.json
    try:
        with open('config.json') as data:
           cfg = js.load(data)
        except FileNotFoundError as e:
           print(e)
        raise SystemExit
    return (cfg)

# get data needed for pi-hole communication
def get_cfgp():

    cfg = load_config()

    # verify && set key info from config.json
    cfgP = cfg['pihole']
    try: # try to get api_path for pi-hole
        api = cfgP['api_path']
    except KeyError as e:
        print(str(e) + ' variable(s) not found.')
        raise SystemExit
    if not (api): #verify api_path is not None
        print('Please check your config.ini.')
        raise SystemExit
    # return as tuple to ensure data integrity
    return (api)

# get data needed for twitter communication
def get_cfgt():

    cfg = load_config()

    # verify && set key info from config.json
    cfgT = cfg['twitter']
    try:
        keys = dict(consumer_key=cfgT['consumer_key'], consumer_secret=cfgT['consumer_secret'],
                    access_token_key=cfgT['access_token'], access_token_secret=cfgT['access_token_secret'])
    except KeyError as e:
        print(str(e) + ' variable(s) not found.')
        raise SystemExit
    if not (keys): #verify value is not None
        print('Please check your config.ini.')
        raise SystemExit

    return (keys)

def get_cfgip():

    cfg = load_config()

    cfgip = cfg['ipstack']
    try: # try to get api_path for pi-hole
        ipstackKey = cfgip['access_key']
    except KeyError as e:
        print(str(e) + ' variable(s) not found.')
        raise SystemExit
    if not (ipstackKey): #verify value is not None
        print('Please check your config.ini.')
        raise SystemExit

    return (ipstackKey)