import requests
from PythonAutomation.Pycharm.Baseclass.Baseclass import Baseclass
from PythonAutomation.Pycharm.RequestMethods.requestMethods import RequestMain


class TestHappyPath(Baseclass):

    STEP_NAME = "Activation_Send_NCP"
    STEP_NUMBER = "6"
    EXPECTED_SERIAL = "0412-000105"
    STATUS_CODE = 200
    URL = "https://hardware-activation.stg.agco-fuse-services.com/v1alpha1/statuses/"

    def test_stepName_and_stepNumber(self):
        self.request = RequestMain()
        self.url = self.URL
        self.param ={
            "currentStepName": self.STEP_NAME,
            "currentStepNumber": self.STEP_NUMBER
        }
        self.headers={
            "Authorization" : f"Bearer {self.token}"
        }

        #response = requests.get(self.url,params=self.param,headers=self.headers)
        response = self.request.get_method(self.url,params=self.param,headers=self.headers)
        jsonresponse = response.json()
        #assert response.status_code == self.STATUS_CODE, f"Expected: 200, Actual:{response.status_code}"
        self.request.validate_statuscode(response,self.STATUS_CODE)
        #print(jsonresponse)

        assert jsonresponse[0]["serialNumber"] == self.EXPECTED_SERIAL, "Serial Number doesn't match"
        print(f" ID: {jsonresponse[0]["id"]}")

