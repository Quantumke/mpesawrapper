import validators,urllib,json
import requests as uplink
from mpesawrapper.container import common
Common=common.CommonContainer()
logger=Common._get_logger()
class Balance():
	def __init__(self):
		pass
	def get_balance(self,**kwargs):
		try:
			if kwargs is not None:
				Initiator=kwargs.pop("Initiator")
				SecurityCredential=kwargs.pop("SecurityCredential")
				CommandID=kwargs.pop("CommandID")
				PartyA=kwargs.pop("PartyA")
				IdentifierType=kwargs.pop("IdentifierType")
				Remarks=kwargs.pop("Remarks")
				QueueTimeOutURL=kwargs.pop("QueueTimeOutURL")
				ResultURL=kwargs.pop("ResultURL")
				token=kwargs.pop("token")
				if Initiator is None:
					return "{'error':'Invalid Initiator'}"
				elif SecurityCredential is None:
					return "{'error':'Invalid SecurityCredential'}"
				elif CommandID is None:
					return "{'error':'Invalid CommandID'}"
				elif PartyA is None:
					return "{'error':'Invalid PartyA'}"
				elif Remarks is None:
					return "{'error':'Invalid Remarks'}"
				elif QueueTimeOutURL is None:
					return "{'error':'Invalid QueueTimeOutURL'}"
				elif IdentifierType is None:
					return "{'error':'Invalid IdentifierType'}"
				elif ResultURL is None:
					return "{'error':'Invalid ResultURL'}"
				url_ = lambda base_url, query_string: base_url + query_string
				res = lambda url_, json_, headers_: uplink.post(url_, data=json_, headers=headers_).json()
				base_url = "https://sandbox.safaricom.co.ke"
				logger.info(base_url)
				query_string = "/mpesa/accountbalance/v1/query"
				logger.info(query_string)
				url = url_(base_url, query_string)
				logger.info(url)
				body = {"Initiator":Initiator,"SecurityCredential":SecurityCredential,"CommandID":CommandID,"PartyA":PartyA,
				         "IdentifierType":IdentifierType,"Remarks":Remarks,"QueueTimeOutURL":QueueTimeOutURL,"ResultURL": ResultURL}
				logger.info(str(json.dumps(body)))
				response = res(url, json.dumps(body),
				               {"Content-Type": "application/json", "Authorization": "Bearer" + " " + token})
				logger.info("------------------------------------------------------------")
				logger.info(str(response))
				return str(response)

		except Exception as e:
			logger.exception(e)
			return "{'error':" + str(e) + "}"
