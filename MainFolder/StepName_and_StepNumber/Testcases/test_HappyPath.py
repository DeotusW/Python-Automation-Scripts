import requests
from BaseFolder.Baseclass import Baseclass
from RequestMethods.requestMethods import RequestMain


class TestHappyPath(Baseclass):

    expected = {
    "serialNumber": "0412-000105",
    "currentStepName": "Activation_Send_NC",
    "currentStepNumber": 6
    }

    STATUS_CODE = 200
    URL = "https://hrgav1lgvd.execute-api.eu-west-1.amazonaws.com/v1alpha1/statuses/"

    def test_stepName_and_stepNumber(self):
        self.url = self.URL
        self.param ={
            "currentStepName": self.expected["currentStepName"],
            "currentStepNumber": self.expected["currentStepNumber"]
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

            if not jsonresponse:
                raise AssertionError("API returned an empty response")

            #Assertion
            for key,value in self.expected.items():
                assert jsonresponse[0][key] == value, f"{jsonresponse[0][key]} Mismatch!, Expected {value}, Actual {jsonresponse[0][key]}"

            print(f" ID: {jsonresponse[0]['id']}")
        except Exception as e:
            raise AssertionError(f"Testcase Failed: {e}")



