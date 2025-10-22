from BaseFolder.Baseclass import Baseclass
from RequestMethods.requestMethods import RequestMain


class BaseHappyPath(Baseclass):

    URL = "https://hrgav1lgvd.execute-api.eu-west-1.amazonaws.com/v1alpha1/statuses/"
    STATUSCODE = 200
    EXPECTED = {}
    PARAMS = {}
    INDEX = 0

    def get_json_response(self):
        self.HEADERS = {"Authorization": f"Bearer {self.token}"}
        response = RequestMain().get_method(self.URL,params = self.PARAMS,headers=self.HEADERS)
        return response

    def validate_json_response(self,response,jsonResponse):
        RequestMain().validate_statuscode(response,self.STATUSCODE)
        if not jsonResponse:
            raise AssertionError("API returned an empty response")
        for item in jsonResponse:
            if item["id"] == self.EXPECTED["id"]:
                print(f"ID: {item['id']}")
                for key, value in self.EXPECTED.items():
                    assert item[key] == value, f"{item[key]} Mismatch! - Expected: {value}, Actual: {item[key]}"

    def HappyPathTest(self):
        try:
            response = self.get_json_response()
            jsonResponse = response.json()
            if not jsonResponse:
                raise AssertionError("JSON Response is Empty")
            self.validate_json_response(response,jsonResponse)
        except Exception as e:
            raise AssertionError(f"Testcase Failed: {e}")

