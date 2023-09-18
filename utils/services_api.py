import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import environ

env = environ.Env()
environ.Env.read_env()

api_key = os.environ.get('api_key')


@csrf_exempt
def aadhar_to_pan_api(request, aadhaar_no):
    if request.method == 'POST':
        # API URL
        api_url = f"https://neofind.in/admin/api/index.php?api_key=e0a3f5e2b7c386a9&aadhaar_no={aadhaar_no}"

        # Make the API call
        response = requests.post(api_url)
        print(api_url)

        # Check the response
        if response.status_code == 200:
            # API call was successful
            result = response.json()
            return result
        else:
            # Handle the error here
            error_message = f"API call failed with status code {response.status_code}"
            return JsonResponse({'error': error_message}, status_code=500)

    return JsonResponse({'error': 'Invalid request method'}, status_code=405)
