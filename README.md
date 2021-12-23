# CompSys_Facial_Recognition_Assignment

Run the following code from the client that you want to monitor the connected users on:

python3 client_pub.py mqqt://broker.emxq.io:1883/YOUR_ID_HERE/home

Run the following code in Putty with x11 enabled and XLaunch/XMing running on the host machine:

python3 client_sub.py mqqt://broker.emxq.io:1883/YOUR_ID_HERE/home

This will run facial_req.py as well as presence_detector.py in order to begin the facial
recogintion and scan the network for known users.
