import requests
import pprint
import json
import os
def upload123(un,pd,id1):

# Specify the Endpoint URL replacing {servicenow_instance_name} with your ServiceNow Instance Name
    url = 'https://athenahealth.service-now.com/api/now/attachment/upload'

    # Specify Parameters for File Being Uploaded, the table_name and table_sys_id should be replaced with values that make
    # sense for your use case
    payload = {'table_name':'incident', 'table_sys_id': id1}
    # Eg. User name="admin", Password="admin" for this code sample. This will be sent across as basic authentication
    user = un
    pwd = pd

    # Set proper headers
    headers = {"Accept":"*/*"}
    # Specify Files To Send and Content Type. When specifying fles to send make sure you specify the path to the file, in
    # this example the file was located in the same directory as the python script being executed.
    # it is important to specify the correct file type
    s="C:\\Users\\gvarshini\\Desktop\\screenshot"
    for filename in os.listdir(s):
        s1=s+"\\"+filename
        files = {'file': (s1, open(s1, 'rb'), 'image/png', {'Expires': '0'})}
        response = requests.post(url, auth=(user, pwd), headers=headers, files=files, data=payload)

    # Send the HTTP request

    # Check for HTTP codes other than 201
    if response.status_code != 201:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        #exit()

    # Print Resopnse Details
    print('Response Status Code:', response.status_code)

    print('')
    print('Reponse Payload:')
    print(json.dumps(response.json(), indent=4))

#upload123('gvarshini','Athenahealth@12#','058e5a8bdbd20dd00e956ce2ca961983')

