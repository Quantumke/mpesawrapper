# mpesawrapper
## UNOFFICIAL DARAJA MPESA API

[READ THE DOCS](http://mpesawrapper.readthedocs.io/en/latest/)


## This is a support Library for the new MPESA API AT

https://developer.safaricom.co.ke/


This Library covers:
* OAUTH - Gives you time bound access token to call allowed APIs
* C2B -Register URL for Validation/Confirmation as an active listener for MPESA transactions on a shortcode.
* Lipa Na M-Pesa Online -  online payment using STK Push.
* B2B -  Mpesa Transaction from one company to another
* Transaction Status -Use this API to check the status of transaction
* Account Balance -Use this API for balance inquiry
* B2C -Mpesa Transaction from company to client
* REVERSAL  -API to reverse MPESA transaction


### Quick Reference


#### Installation

`pip install mpesawrapper`

1. CREATE OAUTH TOKEN

```python
    consumer_key="key from developer portal"
    consumer_secret="secret from developer portal"
	token=mpesawrapper.Generatetoken().generate_token(key=consumer_key,secret=consumer_secret)
```

2. C2B

- Register URL

```python
    token=token generated from CREATE OAUTH TOKEN
    reg_url=mpesawrapper.C2B().register_url(ValidationURL="",ConfirmationURL="",ResponseType="Completed",ShortCode="600147",token=token)
```

- C2B Simulate Transaction

```python
    transaction=mpesawrapper.C2B().c2b_transact(ShortCode="600147",CommandID="CustomerPayBillOnline",Amount=10,Msisdn=254708374149,BillRefNumber="019903023",token=token)
```

3. LIPA NA MPESA ONLINE

-Lipa Na M-Pesa Online Payment API

```python
    push=mpesawrapper.Stkpush().invokemenu(BusinessShortCode="174379",
		                     Password="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
		                     Timestamp="20130814100000",
		                     TransactionType= "CustomerPayBillOnline",
		                     Amount=10,
		                     PartyA= "254708374149",
		                     PartyB= "174379",
		                     PhoneNumber= "254708374149",
		                     CallBackURL= "",
		                     AccountReference= "",
		                     TransactionDesc= "TEST",
		                     token=token)
```

- Lipa Na M-Pesa Query Request API

```python
    response=mpesawrapper.Stkpush().query_request(BusinessShortCode="174379",Password="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",Timestamp="20130814100000",CheckoutRequestID="ws_co_123456789",token=token)
```

4. B2B

```python
    b2b=mpesawrapper.B2B()._b2b_request(
			Initiator = "testapi",
				SecurityCredential="Safaricom147",
				CommandID="BusinessPayBill",
				SenderIdentifierType="4",
				RecieverIdentifierType="4",
				Amount="10",
				PartyA="600147",
				PartyB="600000",
				AccountReference="2312333",
				Remarks="test rpc",
				QueueTimeOutURL="",
				ResultURL="",
				token=token
			)
```

5. Transaction Status

```python
    result=mpesawrapper.TransactionStatus().get_transaction_status(
			Initiator = "testapi",
				SecurityCredential = "Safaricom147!",
				CommandID="TransactionStatusQuery",
				TransactionID="LKQ61H3R9E",
				PartyA="600147",
				IdentifierType= "1",
				ResultURL="",
				QueueTimeOutURL="",
				Remarks="TEST",
				Occasion="TEST",
				OriginalConversationID="LKQ61H3R9E",
				token=token)
```

6. Query Balance

```python
    response=mpesawrapper.Balance().get_balance(
			Initiator="testapi",
				SecurityCredential="Safaricom147!",
				CommandID= "AccountBalance",
				PartyA="600147",
				IdentifierType="4",
				Remarks="bla",
				QueueTimeOutURL="",
				ResultURL="",
				token=token
			)
```

7. B2C

```python
    response=mpesawrapper.B2C().b2c_request(
			InitiatorName="testapi",
				SecurityCredential="Safaricom147!",
				CommandID="SalaryPayment",
				Amount="100",
				PartyA="600147",
				PartyB="254708374149",
				Remarks="testrpc",
				QueueTimeOutURL="",
				ResultURL="",
				Occassion="TEST",
				token=token
			)
```

8. REVERSAL

```python
    result=mpesawrapper.Reversal().reversal_request(
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
				token=token
			)
```