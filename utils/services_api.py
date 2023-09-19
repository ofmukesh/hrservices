import requests
from django.views.decorators.csrf import csrf_exempt
import environ
from services.models import ServiceKeys
import json

env = environ.Env()
environ.Env.read_env()

@csrf_exempt
def aadhar_to_pan_api(request, aadhaar_no):
    api_key = ServiceKeys.objects.get(id='AADHAR_TO_PAN_KEY').api_key

    # API URL
    api_url = f"https://neofind.in/admin/api/index.php?application_no=$application_no&api_key={api_key}&aadhaar_no={aadhaar_no}"

    # Make the API call
    response = requests.post(api_url)

    # Check the response
    result = response.json()
    return result