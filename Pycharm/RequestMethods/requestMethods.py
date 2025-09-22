import requests


class RequestMain:

    @staticmethod
    def get_method(url, params=None, headers=None, body=None, json=None):
        response = requests.get(url, params=params, data=body, json=json, headers=headers)
        return response

    @staticmethod
    def post_method(url, params=None, headers=None, body=None, json=None,auth= None):
        response = requests.post(url, params=params, data=body, json=json, headers=headers,auth=auth)
        return response

    @staticmethod
    def put_method(url, params=None, headers=None, body=None, json=None):
        response = requests.put(url, params=params, data=body, json=json, headers=headers)
        return response

    @staticmethod
    def delete_method(url, params=None, headers=None, body=None, json=None):
        response = requests.post(url, params=params, data=body, json=json, headers=headers)
        return response

    @staticmethod
    def validate_statuscode(response=None,ExpectedStsCode=None):
        assert response.status_code == ExpectedStsCode, f"Expected: {ExpectedStsCode}, Actual:{response.status_code}"