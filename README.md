This was a fun project to help monitor stocks I was interested in. Utilizing Twilio's free trial account to set up a number to send our text as well as the yfinance module to monitor our selected stocks. 

To Do:
As it is the loop purposefully breaks after sending a single text. It would be great to have a single text be sent and then adjust the target numbers adjust so that it stops spamming/starts looking for the new target number. Ie: if Bynd hits 125, it sends a text, then it sets target to 127, etc.
