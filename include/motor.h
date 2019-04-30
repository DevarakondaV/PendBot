// motor.h
//
// last-edit-by: <> 
//
// Description:
//
//////////////////////////////////////////////////////////////////////

#ifndef MOTOR_H
#define MOTOR_H 1


#include <vector>
#include "../include/PubSub.h"
#include "../include/Topic.h"

//Forward declare classes



class motor : public Subscriber
{
public:
  motor(int pin1,int pin2,int pin3,int pin4);
  ~motor();
  void update(Publisher* who,Topic * topic = 0);
  
  //getters and setters
  void set_voltage(double new_voltage);
private:
  
  int CPin;
  int CCPin;
  int PWMPin;
  int EnPin;

  bool enabled;
  int direction; //1 for CW, 0 for CCW
   
 
};


#endif // MOTOR_H
//////////////////////////////////////////////////////////////////////
// $Log:$
//




