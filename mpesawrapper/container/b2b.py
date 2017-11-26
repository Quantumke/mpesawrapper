import validators,urllib,json
import requests as uplink
from mpesawrapper.container import common
Common=common.CommonContainer()
logger=Common._get_logger()
class B2B():
	def __init__(self):
		pass
	def _b2b_request(self,**kwargs):
		try:
			if kwargs is not None:
				Initiator=kwargs.pop("Initiator")
				SecurityCredential=kwargs.pop("SecurityCredential")
				CommandID=kwargs.pop("CommandID")
				SenderIdentifierType=kwargs.pop("SenderIdentifierType")
				RecieverIdentifierType=kwargs.pop("RecieverIdentifierType")
				Amount=kwargs.pop("Amount")
				PartyA=kwargs.pop("PartyA")
				PartyB=kwargs.pop("PartyB")
				AccountReference=kwargs.pop("AccountReference")
				Remarks=kwargs.pop("Remarks")
				QueueTimeOutURL=kwargs.pop("QueueTimeOutURL")
				ResultURL=kwargs.pop("ResultURL")
				token=kwargs.pop("token")
			else:
				return "Error passing arguments"
			logger.info("------"+Initiator+"-------"+SecurityCredential+"-------"+CommandID+"-------"+SenderIdentifierType+"-------"+RecieverIdentifierType+"-------"+Amount+"-------"+PartyA+"-------"+PartyB+"-------"+AccountReference+"-------"+Remarks+"-------"+QueueTimeOutURL+"-------"+ResultURL+"-------")
			if Initiator is None:
				return {"error":"Missing Initiator"}
			elif SecurityCredential is None:
				return {"error": "Missing SecurityCredential"}
			elif CommandID is None:
				return {"error": "Missing CommandID"}
			elif SenderIdentifierType is None:
				return {"error": "Missing SenderIdentifierType"}
			elif PartyA is None:
				return {"error": "Missing PartyA"}
			elif PartyB is None:
				return {"error": "Missing PartyB"}
			elif AccountReference is None:
				return {"error": "Missing AccountReference"}
			elif Remarks is None:
				return {"error": "Missing Remarks"}
			elif QueueTimeOutURL is None:
				return {"error": "Missing QueueTimeOutURL"}
			elif ResultURL is None:
				return {"error": "Missing ResultURL"}
			url_ = lambda base_url, query_string: base_url + query_string
			res = lambda url_, json_, headers_: uplink.post(url_, data=json_, headers=headers_).json()
			base_url = "https://sandbox.safaricom.co.ke"
			logger.info(base_url)
			query_string = "/mpesa/b2b/v1/paymentrequest"
			logger.info(query_string)
			url = url_(base_url, query_string)
			logger.info(url)
			body = {"Initiator":Initiator,"SecurityCredential":SecurityCredential,"CommandID":CommandID, "SenderIdentifierType":SenderIdentifierType,
			        "RecieverIdentifierType":RecieverIdentifierType, "Amount":Amount,"PartyA":PartyA,"PartyB":PartyB,"AccountReference":AccountReference,
			        "Remarks":Remarks,"QueueTimeOutURL":QueueTimeOutURL,"ResultURL":ResultURL}
			logger.info(str(json.dumps(body)))
			response = res(url, json.dumps(body),
			               {"Content-Type": "application/json", "Authorization": "Bearer" + " " + token})
			logger.info("------------------------------------------------------------")
			logger.info(str(response))
			return str(response)

		except Exception as e:
			logger.exception(e)
			return "{'error':"+str(e)+"}"



