from django.shortcuts import render
import requests
import urllib3
import json
from .models import LearningPlan

# Gets the Learning plan details
def getLearningPlanData(request):
    # Send the body of the data
    data = {
        "grant_type":"client_credentials",
        "scope":{
        "userId":"SFADMIN",
        "companyId":"talenteam",
        "userType":"user",
        "resourceType":"learning_public_api"
    }
        }
    headers = {'Authorization': '',
               'Content-Type': 'application/json'}
    url = 'https://talenteam-stage.plateau.com/learning/oauth-api/rest/v1/token'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    data = response.json()
    access_token = data['access_token']


    if (access_token):
        http = urllib3.PoolManager()
        url = 'https://talenteam-stage.plateau.com/learning/odatav4/public/user/learningPlan/v1/UserTodoLearningItems?$filter=criteria/includeDeeplink eq true and criteria/includeLearnerActions eq true&$format=json&$select=title'
        token = f"Bearer {access_token}"
        print(token)
        r = http.request(
            'GET',
            url,
            headers={'Authorization': token, 'Content-Type': 'application/json'}
        )
        print(r.data)
        return urllib3.HTTPResponse("Successful call")