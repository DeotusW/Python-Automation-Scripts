import json
from pathlib import Path
from BaseFolder.Baseclass import Baseclass
from RequestMethods.requestMethods import RequestMain
from StepName_and_StepNumber.Testcases.filetest import CurrentPath


class TestNegativeCases(Baseclass):

    URL = "https://hardware-activation.stg.agco-fuse-services.com/v1alpha1/statuses/"
    STATUS_CODE = 400
    CurrentFilePath = Path(__file__).resolve()
    testdata = None

    #Loading Testdata from Json file
    @property
    def loadtestdata(self):
        if self.testdata is None:
            with open(CurrentPath.parent.parent/"Testdata"/"stepNumber_and_stepNumber_Testdata.json", "r") as f:
                self.testdata = json.load(f)
        return self.testdata


    def test_negative_case(self):

        for tcs in self.loadtestdata:
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





