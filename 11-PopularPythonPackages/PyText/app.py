from twilio.rest import Client

account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="+13369253142",
    from_="+18884345004",
    body="Hello, this is a test message!"
)

