# import mpesawrapper
# mpesa=mpesawrapper.Generatetoken()
# token=mpesa.generate_token(consumer_key="GC2WUo0oFPkUt4ARPbA37mtwGHN3vGAE",consumer_secret="LVrZL1rvCMkAgjXG")
# print (token)
# import uplink,json
#
#
# # To define common request metadata, you can decorate the class
# # rather than each method separately.
# @uplink.headers({"Accept": "application/vnd.github.v3.full+json"})
# class GitHub(uplink.Consumer):
#
#     @uplink.json
#     @uplink.post("/help")
#     def update_user(self, **info:uplink.Body):
#         print (type(uplink.Body))
#
#
# github = GitHub(base_url="http://localhost:8888")
# response = github.update_user(bio="Beam me up, Scotty!",text="make out")
# print(response.json())


#
# import requests,json
# from requests.auth import HTTPBasicAuth
#
# consumer_key = "GC2WUo0oFPkUt4ARPbA37mtwGHN3vGAE"
# consumer_secret = "LVrZL1rvCMkAgjXG"
# api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
#
# r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
# access_token=json.loads(r.text)
# access_token =access_token.get("access_token")
# print (access_token)
#
#
#
#
#
# api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
# headers = {"Authorization": "Bearer %s" % access_token}
# request = { "BusinessShortCode": " " ,
#         "Password": " ",
#         "Timestamp": " ",
#         "CheckoutRequestID": " "
#   }
#
# response = requests.post(api_url, json = request, headers=headers)
#
# print (response.text)