from locust import HttpUser, between, task
import requests
import random



class MobileApp(HttpUser):
    wait_time = between(1, 10)
    weight = 9
    
    @task(5)
    def V2_NewAssignment(self):
        n = random.randint(0,22000)
        self.client.get("/v2/newassignment/"+str(n), name="/v2/newassignment")
    
    @task(5)
    def V1_NewAssignment(self):
        n = random.randint(0,22000)
        self.client.get("/newassignment/"+str(n), name="/v1/newassignment")

    @task(2)
    def V2_image_upload(self):
        #url = 'https://photoscavenger.vdotvo9a4e2a6.eu-central-1.cs.amazonlightsail.com/v2/uploadfile/person'
        url = 'localhost/v2/uploadfile/person'
        with open('Testimages/family.png', 'rb') as image:
            payload={}
            files=[('file',image)]
            headers = {}
            response =  self.client.request("POST", url, headers=headers, data=payload, files=files)
            

    @task(2)
    def V1_image_upload(self):
        #url = 'https://photoscavenger.vdotvo9a4e2a6.eu-central-1.cs.amazonlightsail.com/uploadfile/person'
        url = 'localhost/uploadfile/person'
        with open('Testimages/family.png', 'rb') as image:
            payload={}
            files=[('file',image)]
            headers = {}
            response =  self.client.request("POST", url, headers=headers, data=payload, files=files)





class Website(HttpUser):
    wait_time = between(1, 3)
    weight = 1

    @task(3)
    def example(self):
        self.client.get("/exampleresponse")
    
    @task(3)
    def homepage(self):
        self.client.get("/")