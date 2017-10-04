from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC030034f65df6c4bb5add05d6108d66bc"
# Your Auth Token from twilio.com/console
auth_token  = "49b309906852bbc77da055e7dffa356c"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17755614929", 
    from_="+19564460129",
    body="Hello from Python!")

print(message.sid)
