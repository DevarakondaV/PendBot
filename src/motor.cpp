// motor.cpp
//
// last-edit-by: <> 
// 
// Description:
//
//////////////////////////////////////////////////////////////////////

#include <iostream>
#include "../include/motor.h"
#include <wiringPi.h>
#include <softPwm.h>

motor::motor(int pin1, int pin2,int pin3,int pin4){
  /*
    Motor constructor
    
    args:
    pin1:	GPIO Pin on rasp
    pin2:	GPIO Pin on rasp
  */


  this->CPin = pin1;
  this->CCPin  = pin2;
  this->PWMPin = pin3;
  this->EnPin = pin4;

  // Enabling pins
  pinMode(this->CPin,OUTPUT);
  pinMode(this->CCPin,OUTPUT);
  pinMode(this->EnPin,OUTPUT);
  if (!softPwnCreate(this->PWMPin,0,100)){
    cout << softPwn::errno;
  }

  //Other variables
  this->enabled = false;
}

motor::~motor()
{
	
}

void motor::update(Publisher* who,Topic * topic){
  /*
    Functions handles all the topics related to
    motor
  */
  
  std::string topic_name = topic->get_name();

  if (topic_name == "MotorV")
    this->set_voltage(topic->get_package_value());
    
}


void motor::set_voltage(double new_voltage)
{
  /* 
     Function sets new voltage and calculates the 
     new voltage
     
     args:
     new_voltage:	double. New voltage
     
     returns:
     null
     
  */

  //First Enable motor if not enabled
  if (!this->enabled){
    digitalWrite(this->EnPin);
    this->enabled = true;
    this->direction = 1; // By default always enabled CCW
  }


 //check direction  
  //CCW
  if (this->direction && new_voltage < 0){
    digitalWrite(this->CWPin,LOW);
    digitalWrite(this->CCWPin,HIGH);
    new_voltage *= -1;
    this->direction = 0;
  } else if ( ! this->direction && new_voltage > 0)  { //CW
    digitalWrite(this->CWPin,HIGH);
    digitalWrite(this->CCWPin,LOW);
    this->direction = 1 ;
  }  
	 

  softPwmWrite(this->PWMPin,new_voltage);
 
}







//////////////////////////////////////////////////////////////////////
// $Log:$
//


  

