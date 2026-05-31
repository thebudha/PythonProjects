from twilio.rest import Client
import config


client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to="+13369253142",
    from_="+18884345004",
    body="Hello, this is a test message!"
)

