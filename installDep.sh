#!/bin/bash

# Update Ubuntu
sudo apt-get -y update
sudo apt-get -y upgrade

# Install Dependencies
sudo apt-get install -y build-essential cmake pkg-config
sudo apt-get install -y libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev
sudo apt-get install -y libgtk-3-dev
sudo apt-get install -y libatlas-base-dev gfortran
sudo apt-get install -y python2.7-dev python3.5-dev

# Download the OpenCV source
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.2.0.zip
unzip opencv.zip

# Download the opencv_contrib source
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.2.0.zip
unzip opencv_contrib.zip

# Install pip
cd ~
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

# Install virtualenv and virtualenvwrapper
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip

# Edit ~/.bashrc file
echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc

mv opencv-3.2.0 OpenCV/
mv opencv_contrib-3.2.0 OpenCV/
cd OpenCV
mkdir build


