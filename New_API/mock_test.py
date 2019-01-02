from mock import mock

from manage_data.Run_Request import Run_Request


def mock_test(response_data,url,method,request_data):
    run = Run_Request()
    run.run_method = mock.Mock(return_value=response_data)
    return run.run_method(url,method,request_data)