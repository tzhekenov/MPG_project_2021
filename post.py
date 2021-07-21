import requests


headers = {
    "Authorization": "Basic 1455897457",
    "Content-Type": "application/json"
}

data = {
    "github":"https://github.com/tzhekenov/MPG_project_2021",
    "email":"temirlan.zhekenov@nu.edu.kz",
    "url":"https://us-central1-aiplatform.googleapis.com/v1/projects/301525520780/locations/us-central1/endpoints/1664836526313308160", 
    "notes":"mpg_predicted = 17.07827"
}


r = requests.post('https://dps-challenge.netlify.app/.netlify/functions/api/challenge', data=data, headers=headers)

print(r.status_code)
print(r.json())
