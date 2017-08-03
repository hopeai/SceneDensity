# Video Etiketleme Arayüzü

Video etiketleme arayüzünü kullanarak video sahnelerini yoğunluğa dayalı etikleye bilirsiniz. Arayüzü kullanarak sahneleri 3 yoğunluk seviyesinde etikleye bilirsiniz. Arayüzü bilgisayarınızda çalıştırmak için önce gereken kütüphaneleri kurmanız gerekiyor. OpenCV kütüphanesin kurmak için, aşağıda Windows ve Ubuntu işletim sistemleri için yazılmış kılavuza bakınız.

# Video Etiketleme Arayüzünü nasıl kullanırım

OpenCv kütüphanesini henüz kurmadıysanız işletim sisteminizle bağlı bölüme gidiniz, aksı takdirde devam ediniz. Video Etiketleme Arayüzü indirmek için <a href="https://github.com/ImOmid/SceneDensity/archive/tr.zip" target="_blank">tıklayın</a>. İndirilen dosyanı ziplemeden çıkarın ve  SceneDensity-tr klasörüne giriniz (annotate.py dosyanın olduğu klasörde olduğunuzdan emin olunuz).

## Windows işletim sistemi


Command prompt açınız ve 'cd' komutunu kullanarak SceneDensity-tr dosyasına giriniz.

Örneğim eğer SceneDensity-tr klasörü Downloads dosyasındaysa aşağıdakı komutu giriniz.

```sh
cd Dowsnloads\SceneDensity-tr 
```
Doğru dosyanın içinde olduğunuzda dir komutunu yazdığınızda aşağıdakı resimdeki gibi annotate.py ve diğer dosyaları göreceksiniz.

![](cmd.png?raw=true)

Şimdi arayüzü command prompt'da çalıştıra bilirsiniz.

## In Ubuntu 16.04

Terminal SceneDensity-tr klasörü içinde açınız, ve aşağıdakı komutu girerek sanal ortamı etkinleştiriniz. 

```sh
workon OpenCV
```

Şimdi arayüzü command prompt'da çalıştıra bilirsiniz.


# Arayüzü nasıl çalıştırırım

Arayüzü çalıştırmak için aşağıdakı komutu giriniz. Video sahnelerin nasıl etiketleyeceğinizi programın açıklamasında göreceksiniz.

```sh
python annotate.py
```



# Windows 10'da OpenCV nasıl kurulur


## Aşağıdakı programları indirip kurunuz.

1. Visual Studio ve CMake'i indirin ve kurunuz.

1.1. [Visual Studio 2012](http://go.microsoft.com/?linkid=9816768)<br/> 
1.2. [CMake](http://www.cmake.org/files/v2.8/cmake-2.8.11.2-win32-x86.exe)<br/>

2. Python ve Numpy'i indirip ve varsayılan adresleri değişmeden kurunuz.

2.1. [Python 2.7.x](https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi)<br/>
2.1. [Numpy](http://sourceforge.net/projects/numpy/files/NumPy/1.7.1/numpy-1.7.1-win32-superpack-python2.7.exe/download)<br/>


## OpenCV and OpenCV_contrib' indirip ve aşağıdakı klasöre unzip ediniz.

Download <a href="https://github.com/opencv/opencv/archive/master.zip" target="_blank">OpenCV</a><br/>

Download <a href="https://github.com/opencv/opencv_contrib/archive/master.zip" target="_blank">OpenCV_contrib</a><br/>

<b>Aşağıdakı klasöre unzip ediniz:</b>
```sh
C:\OpenCV\sources\
```
<b>ve aşağıdakı klasörde build ismiyle bir klasör açınız:</b>
```sh
C:\OpenCV\
```


## Configure ve Generate

CMake'i administrator olarak açınız (üzerinde sağ klik edip, Run as administrator seçiniz).

### Configure OpenCV

#### CMake'de aşağıdakı adresleri giriniz.

Where is the source code:
```sh
C:\OpenCV\sources\opencv-master
```
Where to build the binaries
```sh
C:\OpenCV\build
```

#### Configure'e basınız ve specify native compilers'de C & C++ compilers için aşağıdakı adresi giriniz.
```sh
C:\Program Files (x86)\Microsoft Visual Studio 11.0\Vc\bin\cl.exe
```

#### Finish'e basıp ve işlemin tamamlanmasını bekleyiniz. 

### Configure opencv_contrib

CMake'de 'OPENCV_EXTRA_MODULES_PATH' bulup ve aşağıdakı adresi giriniz.
```sh
C:\OpenCV\sources\opencv_contrib-master\modules
```
Configure'e basıp ve işlemin tamamlanmasını bekleyiniz.

### Generate

Generate'e basıp ve işlemin tamamlanmasını bekleyiniz. İşlem tamamlandıktan sonra CMake programın kapatınız.

## Build OpenCV

1. GAşağıdakı klasöre gidiniz:

```sh
C:\OpenCV\build\
```
"OpenCV.sln"i açınız.

2. Debug modunu Release olarak değişiniz (toolbar'ın ortasında bula bilirsiniz). Projelerin 'ready' olmasını bekleyiniz. Visual Studio penceresinin aşağısındakı mavı çizginin solunda 'ready' yazıldığından emin olup ve devam ediniz.

3. All_BUILD'ın üzerinde sağ klik yapıp Build'i seçiniz (ll_BUILD'i pencerenin sağında bula bilirsiniz). İşlemin tamamlanmasını bekleyiniz.

4. INSTALL'ın  üzerinde sağ klik yapıp Build'i seçiniz. İşlemin tamamlanmasını bekleyiniz ve sonra Visual Studio'nu kapatınız.


## Dosyaları kopyalayın

### cv2.pyc

#### cv2.pyc dosyasın aşağıdakı klasörden: 
```sh
C:\OpenCV\sources\build\Release
```
bu klasöre kopyalayın:
```sh
C:\Python27\Lib\site-packages\
```
Aynı isimle başka dosya varsa yenisiyle değiştiriniz.

### *.dll dosyaların kopyalama

Bütün dll dosyaların aşağıdakı klasörden:
```sh
C:\OpenCV\sources\build\Release
```
bu klasöre kopyalayın:
```sh
C:\Python27\
```

## Python ve OpenCV'yi PATH'e eklemek

1. My Computer üzerinde sağ klik yapıp ve properties'i seçiniz.

2. Advanced system settings'e gidiniz (sol üst köşede bula bilirsiniz), Environment Variables'i seçiniz, Path'i System variables bölümünden seçiniz ve Edit düğmesine basınız.

3. Aşağıdakı adreslerin hepsini tek tek 'New' düğmesini kullanarak ekleyin.
```sh
C:\Python27
C:\Python27\Lib\site-packages
C:\Python\Scripts
C:\OpenCV\build\lib\Release
C:\OpenCV\build\install\x86\vc11\bin
C:\OpenCV\build\install\x86\vc11\lib
```

4. Açtık olan bütün pencerelerde Ok düğmesine basınız.


## OpenCV'nin doğru kurulup mu

Command prompt'ı açıp ve aşağıdakı komutları girerek test ediniz'

1. python'u çalıştırın
```sh
python
```
2. Aşağıdakı komutları python ortamında giriniz.
```sh
import cv2
cv2.__version__
```
OpenCV doğru kurumuşsa hatasız çalışacaktır komutlar ve ekranda OpenCV'nin versiyoun '3.2.0' olarak göreceksiniz.

Kurulum işlemin videodan takip etmek için tıklayın. <a href="https://www.youtube.com/watch?v=w20YIlcpSi8" target="_blank">How to build and Install OpenCV 3.2 from source for Python on Windows 10</a>



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









