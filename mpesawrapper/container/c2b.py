import validators,urllib,json
import requests as uplink
from mpesawrapper.container import common
Common=common.CommonContainer()
logger=Common._get_logger()
class C2B():
	def __init__(self):
		pass
	def register_url(self,**kwargs):
		try:
			ValidationURL=kwargs.pop("ValidationURL")
			ConfirmationURL=kwargs.pop("ConfirmationURL")
			ResponseType=kwargs.pop("ResponseType")
			ShortCode=kwargs.pop("ShortCode")
			token=kwargs.pop("token")
			logger.info(ValidationURL)
			logger.info(ConfirmationURL)
			logger.info(ResponseType)
			logger.info(ShortCode)
			logger.info("validate validation url")
			test_validation_url=validators.url(ValidationURL)
			if test_validation_url==True:
				assert test_validation_url==True
			else:
				return {
					"error":"please add a valid validation url"
				}
			test_confirmation_url=validators.url(ConfirmationURL)
			if test_confirmation_url==True:
				assert test_confirmation_url==True
			else:
				return {
					"error":"please add a confirmation url"
				}
			if ResponseType=="Completed" or ResponseType=="Cancel":
				assert ResponseType=="Completed" or ResponseType=="Cancel"
			else:
				return  {
					"error":"please change response type to `Cancel` or `Complete`"
				}
			url_=lambda base_url,query_string:base_url+query_string
			res = lambda url_, json_,headers_: uplink.post(url_, data=json_,headers=headers_).json()
			base_url="https://sandbox.safaricom.co.ke"
			query_string="/mpesa/c2b/v1/registerurl"
			url=url_(base_url,query_string)
			body={"ShortCode": ShortCode ,"ResponseType":ResponseType,"ConfirmationURL":ConfirmationURL,"ValidationURL": ValidationURL}
			logger.info(str(json.dumps(body)))
			response=res(url,json.dumps(body),
			    {"Content-Type":"application/json","Authorization":"Bearer"+" "+token})
			logger.info("------------------------------------------------------------")
			logger.info(str(response))
			return  str(response)
		except Exception as e:
			logger.exception(e)
	def c2b_transact(self,**kwargs):
		try:
			ShortCode = kwargs.pop("ShortCode")
			CommandID = kwargs.pop("CommandID")
			Amount = kwargs.pop("Amount")
			Msisdn = kwargs.pop("Msisdn")
			BillRefNumber = kwargs.pop("BillRefNumber")
			token = kwargs.pop("token")
			logger.info("-----------"+ShortCode+"-----------"+CommandID+"-----------"+str(Amount)+"-----------"+str(Msisdn)+"-----------"+BillRefNumber+"-----------------")
			if ShortCode is None:
				assert ShortCode is None
				logger.info("ShortCode Invalid")
				return {"error":"Invalid shortcode"}
			if CommandID is None:
				assert ShortCode is None
				logger.info("invalid CommandID")
				return {"error":"Invalid CommandID"}
			if Amount is None:
				assert Amount is None
				logger.info("Invalid Amount")
				return  {"error":"Invalid Amount"}
			if Msisdn is None:
				assert Msisdn is None
				logger.info("Msisdn is blank")
				return {"error":"Invalid Msisdn"}
			elif Msisdn.__str__().__len__().__lt__ (12):
				logger.info(Msisdn.__str__().__len__())
				logger.info("Invalid Msisdn length ")
				return {"error":"Invalid Msisdn Length"}
			elif str(Msisdn).startswith("+"):
				logger.info("Msisdn strarts with +")
				return {"error":"Invalid Msisdn -remove + sign"}
			if BillRefNumber is None or BillRefNumber.__str__().__len__() >20:
				logger.info("Invalid BillRefNumber")
				return {"error":"Invalid BillRefNumber"}
			logger.info("--------------------------------------")
			url_ = lambda base_url, query_string: base_url + query_string
			res = lambda url_, json_, headers_: uplink.post(url_, data=json_, headers=headers_).json()
			base_url = "https://sandbox.safaricom.co.ke"
			logger.info(base_url)
			query_string = "/mpesa/c2b/v1/simulate"
			logger.info(query_string)
			url = url_(base_url, query_string)
			logger.info(url)
			body = {"ShortCode":ShortCode,"CommandID": CommandID,"Amount":int(Amount),"Msisdn":int(Msisdn),"BillRefNumber":BillRefNumber}
			logger.info(str(json.dumps(body)))
			response = res(url, json.dumps(body),
			               {"Content-Type": "application/json", "Authorization": "Bearer" + " " + token})
			logger.info("------------------------------------------------------------")
			logger.info(str(response))
			return str(response)

		except Exception as e:
			logger.exception(e)
			return "{'error':" + str(e) + "}"


