# joy_key_node
Very Basic ROS Node for Joy Xbox-Buttons to Arduino with small size that refuse accept large Twist Objects. LED-Blinking with A- and B-Buttons.

## 1) Install Xbox 360 Controller Driver
**1.1) install & config driver**
```
sudo apt-get install --install-recommends jstest* joystick xboxdrv
echo "backlist xpad" | sudo tee -a /etc/modprobe.d/blacklist.conf
```
**1.2) Start & Test your Joystick**
```
sudo xboxdrv --silent
jstest-gtk
```
Your joystick is available as js0, js1 or js2 etc.

![Running Xbox drv](/img/xbox_drv_joy.PNG "")

## 2) Install and run ROS Joy
**2.1) install Joy**
```
sudo apt-get install ros-melodic-joy
```
**2.1) Test your Controller (X = 0 or 1 or 2 etc)**
```
sudo jstest /dev/input/jsX
```
![Running xbox controller](/img/joy_test.PNG "")

**2.2) set permissions, rosparam (X = 0 or 1 or 2 etc) and run**
```
sudo chmod a+rw /dev/input/jsX
rosparam set joy_node/dev "/dev/input/jsX"
rosrun joy joy_node
```
## 3) Rosserial

**3.1) install Rosserial**

https://github.com/ros-drivers/rosserial

**3.2) set permissions for ttyACM0 and run**
```
sudo chmod 666 /dev/ttyACM0
rosrun rosserial_python serial_node.py /dev/ttyACM0
```

## 4) Arduino IDE & KeyReader Node
Load the ino-File in your IDE and rosrun joy_key_reader jkreader