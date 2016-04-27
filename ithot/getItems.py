# coding=utf-8

import json
import requests

if __name__ == '__main__':
    city = '%E4%B8%8A%E6%B5%B7'
    data = {'first':'false', 'pn':141, 'kd':'Java'}
    r = requests.post('http://www.lagou.com/jobs/positionAjax.json?city=' + city, data)

    ret = json.loads(r.text.encode('utf-8'))

    result = ret['content']['result']

    for item in result:
        print item['positionId'], item['companyId']
