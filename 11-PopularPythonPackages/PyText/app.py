from twilio.rest import Client

account_sid = "sid goes here"
auth_token = "token goes here"

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="+13369253142",
    from_="+18884345004",
    body="Hello, this is a test message!"
)

