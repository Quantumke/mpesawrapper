from unittest import TestCase
import  mpesawrapper
class TestOauth(TestCase):

	# def test_generator(self):
	# 	str_=mpesawrapper.Generatetoken()
	# 	str_=str_.generate_token(key="GC2WUo0oFPkUt4ARPbA37mtwGHN3vGAE",te
	# 	                         secret="LVrZL1rvCMkAgjXG")
	# 	self.assertTrue(isinstance(str_, str))
	#
	# def test_c2b(self):
	# 	str_=mpesawrapper.C2b()
	# 	str_=str_.register_url(ValidationURL="https://a7c7fa84.ngrok.io/validate",ConfirmationURL="https://a7c7fa84.ngrok.io/confirm",ResponseType="Completed",ShortCode="600147",token="Br9RlmQE4TiAs3BYvHZGGHwjsZeo")
	# 	print (str_)
	# 	self.assertTrue(isinstance(str_, str))

	# def test_c2b_transaction(self):
	# 	str=mpesawrapper.C2b()
	# 	str_=str.c2b_transact(ShortCode="600147",CommandID="CustomerPayBillOnline",Amount=10,Msisdn=254708374149,BillRefNumber="019903023",token="Br9RlmQE4TiAs3BYvHZGGHwjsZeo")
	# 	self.assertTrue(isinstance(str_, type(str)))

	# def test_stk_push(self):
	# 	str_=mpesawrapper.Stkpush()
	# 	str_=str_.invokemenu(BusinessShortCode="174379",
	# 	                     Password="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
	# 	                     Timestamp="20130814100000",
	# 	                     TransactionType= "CustomerPayBillOnline",
	# 	                     Amount=10,
	# 	                     PartyA= "254708374149",
	# 	                     PartyB= "174379",
	# 	                     PhoneNumber= "254721799582",
	# 	                     CallBackURL= "https://eb86b9c4.ngrok.io/validate",
	# 	                     AccountReference= "LKA1233WE",
	# 	                     TransactionDesc= "TEST",
	# 	                     token="TtNATOwCBQAVgZrocfe5V7R02vT7")
	# 	self.assertTrue(isinstance(str_, type(str)))

	# def testb2b(self):
	# 	str=mpesawrapper.B2B()
	# 	str_=str._b2b_request(
	# 			Initiator = "testapi",
	# 			SecurityCredential="Safaricom147",
	# 			CommandID="BusinessPayBill",
	# 			SenderIdentifierType="4",
	# 			RecieverIdentifierType="4",
	# 			Amount="10",
	# 			PartyA="600147",
	# 			PartyB="600000",
	# 			AccountReference="2312333",
	# 			Remarks="test rpc",
	# 			QueueTimeOutURL="https://a7c7fa84.ngrok.io/confirm",
	# 			ResultURL="https://a7c7fa84.ngrok.io/validate",
	# 			token="Br9RlmQE4TiAs3BYvHZGGHwjsZeo"
	#
	# 	)
	# 	self.assertTrue(isinstance(str_, type(str)))
	# def test_transactionstatus(self):
	# 	str=mpesawrapper.TransactionStatus()
	# 	str_=str.get_transaction_status(
	# 			Initiator = "testapi",
	# 			SecurityCredential = "Safaricom147!",
	# 			CommandID="TransactionStatusQuery",
	# 			TransactionID="LKQ61H3R9E",
	# 			PartyA="600147",
	# 			IdentifierType= "1",
	# 			ResultURL="https://a7c7fa84.ngrok.io/confirm",
	# 			QueueTimeOutURL="https://a7c7fa84.ngrok.io/validate",
	# 			Remarks="Tetsrpc",
	# 			Occasion="micerat",
	# 			OriginalConversationID="LKQ61H3R9E",
	# 			token="SdrVHFTVEAwvJQDog6r1Ak4pLvD0")
	# 	self.assertTrue(isinstance(str_, type(str)))

	# def test_balance(self):
	# 	str=mpesawrapper.Balance()
	# 	str_=str.get_balance(
	# 			Initiator="testapi",
	# 			SecurityCredential="Safaricom147!",
	# 			CommandID= "AccountBalance",
	# 			PartyA="600147",
	# 			IdentifierType="4",
	# 			Remarks="bla",
	# 			QueueTimeOutURL="https://a7c7fa84.ngrok.io/confirm",
	# 			ResultURL="https://a7c7fa84.ngrok.io/validate",
	# 			token="ZSttJepEwM1UV7D5Tkt1yHs1ESPT")
	#
	# def test_b2c(self):
	# 	str=mpesawrapper.B2C()
	# 	str_=str.b2c_request(
	#
	# 			InitiatorName="testapi",
	# 			SecurityCredential="Safaricom147!",
	# 			CommandID="SalaryPayment",
	# 			Amount="100",
	# 			PartyA="600147",
	# 			PartyB="254708374149",
	# 			Remarks="testrpc",
	# 			QueueTimeOutURL="https://a7c7fa84.ngrok.io/confirm",
	# 			ResultURL="https://a7c7fa84.ngrok.io/validate",
	# 			Occassion="100",
	# 			token="SMbLZ8UgS7GhhPkMz11k9Iok4emE"
	#
	# 	)


	def test_reversal(self):
		str=mpesawrapper.Reversal()
		str_=str.reversal_request(
				Initiator="testapi",
				SecurityCredential="Safaricom147!",
				CommandID="TransactionReversal",
				TransactionID="LKQ61H3R9E",
				Amount="10",
				ReceiverParty="600147",
				RecieverIdentifierType= "4",
				ResultURL="https://a7c7fa84.ngrok.io/confirm",
				QueueTimeOutURL="https://a7c7fa84.ngrok.io/validate",
				Remarks="trytest",
				Occasion="100",
				token="6GtaGCGBl4rHb4CSG4TCTZ5GyPGi"

		)
		#self.assertTrue(isinstance(str_, type(str)))