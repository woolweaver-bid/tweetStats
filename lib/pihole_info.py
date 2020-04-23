#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# retreive data from pi-hole api.php (probably will break in a future update of pi-hole)

def reach_pihole(api_url):

    from requests import get # handles communication to pi-hole

    # verify pi-hole reachability
    try:
        api1 = get(api_url[0])# is passed from get_cfgp
        x1 = api1.status_code
    except Exception as e:
        x = 'Could not contact API: ' + str(e)
        return x

    try:
        api2 = get(api_url[1])# is passed from get_cfgp
        x2 = api2.status_code
    except Exception as e:
        x = 'Could not contact API: ' + str(e)
        return x

    d1 = api1.json()
    d2 = api2.json()

    if not all(k in d1 for k in # check for needed variables
               ("domains_being_blocked", "dns_queries_today", "ads_blocked_today", "ads_percentage_today", "queries_forwarded", "queries_cached", "unique_clients", "privacy_level", "gravity_last_updated")):
        print('This is not Pi-Hole JSON...') # complain if all aren't present
        return

    if not all(k in d2 for k in # check for needed variables
               ("domains_being_blocked", "dns_queries_today", "ads_blocked_today", "ads_percentage_today", "queries_forwarded", "queries_cached", "unique_clients", "privacy_level", "gravity_last_updated")):
        print('This is not Pi-Hole JSON...') # complain if all aren't present
        return

    return (d1, d2, x1, x2)


def combinator(d1, d2):

    from lib.commaValue import commaValue as cv
    from datetime import datetime as dt # used to calculate UTC from epoch

    # setup pi-hole variables
    ads_blocked_today = d1["ads_blocked_today"] + d2["ads_blocked_today"] #  total number of ads block for the last 24 hrs
    ads_today = str(cv(ads_blocked_today))

    dns_queries_today = d1["dns_queries_today"] + d2["dns_queries_today"] # pihole_info[1] - total number of dns queries for the last 24 hrs
    queries_today = str(cv(dns_queries_today))

    ads_percentage_today = (ads_blocked_today/dns_queries_today)*100 # percentage of ads block for the last 24 hrs
    percent_today = str(round(ads_percentage_today, 2))

    ads_blocked = ads_today + '|' + percent_today + '%' # pihole_info[2]

    queries_forwarded = d1["queries_forwarded"] + d2["queries_forwarded"] # pihole_info[3] - number of queries forward to upstream DNS
    forwarded = str(cv(queries_forwarded))

    queries_cached = d1["queries_cached"] + d2["queries_cached"] # pihole_info[4] - number of queries cached
    cached = str(cv(queries_cached))

    blocked_pi1 = str(cv(d1["domains_being_blocked"]))
    blocked_pi2 = str(cv(d2["domains_being_blocked"]))  # pihole_info[0] - Total number of domians on the block list

    clients_pi1 = str(d1["unique_clients"])
    clients_pi2 = str(d2["unique_clients"]) # pihole_info[5] - number of unique clients

    clients =  clients_pi1 + "|" + clients_pi2 

    levels_pi1 = str(d1["privacy_level"])
    levels_pi2 = str(d2["privacy_level"]) # pihole_info[6] - Admin Privacy level selected

    levels = levels_pi1  + "|" + levels_pi2

    glaPI1 = d1["gravity_last_updated"]
    glaPI2 = d2["gravity_last_updated"]

    gluPI1 = dt.utcfromtimestamp(glaPI1["absolute"]).strftime('%Y-%m-%d %H:%M') # pihole_info[7] - date gravity was updated last
    gluPI2 = dt.utcfromtimestamp(glaPI2["absolute"]).strftime('%Y-%m-%d %H:%M') # pihole_info[7] - date gravity was updated last

    glu1 = gluPI1 + "|" + blocked_pi1
    glu2 = gluPI2 + "|" + blocked_pi2

    return ( ads_blocked, forwarded, cached, queries_today, clients, levels, glu1, glu2)
