from twilio.rest import Client
import yfinance as yf

bynd = yf.Ticker("BYND")
cybr = yf.Ticker("CYBR")

account_sid = #aquire from Twilio account
auth_token = #aquire from Twilio account
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
                            from_=#aquire from Twilio account
                            to=#String of target cellphone number
                        )
        awake = False
    elif bynd.info['ask'] >=140.0:
        text_ask = bynd.info['ask']
        message = client.messages \
                        .create(
                            body=f'You should sell, BYND is at {text_ask}',
                            from_=#aquire from Twilio account
                            to=#String of target cellphone number
                        )
        awake = False
    elif cybr.info['ask'] <= 50.00:
        text_ask = cybr.info['ask']
        message = client.messages \
                        .create(
                            body=f'You should buy, CYBR is at {text_ask}',
                            from_=#aquire from Twilio account
                            to=#String of target cellphone number
                        )
        awake = False
    elif cybr.info['ask'] >=200.0:
        text_ask = cybr.info['ask']
        message = client.messages \
                        .create(
                            body=f'You should sell, CYBR is at {text_ask}',
                            from_=#aquire from Twilio account
                            to=#String of target cellphone number
                        )
        awake = False
    else:
        pass
print(bynd.info["ask"])
print(cybr.info["ask"])


