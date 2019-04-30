// robot.h
//
// last-edit-by: <> 
//
// Description:
//
//////////////////////////////////////////////////////////////////////

#ifndef ROBOT_H
#define ROBOT_H 1


#include "PubSub.h"
#include "Topic.h"

class MotorV : public Topic
{
public:
  MotorV(){};
  ~MotorV(){};
  string get_name();
  void set_package_value(double package);
  double get_package_value();
private:
  string name = "MotorV";
  double package = 0;
};



class robot : public Publisher, public Subscriber
{
public:
  robot(int * pins,int count_pins);
  ~robot();
  void update(Publisher* who,Topic * topic = 0);

  void run(double accV);
  double calc_new_error(double accV);

  void handle_wifi(Topic * topic);
  void handle_acc(Topic * topic);  
  
private:
  
  double position_x;
  MotorV motorV;

};


#endif // ROBOT_H
//////////////////////////////////////////////////////////////////////
// $Log:$
//








#ifdef __TEST__

class rtest {

public:
 
private:
  
}
  

#endif
