import validators,urllib,json
import requests as uplink
from mpesawrapper.container import common
Common=common.CommonContainer()
logger=Common._get_logger()
class B2C():
	def __init__(self):
		pass
	def b2c_request(self,**kwargs):
		try:
			if kwargs is not None:
				InitiatorName=kwargs.pop("InitiatorName")
				SecurityCredential=kwargs.pop("SecurityCredential")
				CommandID=kwargs.pop("CommandID")
				Amount=kwargs.pop("Amount")
				PartyA=kwargs.pop("PartyA")
				PartyB=kwargs.pop("PartyB")
				Remarks=kwargs.pop("Remarks")
				QueueTimeOutURL=kwargs.pop("QueueTimeOutURL")
				ResultURL=kwargs.pop("ResultURL")
				Occassion=kwargs.pop("Occassion")
				token=kwargs.pop("token")
				if InitiatorName is None:
					return "{'error':'invalid intiator name'}"
				elif SecurityCredential is None:
					return "{'error':'invalid SecurityCredential'}"
				elif CommandID is None:
					return "{'error':'invalid CommandID'}"
				elif Amount is None:
					return "{'error':'invalid Amount'}"
				elif PartyA is None:
					return "{'error':'invalid PartyA'}"
				elif PartyB is None:
					return "{'error':'invalid PartyB'}"
				elif Remarks is None:
					return "{'error':'invalid Remarks'}"
				elif QueueTimeOutURL is None:
					return "{'error':'invalid QueueTimeOutURL'}"
				elif ResultURL is None:
					return "{'error':'invalid ResultURL'}"
				elif Occassion is None:
					return "{'error':'invalid Occassion'}"
				url_ = lambda base_url, query_string: base_url + query_string
				res = lambda url_, json_, headers_: uplink.post(url_, data=json_, headers=headers_).json()
				base_url = "https://sandbox.safaricom.co.ke"
				logger.info(base_url)
				query_string = "/mpesa/b2c/v1/paymentrequest"
				logger.info(query_string)
				url = url_(base_url, query_string)
				logger.info(url)
				body ={"InitiatorName":InitiatorName,"SecurityCredential":SecurityCredential,"CommandID":CommandID,
				       "Amount":Amount,"PartyA":PartyA,"PartyB":PartyB,"Remarks":Remarks,"QueueTimeOutURL":QueueTimeOutURL ,
				       "ResultURL":ResultURL,"Occassion":Occassion}
				logger.info(str(json.dumps(body)))
				response = res(url, json.dumps(body),
				               {"Content-Type": "application/json", "Authorization": "Bearer" + " " + token})
				logger.info("------------------------------------------------------------")
				logger.info(str(response))
				return str(response)
		except Exception as e:
			logger.exception(e)
			return "{'error':" + str(e) + "}"

