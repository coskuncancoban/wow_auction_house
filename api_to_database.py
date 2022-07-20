import api_requests
import json
from varname.helpers import Wrapper


#Assign the response to a variable. 
realms_response = api_requests.realm_request()


#Write response to file.
def json_file(response):
    json_string = json.dumps(response) #json to str
    response = Wrapper(response) #seperate the name and value.
    json_file = open (f"./databases/{response.name}.json", "w" ) #create file
    json_file.write(json_string) #write data to file
    json_file.close #close file
