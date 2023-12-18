Requirements:
1. Syntax, spelling, grammar - Code works so no syntax errors
2. Comments are provided for all the codes
3. Both .zip format and link to my codes in replit.com will be provided
4. In Python, these APIs are connected: Harry Potter API https://hp-api.herokuapp.com/, OpenWeather API, OpenNotify and it sends out SMS through Twilio API
5. Using each of the three APIs, a message is constructed in a string in Python.
6. Sent the message using Twilio (I can only send to my own validated number using a free account)
7. Created a flask site with one button (send sms)
8. When you press the button, Python will call the 3 information APIs, construct the string, and send the SMS to my number
9. The message is flashed ina new webpage using jinja letting the user know the SMS was sent.
10. Messages are logged in to a text file in static/files/sent_messages.txt


This code will only work in my replit because I have used my secret key in the codes
If you fork the codes you need to create your own secret key for the code to run