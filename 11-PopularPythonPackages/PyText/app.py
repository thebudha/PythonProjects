from twilio.rest import Client

account_sid = "AC827aba8deda9d636172fb9f7cd38e3d8"
auth_token = "151a1856eec1947e380dee666853c870"

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="+13369253142",
    from_="+18884345004",
    body="Hello, this is a test message!"
)

