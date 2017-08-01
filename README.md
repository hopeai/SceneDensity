# Simple Video Annotation Tool

This is a script to label the Scene in a Video based on the crowed density level. You can label the scene into 3 level, Empty, Half, and Full. In order to run this script we need to install OpenCV library on our system. Please follow the installation guide for your system.

# How to run script

We assume that you install OpenCV and are ready to run the script. In ordor to download click <a href="https://github.com/ImOmid/SceneDensity/archive/master.zip" target="_blank">here</a>. Unzip the file and navigate into SceneDensity directory. 

## In Ubuntu 16.04

Open the Terminal inside the SceneDensity directory, activate the virtual environment you by following command.

```sh
workon OpenCV
```

Use the following command to run the annotation tool. You will see an instruction about how to use this tool.

```sh
python annotate.py
```

## In Windows 10

Open command prompt and use the command below to run the tool.You will see an instruction about how to use this tool.

```sh
python annotate.py
```


# Install OpenCV on Ubuntu

## Install dependencies

Open Terminal and use the following commands

```sh
cd ~ && mkdir OpenCV && cd OpenCV && wget https://raw.githubusercontent.com/ImOmid/SceneDensity/master/installDep.sh
```
Now, you should be inside OpenCv directory. Use the following command to install dependencies.

```sh
bash ./installDep.sh
```

Please wait, it will take time. Afterwards, close the Terminal and open a new Terminal.

## Create your Python Virtual Environment using following commands.

For Python 2.7 use:

```sh
mkvirtualenv OpenCV -p python2
```

For Python 3.5 use:

```sh
mkvirtualenv OpenCV -p python3
```

Use the following command to change your Python environment into the virtual environment you just created.

```sh
workon OpenCV
```

## Install numpy in OpenCV virtual environment using following command.

```sh
pip install numpy
```

## Change the current working directory.

Use the following command to change the directory to build directory.

```sh
cd ~/OpenCV/build
```

## Configure the build

Use the following command to configure the build. Copy and paste it into the Terminal. Current working directory <b>must be build</b>.

```sh
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=~/OpenCV/opencv_contrib-3.2.0/modules \
    -D PYTHON_EXECUTABLE=~/.virtualenvs/OpenCV/bin/python \
    -D BUILD_EXAMPLES=ON ../opencv-3.2.0
```

<b>Be sure to check the output of CMake</b> before going to next step. You sould see an output in which cmake found the Interpreter, Libraries, numpy path for Python. The output is similar to YouTube Video on <a href="https://youtu.be/LneXUj7NBng?t=232" target="_blank">How to build and Install OpenCV 3.2 Python on Ubuntu 16.04.</a><br/>


## If there is no error in the previsous pass, use the following command to compile OpenCV.

```sh
make
```

<b>It can take up to 2 hours based on your Computer specifications. Be patient!</b>

If the compile finished without any error go to next step. Otherwise, use the following command to clean and make again.

```sh
make clean && make
```

## Install OpenCV

Use the below commands to install OpenCV

```sh
sudo make install
sudo ldconfig
```

## Finish OpenCV installation

Use the folllowing commands to build a symbolic link for OpenCV cv2.so.

For Python 2.7:
```sh
cd ~/.virtualenvs/OpenCV/lib/python2.7/site-packages/
ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so
```

For Python 3.5:
```sh
cd /usr/local/lib/python3.5/site-packages/
sudo mv cv2.cpython-35m-x86_64-linux-gnu.so cv2.so # Rename the file
cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so
```

## Test OpenCV install

If all the previous steps are done successfully. You should be able to import OpenCV in your virtual environment. Use the following commands to verify it.

### Open python inside OpenCV virtula environment.
```sh
cd ~
workon OpenCV
python
```

### In the python interpereter import cv2 and check its version.
```sh
import cv2
cv2.__version__
```

The output should be '3.2.0'




# Install OpenCV on Ubuntu 10 Windows


## Download and install dependencies

1. Download and install Visual Studio and CMake.

1.1. [Visual Studio 2012](http://go.microsoft.com/?linkid=9816768)<br/> 
1.2. [CMake](http://www.cmake.org/files/v2.8/cmake-2.8.11.2-win32-x86.exe)<br/>

2. Download and install necessary Python, and Numpy to their default locations.

2.1. [Python 2.7.x](https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi)<br/>
2.1. [Numpy](http://sourceforge.net/projects/numpy/files/NumPy/1.7.1/numpy-1.7.1-win32-superpack-python2.7.exe/download)<br/>


## Download and extract OpenCV and OpenCV_contrib

Download <a href="https://github.com/opencv/opencv/archive/master.zip" target="_blank">OpenCV</a><br/>

Download <a href="https://github.com/opencv/opencv_contrib/archive/master.zip" target="_blank">OpenCV_contrib</a><br/>

Extract both zip files into:
```sh
C:\OpenCV\sources\
```
and create a build directory in:
```sh
C:\OpenCV\
```


## Configure and Generate

Run CMake as administrator

### Configure OpenCV

#### Browse the source code and build directories as follows.

Where is the source code:
```sh
C:\OOpenCV\sources\opencv-master
```
Where to build the binaries
```sh
C:\OpenCV\build
```

#### Click Configure and specify native compilers. For C & C++ compilers browse following.
```sh
C:\Program Files (x86)\Microsoft Visual Studio 11.0\Vc\bin\cl.exe
```

#### Click Finish and wait until Configuring done. 

### Configure opencv_contrib

Look for OPENCV_EXTRA_MODULES_PATH and set it as follows.
```sh
C:\OpenCV\sources\opencv_contrib-master\modules
```
Then click Configure and wait until it is done.

### Generate

Click Generate and wait for it to finish. When it is done close CMake.

## Build OpenCV

1. Got to:

```sh
C:\OpenCV\build\
```
directory and run "OpenCV.sln" with Visual Studio.

2. Change the Debug mode to Release mode (you'll find it the middle of toolbar). Wait for the projects to get ready. Check if it is written Ready in the bottom left corner of the Visual Studio window.

3. When the projects are ready, Right Click on All_BUILD and select Build (you'll find in the solution explorer on the right of Visual Studio). It will take a while, wait until it finishes.

4. Right Click on INSTALL (right under ALL_BUILD) and select Build. When it finishes close the Visual Studio.

## Copy build files

### Copy cv2.pyc

#### Copy cv2.pyc file from: 
```sh
C:\OpenCV\sources\build\Release
```
into:
```sh
C:\Python27\Lib\site-packages\
```
If there is a file with the same name replace it.

### Copy *.dll files
Copy all the dll files from:
```sh
C:\OpenCV\sources\build\Release
```
into:
```sh
C:\Python27\
```

## Add Python and OpenCV into PATH

1. Right Click on My Computer and select properties.

2. Go to Advanced system settings (on top left corner) and select Environment Variables (on Advanced tab and at the bottom), and click on Path from the System variables section and click Edit.

3. Add all the following pathes by each time clicking on New
```sh
C:\Python27
C:\Python27\Lib\site-packages
C:\Python\Scripts
C:\OpenCV\build\lib\Release
C:\OpenCV\build\install\x86\vc11\bin
C:\OpenCV\build\install\x86\vc11\lib
```

4. Click OK on all setting windows you have opened.


## Test OpenCV

Open Command prompt and run the following commands.

1. Run python
```sh
python
```
2. Python interpreter must be run. To check if you installed OpenCV successfully import cv2 and check its version by following commands in Python interpreter.
```sh
import cv2
cv2.__version__
```
You should see '3.2.0'

You can watch the Video Tutorial on <a href="https://www.youtube.com/watch?v=w20YIlcpSi8" target="_blank">How to build and Install OpenCV 3.2 from source for Python on Windows 10</a>







