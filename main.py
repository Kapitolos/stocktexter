from twilio.rest import Client
import yfinance as yf

bynd = yf.Ticker("BYND")
cybr = yf.Ticker("CYBR")

account_sid = 'AC404d4e4f5dd3733f949ae699aaaa2be8'
auth_token = '74248d741671d27911db25db6dd3e2b2'
client = Client(account_sid, auth_token)
awake = True
print(bynd.info["ask"])
print(cybr.info["ask"])

while awake == True:
    if bynd.info['ask'] <= 125.00:
        text_ask = bynd.info['ask']
        message = client.messages \
                        .create(
                            body=f'You should buy, BYND is at {text_ask}',
                            from_='+19382010470',
                            to='+16477038664'
                        )
        awake = False
    elif bynd.info['ask'] >=140.0:
        text_ask = bynd.info['ask']
        message = client.messages \
                        .create(
                            body=f'You should sell, BYND is at {text_ask}',
                            from_='+19382010470',
                            to='+16477038664'
                        )
        awake = False
    elif cybr.info['ask'] <= 50.00:
        text_ask = cybr.info['ask']
        message = client.messages \
                        .create(
                            body=f'You should buy, CYBR is at {text_ask}',
                            from_='+19382010470',
                            to='+16477038664'
                        )
        awake = False
    elif cybr.info['ask'] >=200.0:
        text_ask = cybr.info['ask']
        message = client.messages \
                        .create(
                            body=f'You should sell, CYBR is at {text_ask}',
                            from_='+19382010470',
                            to='+16477038664'
                        )
        awake = False
    else:
        pass
print(bynd.info["ask"])
print(cybr.info["ask"])


