#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_ipstack():

    from lib.get_config import get_cfgip as cfgIP

    from requests import get

    key = cfgIP()
    ip = get('https://www.wikipedia.org').headers['X-Client-IP']
    address = "http://api.ipstack.com/" + ip + "?access_key=" + key + "&output=json&fields=region_name,continent_name"

    url = get(address)
    url_json = url.json()
    success = url.status_code

    try:
        badip = url_json["region_name"]
        if badip != None:
            debug = (str(success) + "\nipstack API URL\n" + address)
        else:
            if badip == None:
                debug = ("please check your IP address \nipstack API URL\n" + address)
            else:
                debug = ("something is really broke")
    except KeyError as e:
        debug = ("invalid access key \nipstack API URL\n" + address)

    return (url_json, ip, debug)

def speedtest_ip():

    import os
    import json

    jstring = os.popen("speedtest-cli --share --json").read()
    data = json.loads(jstring)
    client = data["client"]

    ulByte = data["bytes_sent"]/1024/1024
    dlByte = data["bytes_received"]/1024/1024
    us = data["upload"]/1000000
    ds = data["download"]/1000000
    pg = data["ping"]
    isp = client["isp"]
    share = data["share"]

    uls = round(us, 2)
    dls = round(ds, 2)
    pings = round(pg, 2)
    dlMB = round(dlByte, 2)
    ulMB = round(ulByte, 2)

    ping = str(pings) + " ms"

    ul = str(uls) + " Mbps"
    dl = str(dls) + " Mbps"
    speed = ul + "/" + dl

    ulMBs = str(ulMB) + " MB"
    dlMBs = str(dlMB) + " MB"
    Sdata = ulMBs + "/" + dlMBs

    ip = '.'.join(check_ipstack()[1].split('.')[:2]) + '.xx.xx'
    
    ipstack = check_ipstack()[0]
    region = ipstack['region_name']
    continent = ipstack['continent_name']

    return (ping, speed, Sdata, ip, isp, region, continent, share)