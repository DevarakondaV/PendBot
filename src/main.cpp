#include <iostream>
#include <ctime>
#include <unistd.h>


#include "../include/robot.h"
#include "../include/acc.h"
#include "../include/motor.h"
#include <wiringPi.h>

using namespace std;


void start_control_loop(acc accelerometer);

int main() {

  wiringPiSetup();
  //robot m_robot = robot();
  cout << "Hello world";


  //robot
  int pins[4] = {1,2,3,4};
  acc accelerometer = acc(1,2);
  motor motor_left = motor(3,4);
  motor motor_right = motor(5,6);
  robot Pendbot = robot(pins,4);
  MotorV left = MotorV();

  //accelerometer.subscribe(&Pendbot);
  
  Pendbot.subscribe(&motor_left);
  Pendbot.subscribe(&motor_right);

  Pendbot.notify(&left);
  
  
  
  return 0;
}



void start_control_loop(acc accelerometer) {

  //periodically runs loop in sample time
  int sleep_time = 500;
  while(true){

    usleep(sleep_time);
    accelerometer.read();
    //accelerometer.notify(accelerometer.get_thetap(),Pendbot);
  }
}

