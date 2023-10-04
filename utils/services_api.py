import requests
from django.views.decorators.csrf import csrf_exempt
import environ
from services.models import ServiceKeys
import logging

env = environ.Env()
environ.Env.read_env()

@csrf_exempt
def aadhar_to_pan_api(request, aadhaar_no,application_no):
    api_key = ServiceKeys.objects.get(id='AADHAR_TO_PAN_KEY').api_key

    # API URL
    api_url = f"https://neofind.in/admin/api/index.php?application_no={application_no}&api_key={api_key}&aadhaar_no={aadhaar_no}"

    # Make the API call
    response = requests.post(api_url)

    # Check the response
    result = response.json()
    return result


@csrf_exempt
def voter_api(request, epic_no):
    api_key = ServiceKeys.objects.get(id='VOTER_KEY').api_key

    # API URL
    api_url = f"https://api.gtelapi.com/voterapi/monthly.php?mobile=7056757439&apikey={api_key}&epicno={epic_no}"

    # Make the API call
    response = requests.post(api_url)

    # Check the response
    result = response.json()
    print(result)
    return result