import validators,urllib,json
import requests as uplink
from mpesawrapper.container import common
Common=common.CommonContainer()
logger=Common._get_logger()
class TransactionStatus():
	def __init__(self):
		pass
	def get_transaction_status(self,**kwargs):
		try:
			if kwargs is not  None:
					Initiator=kwargs.pop("Initiator")
					SecurityCredential=kwargs.pop("SecurityCredential")
					CommandID= kwargs.pop("CommandID")
					TransactionID=kwargs.pop("TransactionID")
					PartyA=kwargs.pop("PartyA")
					IdentifierType=kwargs.pop("IdentifierType")
					ResultURL=kwargs.pop("ResultURL")
					QueueTimeOutURL=kwargs.pop("QueueTimeOutURL")
					Remarks=kwargs.pop("Remarks")
					Occasion=kwargs.pop("Occasion")
					OriginalConversationID=kwargs.pop("OriginalConversationID")
					token=kwargs.pop("token")
					logger.info(Initiator)
			else:
				return "{'error':'Invalid args passed'}"
			if Initiator is None:
				return "{'error':'invalid Initiator'}"
			elif SecurityCredential is None:
				return "{'error':'invalid SecurityCredential'}"
			elif CommandID is None:
				return "{'error':'invalid CommandID'}"
			elif TransactionID is None:
				return "{'error':'invalid TransactionID'}"
			elif PartyA is None:
				return "{'error':'invalid PartyA'}"
			elif IdentifierType is None:
				return "{'error':'invalid IdentifierType'}"
			elif ResultURL is None:
				return "{'error':'invalid ResultURL'}"
			elif QueueTimeOutURL is None:
				return "{'error':'invalid QueueTimeOutURL'}"
			elif Remarks is None:
				return "{'error':'invalid Remarks'}"
			elif Occasion is None:
				return "{'error':'invalid Occasion'}"
			elif OriginalConversationID is None:
				return "{'error':'invalid OriginalConversationID'}"
			url_ = lambda base_url, query_string: base_url + query_string
			res = lambda url_, json_, headers_: uplink.post(url_, data=json_, headers=headers_).json()
			base_url = "https://sandbox.safaricom.co.ke"
			logger.info(base_url)
			query_string = "/mpesa/transactionstatus/v1/query"
			logger.info(query_string)
			url = url_(base_url, query_string)
			logger.info(url)
			body ={"Initiator": Initiator,"SecurityCredential":SecurityCredential,"CommandID": CommandID,"TransactionID":TransactionID,
			       "PartyA": PartyA,"IdentifierType":IdentifierType,"ResultURL":ResultURL,"QueueTimeOutURL":QueueTimeOutURL,
			       "Remarks":Remarks,"Occasion":Occasion,"OriginalConversationID":OriginalConversationID}
			logger.info(str(json.dumps(body)))
			response = res(url, json.dumps(body),
			               {"Content-Type": "application/json", "Authorization": "Bearer" + " " + token})
			logger.info("------------------------------------------------------------")
			logger.info(str(response))
			return str(response)
		except Exception as e:
			logger.exception(e)
			return "{'error':" + str(e) + "}"
