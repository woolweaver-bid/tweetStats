#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# login to Twitter
def get_api():

    from lib.get_config import get_cfgt as cfgt
    from TwitterAPI import TwitterAPI

    keys = cfgt()

    KEYS_and_API = TwitterAPI(**keys)

    verify = KEYS_and_API.request('account/verify_credentials')

    for item in verify.get_iterator():
      if 'screen_name' in item:
        print("logged in as @" + item['screen_name'])

    return (KEYS_and_API)