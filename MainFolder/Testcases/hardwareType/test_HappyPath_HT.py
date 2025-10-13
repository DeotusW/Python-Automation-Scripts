from BaseFolder.Baseclass import Baseclass
from RequestMethods.requestMethods import RequestMain


class TestHappyPathHT(Baseclass):
    URL = "https://hrgav1lgvd.execute-api.eu-west-1.amazonaws.com/v1alpha1/statuses/"
    STATUSCODE = 200
    expected = {
        "serialNumber": "0411-000014",
        "hardwareType": "ACM"
    }

    def test_hardware_type(self):
        self.url = self.URL
        self.param = {"hardwareType": self.expected["hardwareType"]}
        self.headers = {"Authorization": f"Bearer {self.token}"}
        try:
            response = RequestMain().get_method(self.url,params=self.param,headers=self.headers)
            jsonresponse = response.json()
            RequestMain().validate_statuscode(response,self.STATUSCODE)

            if not jsonresponse:
                raise AssertionError("JSON Response is Empty")

            print(f" ID: {jsonresponse[0]['id']}")

            #Assertion Here
            for key,value in self.expected.items():
                assert jsonresponse[2][key] == value, f"{jsonresponse[2][key]} Mismatch! - Expected: {value}, Actual: {jsonresponse[2][key]}"

        except Exception as e:
            raise AssertionError(f"Testcase Failed: {e}")




