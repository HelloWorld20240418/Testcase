from utils.request_handler import get
from config import HOST,CASE_JSON
from utils.request_handler import post
import time
import pytest

REPORT_ID = ''
@pytest.fixture
def teset_create_case(session_with_cookie,current_time_str):
    url = f"http://{HOST}/api/case"
    if "_id" in CASE_JSON:
        del CASE_JSON["_id"]
    CASE_JSON['TestName'] = CASE_JSON['TestName'] + current_time_str
    CASE_JSON['DisplayName'] = CASE_JSON['TestName']
    res = post(session_with_cookie, url, CASE_JSON)
    assert res is not None
    assert res.status_code == 200
    json_data = res.json()
    case_id = json_data.get("Data", "") if json_data.get("ErrorCode", -1) == 0 else ""
    assert case_id, f"用例创建失败，响应: {json_data}"
    return case_id

def test_start_case(session_with_cookie,teset_create_case):
    """
    * 启动测试用例接口
    """
    url = f"http://{HOST}/api/case/{teset_create_case}/start"
    res = get(session_with_cookie, url)
    assert res is not None
    assert res.status_code == 200

def test_service_monitor(session_with_cookie):
    start_time = time.time()
    while time.time() - start_time < 30:  # 最多等待30秒

        status_data = nova_get_running_status(session_with_cookie)
        global REPORT_ID

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
    response = get(session_with_cookie,url)
    assert response is not None
    assert response.status_code == 200
    return response.json()

#http://192.168.15.150/api/history/http_request_detail?reportId=67f48552e360c40f87789fd0&TestType=HttpCps&hostIP=192_168_15_150
def test_return_result(session_with_cookie):
    ip = HOST.replace('.', '_')
    global REPORT_ID
    url =f"http://{HOST}/api/history/http_request_detail?reportId={REPORT_ID}&TestType=HttpCps&hostIP={ip}"
    response = get(session_with_cookie,url)
    response_json = response.json()

    assert response_json['ErrorCode'] == 0
    print('')
    print('result:<<<<<<<<<<<<<<<<<<<<<<<<<<')
    for i in response_json['payload']:
        print(i['Doc_url_Path'],'HTTP请求速率：',i['Request_Rate'])
    #print('TPS:',response_json['payload'][0]['Request_Rate'])
    print('result>>>>>>>>>>>>>>>>>>>>>>>>>>>')