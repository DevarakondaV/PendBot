#ifndef __ROBOT_H__
#define __ROBOT_H__



class mDriver;
class accelerometer;
class controller;


class robot
{
public:
  robot(int * pins,int count_pins);
  ~robot();


  void run();
  
  
private:

  /* Components of the robot */
  controller * m_con; // 0 pins
  mDriver * m_driver; // requires 6 pins
  accelerometer * m_acc; // requires 6 pins
  
    
};



#endif
  
#ifdef __TEST__

class rtest {

public:
 
private:
  
}
  

#endif
