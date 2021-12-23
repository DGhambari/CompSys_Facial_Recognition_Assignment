#!/bin/bash

# Name: Darren Ghambari
# Student ID: 20095580

#!/bin/sh
apt-get install sense-hat -y
apt-get install python-picamera python3-picamera -y
apt-get install build-essential cmake pkg-config -y
apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev -y
apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
apt-get install libxvidcore-dev libx264-dev -y
apt-get install libfontconfig1-dev libcairo2-dev -y
apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev -y
apt-get install libgtk2.0-dev libgtk-3-dev -y
apt-get install libatlas-base-dev gfortran -y
apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103 -y
apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5 -y
apt-get install python3-dev -y
wget https://bootstrap.pypa.io/get-pip.py -y
python get-pip.py -y
python3 get-pip.py -y
rm -rf ~/.cache/pip -y
pip install virtualenv virtualenvwrapper -y
