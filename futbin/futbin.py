from curl_cffi import requests
import time
from json import JSONDecodeError


def futbinPrice(item_id, platform='ps'):
    rc = requests.get('https://www.futbin.com/24/playerPrices', params={'player': str(item_id)},impersonate="chrome110")
    try:
        rc = rc.json()
    except JSONDecodeError:
        if rc.status_code == 503:
            time.sleep(5)
            return futbinPrice(item_id, platform=platform)  # this is wrong and it can be stuck here for very long time (until crash when no memory left probably)
        print('futbin response is not valid')
        print(rc.status_code)
        print(rc.url)
        print(rc.content)
        rc = {}
    if not rc:
        return 0
    rc = rc[str(item_id)]['prices']
    rc['ps']['LCPrice'] = rc['ps']['LCPrice'].replace(',', '')
    ps = int(rc['ps']['LCPrice'])
    price = ps


    return price
if __name__ == '__main__':
    print(futbinPrice(260908))