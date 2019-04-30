// acc.h
//
// last-edit-by: <> 
//
// Description:
//
//////////////////////////////////////////////////////////////////////

#ifndef ACC_H
#define ACC_H 1


#include "../include/PubSub.h"
#include "../include/Topic.h"


class AccV : public Topic
{
public:
  AccV() {};
  ~AccV() {};
  string get_name();
  void set_package_value(double package);
  double get_package_value();
private:
  string name="AccV";
  double package = 0;
};

class acc : public Publisher
{
public:
  acc(int pin1,int pin2);
  void update(Publisher * who,Topic * topic);
  void read(double deltaT);
  double read_sensor();
  ~acc();
  
private:
  
  //private functions
  double calculate_angle(double valx, double valy);
  
  //GPIO pins
  int acc_pin1;
  int acc_pin2;

  
  AccV accV;
  //other constants
  const double g = 9.81;	//gravity
};




#endif // ACC_H
//////////////////////////////////////////////////////////////////////
// $Log:$
//




