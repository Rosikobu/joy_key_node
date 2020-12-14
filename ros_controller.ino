#include <ros.h>
#include <std_msgs/Int8.h>

ros::NodeHandle nh;

void messageCb( const std_msgs::Int8& toggle_msg){
  if(toggle_msg.data == 0) 
  {
    digitalWrite(13, HIGH);    
  }
  if(toggle_msg.data == 1)
  {
    digitalWrite(13, LOW);     
  }
}

ros::Subscriber<std_msgs::Int8> sub("reader", &messageCb );

void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}