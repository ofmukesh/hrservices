import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import environ

env = environ.Env()
environ.Env.read_env()

client_id = os.environ.get('invi_client_id')
secret_key = os.environ.get('invi_secret_key')


@csrf_exempt
def aadhar_to_pan_api(request, aadhaar_no):
    if request.method == 'POST':
        # API URL
        api_url = 'https://api.invincibleocean.com/invincible/aadhaarToPan'

        # Request data
        data = {
            'aadharNumber': aadhaar_no  # Replace with the Aadhar number you want to query
        }

        # Headers
        headers = {
            'clientId': client_id,
            'secretKey': secret_key,
            'Content-Type': 'application/json'
        }

        # Make the API call
        response = requests.post(api_url, json=data, headers=headers)

        # Check the response
        if response.status_code == 200:
            # API call was successful
            result = response.json()
            return JsonResponse(result)
        else:
            # Handle the error here
            error_message = f"API call failed with status code {response.status_code}"
            return JsonResponse({'error': error_message}, status_code=500)

    return JsonResponse({'error': 'Invalid request method'}, status_code=405)
