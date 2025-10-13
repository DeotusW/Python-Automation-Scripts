import json
from pathlib import Path

import pytest

from BaseFolder.Baseclass import Baseclass
from RequestMethods.requestMethods import RequestMain

testdata_HT = None

def get_testdata_HT():
    global testdata_HT
    CurrentFilePath = Path(__file__)
    if testdata_HT is None:
        try:
            with open(CurrentFilePath.parent.parent/"Testdata"/"hardwareType_Testdata.json","r") as f:
                testdata_HT = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("The Testdata JSON file is missing - Not Found!")
    return testdata_HT

class TestNegCasesHT(Baseclass):
    URL = "https://hrgav1lgvd.execute-api.eu-west-1.amazonaws.com/v1alpha1/statuses/"

    @pytest.mark.parametrize("HT", get_testdata_HT())
    def test_hardware_type_Neg(self,HT):
        self.params = {
            "hardwareType": HT["hardwareType"]
        }
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }
        try:
            response = RequestMain().get_method(self.URL, params=self.params, headers=self.headers)
            jsonresponse = response.json()
            if not jsonresponse:
                print("JSON Response is Empty")
                #print(HT["StatusCode"])
                RequestMain().validate_statuscode(response,HT["StatusCode"])
            else:
                #print(HT["StatusCode"])
                RequestMain().validate_statuscode(response, HT["StatusCode"])
                assert jsonresponse["message"] == HT["ExpectedMessage"], f"Expected Message doesn't Match!"

        except Exception as e:
            raise AssertionError(f"Testcase Failed: {e}")



