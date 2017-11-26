import validators,urllib,json,datetime
import requests as uplink
from mpesawrapper.container import common
Common=common.CommonContainer()
logger=Common._get_logger()
class Stkpush():
	def __init__(self):
		pass

	def invokemenu(self,**kwargs):
		try:
			BusinessShortCode=kwargs.pop("BusinessShortCode")
			Password=kwargs.pop("Password")
			Timestamp=kwargs.pop("Timestamp")
			TransactionType=kwargs.pop("TransactionType")
			Amount=kwargs.pop("Amount")
			PartyA=kwargs.pop("PartyA")
			PartyB=kwargs.pop("PartyB")
			PhoneNumber=kwargs.pop("PhoneNumber")
			CallBackURL=kwargs.pop("CallBackURL")
			AccountReference=kwargs.pop("AccountReference")
			TransactionDesc=kwargs.pop("TransactionDesc")
			token=kwargs.pop("token")

			logger.info(BusinessShortCode)
			logger.info(Password)
			logger.info(Timestamp)
			logger.info(Amount)
			logger.info(PartyA)
			logger.info(PartyB)
			logger.info(PhoneNumber)
			logger.info(CallBackURL)
			logger.info(AccountReference)
			logger.info(TransactionDesc)
			logger.info(token)
			def _validate_date():
				try:
					datetime.datetime.strptime(Timestamp, "%Y%m%d%H%M%S")
					return True
				except ValueError as e:
					logger.exception(e)
					return False

			if BusinessShortCode.__str__().__len__().__lt__ (3):
				logger.info("Invalid BusinessShortCode")
				return json.dumps({"error":"invalid BusinessShortCode"})
			if Password is None:
				logger.info("Invalid Password")
				return json.dumps({"error": "invalid password"})
			if Timestamp is None:
				logger.info("Invalid Timestamp")
				return json.dumps({"error": "invalid Timestamp"})
			elif _validate_date().__eq__(False):
				logger.info("Invalid timestamp")
				return json.dumps({"error":"Invalid Timestamp Format"})
			if TransactionType is None:
				logger.info("Invalid TransactioonTypr")
				return json.dumps({"error": "invalid TransactionType"})
			if Amount is None or Amount.__str__().__len__().__lt__ (0):
				logger.info("Invalid Amount")
				return json.dumps("Invalid Amount")
			if PartyA is None or PartyA.__str__().__len__().__lt__ (12) or PartyA.__str__().startswith("+"):
				logger.info("Invalid PartyA")
				return  json.dumps({"error":"Invalid PartyA "})
			if PartyB is None or PartyB.__str__().__len__().__lt__ (3) or PartyB.__str__().startswith("+"):
				logger.info("Invalid PartyB")
				return json.dumps({"error":"Invalid PartyB "})
			if PhoneNumber is None or PhoneNumber.__str__().__len__().__lt__ (12) or PhoneNumber.__str__().startswith("+"):
				logger.info("Invalid PhoneNumber")
				return json.dumps({"error": "Invalid PhoneNumber "})
			if CallBackURL is None:
				logger.info("Invalid CallbackUrl")
				return json.dumps({"error":"invalid CallBackURL"})
			if AccountReference is None:
				logger.info("Invalid AccountRef")
				return json.dumps({"error":"invalid AccountReference"})
			if TransactionDesc is None:
				logger.info("Invalid TransactionDesc")
				return json.dumps({"error":"Invalid TransactionDesc"})
			if token is None:
				logger.info("Invalid Token")
				return  json.dumps({"error":"Invalid Token"})
			logger.info("--------------------------------------")
			url_ = lambda base_url, query_string: base_url + query_string
			res = lambda url_, json_, headers_: uplink.post(url_, data=json_, headers=headers_).json()
			base_url = "https://sandbox.safaricom.co.ke"
			logger.info(base_url)
			query_string = "/mpesa/stkpush/v1/processrequest"
			logger.info(query_string)
			url = url_(base_url, query_string)
			logger.info(url)
			body = {"BusinessShortCode": BusinessShortCode,"Password": Password,"Timestamp": Timestamp,"TransactionType": "CustomerPayBillOnline",
			        "Amount": Amount,"PartyA": PartyA,"PartyB": PartyB,"PhoneNumber":PhoneNumber,"CallBackURL":CallBackURL,
			        "AccountReference":AccountReference,"TransactionDesc":TransactionDesc}
			logger.info(str(json.dumps(body)))
			logger.info("Bearer"+" "+str(token))
			response = res(url, json.dumps(body),
			               {"Content-Type": "application/json", "Authorization": "Bearer"+" "+token})
			logger.info("------------------------------------------------------------")
			logger.info(str(response))
			return str(response)
		except Exception as e:
			logger.exception(e)
			return "{'error':"+str(e)+"}"
	def query_request(self,**kwargs):
		try:
			if kwargs is not  None:
				BusinessShortCode=kwargs.pop("BusinessShortCode")
				Password=kwargs.pop("Password")
				Timestamp=kwargs.pop("Timestamp")
				CheckoutRequestID=kwargs.pop("CheckoutRequestID")
				token=kwargs.pop("token")
			if BusinessShortCode is None:
				return json.dumps({"error":"Invalid BusinessShortCode"})
			elif Password is None:
				return json.dumps({"error": "Invalid Password"})
			elif Timestamp is None:
				return json.dumps({"error": "Invalid Timestamp"})
			elif CheckoutRequestID is None:
				return json.dumps({"error": "Invalid CheckoutRequestID"})
			elif token is None:
				return json.dumps({"error": "Invalid token"})
			url_ = lambda base_url, query_string: base_url + query_string
			res = lambda url_, json_, headers_: uplink.post(url_, data=json_, headers=headers_).json()
			base_url = "https://sandbox.safaricom.co.ke"
			logger.info(base_url)
			query_string = "/mpesa/stkpushquery/v1/query"
			logger.info(query_string)
			url = url_(base_url, query_string)
			logger.info(url)
			body = {"BusinessShortCode":BusinessShortCode ,"Password":Password,"Timestamp":Timestamp,"CheckoutRequestID":CheckoutRequestID}
			logger.info(str(json.dumps(body)))
			logger.info("Bearer" + " " + str(token))
			response = res(url, json.dumps(body),
			               {"Content-Type": "application/json", "Authorization": "Bearer" + " " + token})
			logger.info("------------------------------------------------------------")
			logger.info(str(response))
			return str(response)
		except Exception as e:
			logger.exception(e)
			return "{'error':"+str(e)+"}"




