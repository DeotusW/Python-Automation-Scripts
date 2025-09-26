import json
from pathlib import Path
import pytest
from BaseFolder.Baseclass import Baseclass
from RequestMethods.requestMethods import RequestMain

__testdata = None

# Loading Testdata from Json file

def get_testdata():
    global __testdata
    if __testdata is None:
        CurrentPath = Path(__file__)
        try:
            with open(CurrentPath.parent.parent / "Testdata" / "stepNumber_and_stepNumber_Testdata.json", "r") as f:
                __testdata = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("The Testdata JSON file is missing - Not Found!")
    return __testdata

class TestNegativeCases(Baseclass):

    URL = "https://hrgav1lgvd.execute-api.eu-west-1.amazonaws.com/v1alpha1/statuses/"
    STATUS_CODE = 400
    CurrentFilePath = Path(__file__).resolve()

    @pytest.mark.parametrize("tcs", get_testdata())
    def test_negative_case(self,tcs):
            try:
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

            except Exception as e:
                raise AssertionError(f"Testcase Failed: {e}")





