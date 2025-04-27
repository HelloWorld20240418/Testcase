import pytest
from datetime import datetime
import requests
from config import HOST, USERNAME, PASSWORD

@pytest.fixture(scope="session")
def session_with_cookie():
    session = requests.Session()
    login_url = f"http://{HOST}/api/user/login"
    res = session.post(login_url, json={"name": USERNAME, "password": PASSWORD})
    assert res.status_code == 200, "登录失败"
    # 可以打印查看是否登录成功
    #print("登录成功，cookies:", session.cookies.get_dict())
    return session


@pytest.fixture
def current_time_str():
    """返回当前时间的字符串，格式为 YYYY-MM-DD HH:MM:SS"""
    return datetime.now().strftime("%Y%m%d-%H%M%S")






