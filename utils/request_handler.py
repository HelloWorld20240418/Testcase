import logging

logging.basicConfig(level=logging.INFO)

def post(session, url, data=None):
    try:
        response = session.post(url, json=data)
       # logging.info(f"[POST] {url} | Data: {data} | Status: {response.status_code}")
        return response
    except Exception as e:
        logging.error(f"POST 请求失败: {e}")
        return None

def get(session, url):
    try:
        response = session.get(url)
       # logging.info(f"[GET] {url} | Status: {response.status_code}")
        return response
    except Exception as e:
        logging.error(f"GET 请求失败: {e}")
        return None
