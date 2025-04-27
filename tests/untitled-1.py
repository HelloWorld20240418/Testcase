import pytest
from utils.request_handler import get, post
from config import HOST, CASE_CONFIGS
import time

REPORT_ID = ''

@pytest.fixture(params=CASE_CONFIGS)
def case_config(request):
    return request.param

@pytest.fixture
def teset_create_case(session_with_cookie, current_time_str, case_config):
    url = f"http://{HOST}/api/case"
    case_json = case_config["case_json"]
    if "_id" in case_json:
        del case_json["_id"]
    case_json['TestName'] = case_json['TestName'] + current_time_str
    case_json['DisplayName'] = case_json['TestName']
    res = post(session_with_cookie, url, case_json)
    assert res is not None
    assert res.status_code == 200
    json_data = res.json()
    case_id = json_data.get("Data", "") if json_data.get("ErrorCode", -1) == 0 else ""
    assert case_id, f"用例创建失败，响应: {json_data}"
    return case_id

def test_start_case(session_with_cookie, teset_create_case):
    """
    * 启动测试用例接口
    """
    url = f"http://{HOST}/api/case/{teset_create_case}/start"
    res = get(session_with_cookie, url)
    assert res is not None
    assert res.status_code == 200

def test_service_monitor(session_with_cookie):
    start_time = time.time()
    global REPORT_ID
    while time.time() - start_time < 30:  # 最多等待30秒
        status_data = nova_get_running_status(session_with_cookie)
        if status_data['Data'].get("TestStatus") == "Running":
            REPORT_ID = status_data['Data'].get('ReportID', '')
            assert True
        elif status_data['Data'].get("TestStatus") == "Stopped":
            break
        time.sleep(1)

def nova_get_running_status(session_with_cookie):
    """
    * 获取测试用例监控状态接口
    """
    url = f"http://{HOST}/api/running/status"
    response = get(session_with_cookie, url)
    assert response is not None
    assert response.status_code == 200
    return response.json()

def test_return_result(session_with_cookie, case_config):
    ip = HOST.replace('.', '_')
    global REPORT_ID
    test_type = case_config["test_type"]
    url = f"http://{HOST}/api/history/http_request_detail?reportId={REPORT_ID}&TestType={test_type}&hostIP={ip}"
    response = get(session_with_cookie, url)
    response_json = response.json()
    assert response_json['ErrorCode'] == 0
    print('')
    print('result:<<<<<<<<<<<<<<<<<<<<<<<<<<')
    for i in response_json['payload']:
        print(i['Doc_url_Path'], 'HTTP请求速率：', i['Request_Rate'])
    print('result>>>>>>>>>>>>>>>>>>>>>>>>>>>')
