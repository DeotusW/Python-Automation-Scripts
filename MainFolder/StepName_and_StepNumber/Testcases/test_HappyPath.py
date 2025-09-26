import requests
from BaseFolder.Baseclass import Baseclass
from RequestMethods.requestMethods import RequestMain


class TestHappyPath(Baseclass):

    STEP_NAME = "Activation_Send_NCP"
    STEP_NUMBER = "6"
    EXPECTED_SERIAL = "0410-000015"
    STATUS_CODE = 200
    URL = "https://hrgav1lgvd.execute-api.eu-west-1.amazonaws.com/v1alpha1/statuses/"

    def test_stepName_and_stepNumber(self):
        self.url = self.URL
        self.param ={
            "currentStepName": self.STEP_NAME,
            "currentStepNumber": self.STEP_NUMBER
        }
        self.headers={
            "Authorization" : f"Bearer {self.token}"
        }

        try:
            #response = requests.get(self.url,params=self.param,headers=self.headers)
            response = RequestMain().get_method(self.url,params=self.param,headers=self.headers)
            jsonresponse = response.json()
            #assert response.status_code == self.STATUS_CODE, f"Expected: 200, Actual:{response.status_code}"
            RequestMain().validate_statuscode(response,self.STATUS_CODE)
            #print(jsonresponse)

            assert jsonresponse[0]["serialNumber"] == self.EXPECTED_SERIAL, "Serial Number doesn't match"
            print(f"ID: {jsonresponse[0]['id']}")

        except Exception as e:
            raise AssertionError(f"Testcase Failed: {e}")

