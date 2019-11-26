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
            debug = (str(success) + "\n\nipstack API URL\n" + address)
        else:
            if badip == None:
                debug = ("please check your IP address \n\nipstack API URL\n" + address)
            else:
                debug = ("something is really broken")
    except KeyError as e:
        debug = ("invalid access key \n\nipstack API URL\n" + address)

    return (url_json, ip, debug)

def speedtest_ip():

    import speedtest

    servers = []
    # If you want to test against a specific server
    # servers = [1234]

    threads = None
    # If you want to use a single threaded test
    # threads = 1

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    data = s.results.dict()

    cip = check_ipstack()
    ipstack = cip[0]

    ulByte = data["bytes_sent"]/1024/1024
    dlByte = data["bytes_received"]/1024/1024
    us = data["upload"]/1000000
    ds = data["download"]/1000000
    pg = data["ping"]

    client = data["client"]
    isp = client["isp"]

    uls = round(us, 2)
    dls = round(ds, 2)
    pings = round(pg, 2)
    dlMB = round(dlByte, 2)
    ulMB = round(ulByte, 2)

    # variables to be passed
    share = data["share"]
    ping = str(pings) + " ms"
    ul = str(uls) + " Mbps"
    dl = str(dls) + " Mbps"
    speed = ul + "/" + dl
    ulMBs = str(ulMB) + " MB"
    dlMBs = str(dlMB) + " MB"
    Sdata = ulMBs + "/" + dlMBs
    ip = '.'.join(cip[1].split('.')[:2]) + '.xx.xx'
    region = ipstack['region_name']
    continent = ipstack['continent_name']

    return (ping, speed, Sdata, ip, isp, region, continent, share)
