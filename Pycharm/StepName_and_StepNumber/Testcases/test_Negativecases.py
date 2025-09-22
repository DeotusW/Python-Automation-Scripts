import json

import pytest

from Pycharm.Baseclass.Baseclass import Baseclass
from Pycharm.RequestMethods.requestMethods import RequestMain


class TestNegativeCases(Baseclass):

    #Loading Testdata from Json file.
    with open("C:/Users/dwilson3/Documents/Python-Automation-Scripts/Pycharm/StepName_and_StepNumber/Testdata/stepNumber_and_stepNumber_Testdata.json","r") as f:
        testdata = json.load(f)

    URL = "https://hardware-activation.stg.agco-fuse-services.com/v1alpha1/statuses/"
    STATUS_CODE = 400

    @pytest.mark.parametrize("tcs",testdata)
    def test_negative_case(self,tcs):
        request = RequestMain()
        self.url = self.URL
        self.param = {
            "currentStepName": tcs["currentStepName"],
            "currentStepNumber": tcs["currentStepNumber"]
        }
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = request.get_method(self.url,params=self.param,headers=self.headers)
        jsonresponse = response.json()
        request.validate_statuscode(response, self.STATUS_CODE)
        assert jsonresponse["message"] == tcs["ExpectedMessage"], "Expected Message doesn't Match"





