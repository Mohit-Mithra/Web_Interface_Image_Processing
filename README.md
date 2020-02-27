# Web_Interface_IP

## Setup Instructions

## Install
1. Follow [this](https://vitux.com/install-python3-on-ubuntu-and-set-up-a-virtual-programming-environment/) to install Python3
2. pip3 install django
3. pip3 install numpy
4. pip3 install matplotlib
5. pip3 install scipy
6. pip3 install opencv-python
7. pip3 install PeakUtils
8. pip3 install Pillow

## Modifications

In Web_Interface_Image_Processing/Web_Interface_IP/SIH/img_processing/views.py ,

change the path in line 36 inside os.chdir()

from 

os.chdir(r'/home/mohit/Web_Interface_Image_Processing/Web_Interface_IP/SIH/img_processing')

to 

os.chdir(r'..appropriate_path_in_your_machine.../Web_Interface_Image_Processing/Web_Interface_IP/SIH/img_processing')

where appropriate_path_in_your_machine is the location where the repository is cloned.


## Running the server

Run *python3 manage.py runserver* in the project root folder (Web_Interface_IP/SIH/ directory)
Then visit 127.0.0.1:8000/

