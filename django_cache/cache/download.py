import json
import uuid

import schedule
import time
import os
import sys
import pandas as pd
from django.core.cache import cache


# sys.path.insert(0, os.path.realpath('/Users/harshmule/Projects/djangopractic/redis_cache/django_cache')+'/')

from io import BytesIO
import datetime
from zipfile import ZipFile
from urllib.request import Request, urlopen
from common.common_constants import CommonConstants



def extract_zip():
    try:
        print("Cron for extract_zip Started at ", datetime.datetime.now())
        # today_date = datetime.date.today() - datetime.timedelta(days=1)

        # today_date = datetime.date.today()
        # changed_format = today_date.strftime("%d-%m-%y")
        # date_string = changed_format.replace('-', '')
        # url = CommonConstants.ZIP_FILE_URL.format(date_string)
        url = CommonConstants.ZIP_FILE_URL.format(CommonConstants.BILL_FETCH_DATE)

        print("url is", url)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                print(CommonConstants.BASE_FILE_PATH + CommonConstants.RELATIVE_FILE_PATH)
                zfile.extractall(CommonConstants.BASE_FILE_PATH + CommonConstants.RELATIVE_FILE_PATH)
                print("Cron for extract_zip ended at ", datetime.datetime.now())
    except:
        print("Cron job ran for extract_zip but not successful")
        return


# schedule.every().day.at("10").do(extract_zip)
# schedule.every().day.at("01:51").do(PostDataInCacheIn)
# schedule.every(10).seconds.do(extract_zip)
def PostDataInCacheIn():
    print("Cron for PostDataInCacheIn Started at ", datetime.datetime.now())
    from cache.views import PostDataInCache
    postclass = PostDataInCache()
    postclass.post_data_in_cache()
    print("Cron ended at ", datetime.datetime.now())
    pass

# def jobb():
#     print("container is up")
# schedule.every(10).seconds.do(PostDataInCacheIn)
# schedule.every(2).seconds.do(jobb)
#
schedule.every().day.at(CommonConstants.EXTRACT_FILE_TIME).do(extract_zip)
schedule.every().day.at(CommonConstants.PUT_DATA_IN_CACHE_TIME).do(PostDataInCacheIn)
while 1:
    schedule.run_pending()
    time.sleep(1)
