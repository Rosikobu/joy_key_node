#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8
from std_msgs.msg import Empty
from sensor_msgs.msg import Joy

def callback(data):

    a_pressed = Int8(0) # A-Button
    b_pressed = Int8(1) # B-Button

    # Example with Empty-data
    #empy = Empty()
    #if(data.buttons[0]==1):
    #    pub.publish(empty)

    if(data.buttons[0]==1):
        pub.publish(a_pressed)
    elif(data.buttons[1]==1):
        pub.publish(b_pressed)


def jk_reader():

    global pub
    # Example with Empty-Data
    #pub = rospy.Publisher('reader', Empty, queue_size=10)
    pub = rospy.Publisher('reader', Int8, queue_size=10)

    rospy.Subscriber("joy", Joy, callback)

    rospy.init_node('keyreader', anonymous=True)
    rospy.spin()

if __name__ == '__main__':
    try:
        jk_reader()
    except rospy.ROSInterruptException:
        pass
