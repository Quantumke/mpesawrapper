import validators,urllib,json
import requests as uplink
from mpesawrapper.container import common
Common=common.CommonContainer()
logger=Common._get_logger()
class Reversal():
	def __init__(self):
		pass
	def  reversal_request(self,**kwargs):
		try:
			logger.info("hello")
			print ('------')
			if kwargs is not None:
				Initiator=kwargs.pop("Initiator")
				SecurityCredential=kwargs.pop("SecurityCredential")
				CommandID=kwargs.pop("CommandID")
				TransactionID=kwargs.pop("TransactionID")
				Amount=kwargs.pop("Amount")
				ReceiverParty=kwargs.pop("ReceiverParty")
				RecieverIdentifierType=kwargs.pop("RecieverIdentifierType")
				ResultURL=kwargs.pop("ResultURL")
				QueueTimeOutURL=kwargs.pop("QueueTimeOutURL")
				Remarks=kwargs.pop("Remarks")
				Occasion=kwargs.pop("Occasion")
				token=kwargs.pop("token")
				if not Initiator:
					return "{'error':'invalid initiator'}"
				elif SecurityCredential is None:
					return "{'error':'invalid SecurityCredential'}"
				elif CommandID is None:
					return "{'error':'invalid CommandID'}"
				elif TransactionID is None:
					return "{'error':'invalid TransactionID'}"
				elif Amount is None:
					return "{'error':'invalid Amount'}"
				elif ReceiverParty is None:
					return "{'error':'invalid ReceiverParty'}"
				elif ResultURL is None:
					return "{'error':'invalid ResultURL'}"
				elif QueueTimeOutURL is None:
					return "{'error':'invalid QueueTimeOutURL'}"
				elif Remarks is None:
					return "{'error':'invalid Remarks'}"
				elif Occasion is None:
					return "{'error':'invalid Occasion'}"
				elif token is None:
					return "{'error':'invalid token'}"
				url_ = lambda base_url, query_string: base_url + query_string
				res = lambda url_, json_, headers_: uplink.post(url_, data=json_, headers=headers_).json()
				base_url = "https://sandbox.safaricom.co.ke"
				logger.info(base_url)
				query_string = "/mpesa/reversal/v1/request"
				logger.info(query_string)
				url = url_(base_url, query_string)
				logger.info(url)
				body ={"Initiator":Initiator,"SecurityCredential":SecurityCredential,"CommandID":CommandID,"TransactionID":TransactionID,
				       "Amount":Amount,"ReceiverParty":ReceiverParty,"RecieverIdentifierType":RecieverIdentifierType,
				       "ResultURL":ResultURL,"QueueTimeOutURL":QueueTimeOutURL,"Remarks":Remarks,"Occasion":Occasion}
				logger.info(str(json.dumps(body)))
				response = res(url, json.dumps(body),
				               {"Content-Type": "application/json", "Authorization": "Bearer" + " " + token})
				logger.info("------------------------------------------------------------")
				logger.info(str(response))
				return str(response)
			else:
				logger.info("Invalid payload")
				print ("error")
		except Exception as e:
			logger.exception(e)
			return "{'error':" + str(e) + "}"