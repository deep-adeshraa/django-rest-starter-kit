# Djang-Rest startet-kit

django project

1) Clone the repository
2) create your virtual environment for this project
       ` python3 -m venv "name of env`
3) install requirements `pip install -r requirements.txt`
4) migrate tables 
        `python3 manage.py migrate`
5) to create random data 
        `python3 manage.py generate_data` 

# Some Demo apis usage. provided all required params in postman collection
`base_url = https://deep-project.herokuapp.com`
1) to get user activity details you need token
   so first sign-up on url
   `{{base_url}}/api/sign-up/`
2) now your account is created so you need to login
    `{{base_url}}/api/sign-up/`
    
3) You will get token after successfull login
4) now hit get request on
    `{{base_url}}/api/get-activities/`
    
# thank you 
