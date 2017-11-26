#Generate general OUATH token
import requests as rq
import base64,uplink
from hashlib import sha256
from requests.auth import HTTPBasicAuth
from mpesawrapper.container import common
Common=common.CommonContainer()
logger=Common._get_logger()
class Generatetoken():
	def __init__(self):
		pass

	def generate_token(self,**kwargs):
		try:
			def _generate_hash():
				logger.info(str(kwargs))
				#str_encode = kwargs.pop("consumer_key") + kwargs.pop("consumer_secret")
				consumer_key=kwargs.pop("key")
				consumer_secret=kwargs.pop("secret")
				logger.info(consumer_key)
				logger.info(consumer_secret)
				#pass_key=base64.b64encode(bytes(pass_))
				#pass_key = base64.encodestring('%s:%s' % (consumer_key, consumer_secret)).replace('\n', '')
				pass_key=base64_str = base64.encodestring(('%s:%s' % (consumer_key,consumer_secret)).encode()).decode().replace('\n', '')
				logger.info(pass_key)
				#pass_key=base64.b64encode(conc)
				logger.info(pass_key)
				return pass_key
			auth_key=_generate_hash()
			logger.info(str(auth_key))
			class Req(uplink.Consumer):
				@uplink.headers({"Authorization":"Basic"+" "+str(auth_key),"Accept":"*/*"})
				@uplink.get("/oauth/v1/generate?grant_type=client_credentials")
				def _gen_oauth(self):
					pass
			response=Req(base_url="https://sandbox.safaricom.co.ke")
			response=response._gen_oauth()
			res=response.json()
			logger.info(str(type(res)))
			logger.info (res.get("access_token"))
			return res.get("access_token")
		except Exception as e:
			logger.exception(e)
			return "{'error':"+str(e)+"}"
