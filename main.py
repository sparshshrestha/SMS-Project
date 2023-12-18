# Importing all the required packages and python files
from flask import Flask, render_template
import os
from twilio.rest import Client
from space import space
from weather import weather
from hp import hp
import random

# Assigning secret keys
# This code only works for my replit
# You need to create your own secret keys from the API Keys for the code to work in your replit
# Create your Account SID and Auth Token at twilio.com/console
account_sid = os.environ['sid']
auth_token = os.environ['auth']

# Creating an app
app = Flask('app')


# Routing the app to the page
@app.route('/')
def hello_world():
    # Renders the index.html page
    return render_template("index.html")


# Routs the website to sms.html page
@app.route('/sms')
def sens_sms():
    # Setting environment variables
    # See http://twil.io/secure for more info
    client = Client(account_sid, auth_token)
    # Construct message from 3 APIS
    msg = f"Here are some facts for you:\n{space()}\n{weather()}\n{hp()}\n"
    # Send the message from twilio to my number
    # Since my twilio is a free account I can only send message to my phone number
    # To send the message to another number you need to purchace a paid membership
    message = client.messages \
                   .create(
                        body = msg, # Message
                        from_ = '+12059418391', # Twilio Number
                        to = '+17059884214' # My Number
                    )
    # This shows the message.sid to confirm that the message is sent to my number
    print(message.sid)

    # Saving the message in text file
    with open("static/files/sent_messages.txt", "a") as f:
        f.write(f"{msg}\n")

    # Renders the success.html page
    return render_template("success.html", msg=msg)


# Runs the website
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=random.randint(2000, 9000))
