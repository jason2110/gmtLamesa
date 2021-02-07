# OTP project in Python

from twilio.rest import Client

import random

accountSSID = "AC084a0e764cd24608c3ef7552245195b2"
authToken = "4d7fc6cc9dce8420f6a006b53b8894be"
myClient = Client(accountSSID,authToken)

generateOTP = random.randint(100,999)
message = "Dear user your OTP is :" +str(generateOTP)

OTP = myClient.messages.create(
    from_= "+13178277061",
    body= message,
    to = "(+63) 9155517080"
)

print(OTP.sid)
print(message)
