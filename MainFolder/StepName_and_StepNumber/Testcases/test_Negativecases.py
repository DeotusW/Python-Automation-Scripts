import json

import pytest

from BaseFolder.Baseclass import Baseclass
from RequestMethods.requestMethods import RequestMain

class TestNegativeCases(Baseclass):

    #Loading Testdata from Json file.
    @staticmethod
    def loadtestdata():
        with open("MainFolder/StepName_and_StepNumber/Testdata/stepNumber_and_stepNumber_Testdata.json", "r") as f:
            testdata = json.load(f)
            return testdata

    URL = "https://hardware-activation.stg.agco-fuse-services.com/v1alpha1/statuses/"
    STATUS_CODE = 400
    TESTDATA = loadtestdata()

    @pytest.mark.parametrize("tcs",TESTDATA)
    def test_negative_case(self,tcs):
        self.url = self.URL
        self.param = {
            "currentStepName": tcs["currentStepName"],
            "currentStepNumber": tcs["currentStepNumber"]
        }
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = RequestMain().get_method(self.url,params=self.param,headers=self.headers)
        jsonresponse = response.json()
        RequestMain().validate_statuscode(response, self.STATUS_CODE)
        assert jsonresponse["message"] == tcs["ExpectedMessage"], "Expected Message doesn't Match!"





