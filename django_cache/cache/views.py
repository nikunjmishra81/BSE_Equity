import json
import logging
import os

import pandas as pd

import math

import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from common.common_constants import CommonConstants as constants
import redis as rd
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

logger = logging.getLogger(__name__)

redis = rd.Redis(host=constants.REDIS_HOST, port=6379, db=0)
class CacheDataView(APIView):

    def get(self, request):
        page = request.GET.get(constants.PAGE, '')
        size = request.GET.get(constants.SIZE, '')
        search = request.GET.get('name', '').upper()
        date = request.GET.get('date', '')
        if not page or not size:
            offset = None
            limit = None
        else:
            offset = int(page) * int(size)
            limit = int(size)
        dsate = redis.get(constants.CACHE_DATA + '_' + date)
        print("ds",dsate)
        if redis.get(constants.CACHE_DATA+'_'+date)!=[] and redis.get(constants.CACHE_DATA+'_'+date)!=None and date!='' :
            unparsed_data = redis.get(constants.CACHE_DATA + '_' + date).decode('utf8')
            unparsed_data  = unparsed_data.rstrip(',').replace('\n', ',')
            # unparsed_data = json.dumps(json.JSONDecoder().decode(unparsed_data))
            cache_data = eval(unparsed_data)
            if date:
                data_after_time_filter = list(filter(lambda x: str(x[constants.CREATED_AT]) == str(date), cache_data))
            else:
                data_after_time_filter = cache_data
            if search:
                data = [x for x in data_after_time_filter if x[constants.SC_NAME].startswith(search)]
            else:
                data = data_after_time_filter
            # if offset and limit:
            result = data[offset:offset + limit]
            # else:
            #     result = data
            response = {
                'total_data': len(data),
                'total_pages': math.ceil(len(data)/int(size)),
                'data': result}
            return Response(response, status=status.HTTP_200_OK)
            
        else:
            response ={
                'total_data': 0,
                'total_pages': 0,
                'data': []}
            return Response(response, status=status.HTTP_200_OK)


class PostDataInCache():
    def post_data_in_cache(self):
        try:
            today_date = datetime.date.today()
            changed_format = today_date.strftime("%d-%m-%y")
            date_string = changed_format.replace('-', '')
            url = constants.CSV_FILE_PATH.format(date_string)
            # url = constants.CSV_FILE_PATH.format(constants.BILL_FETCH_DATE)
            print("file path is",url)
            df = pd.read_csv(url,
                             usecols=[
                                 constants.SC_CODE,
                                 constants.SC_NAME,
                                 constants.OPEN,
                                 constants.HIGH,
                                 constants.LOW,
                                 constants.CLOSE
                             ])
            todays_date = datetime.date.today().strftime('%Y-%m-%d')
            df[constants.CREATED_AT] = todays_date
            json_data = df.to_json(orient='records', lines=True)
            """ To set data to the cache """
            redis.set(name = constants.CACHE_DATA+'_'+todays_date, value = json_data, keepttl=CACHE_TTL)
            os.remove(url)
            return {constants.MSG: json_data}
        except:
            print("Cron job ran for post_data_in_cache but not successful")
            return