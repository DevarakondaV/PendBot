// acc.cpp
//
// last-edit-by: <> 
// 
// Description:
//
//////////////////////////////////////////////////////////////////////


#include <stdio.h>
#include <thread>
#include <chrono>
#include <vector>
#include "../include/acc.h"


acc::acc(int pin1,int pin2)
{
  /*
    Function creaats accscope interaction object
    
    args:
    m_rasp:		Reference to rasp interactor class
    pin1:	int. GPIO pin 1
    pin2:	int. GPIO pin 2
		
		
  */
  acc_pin1 = pin1;
  acc_pin2 = pin2;

  accV = AccV();
 
}

double acc::read_sensor()
{
  int sensor_vals = 1;
  return calculate_angle(0,0);
}


double acc::calculate_angle(double valx,double valy)
{
  /*
    Function calculates the angles according to vals
    
    arsg:
    vals:	acceleration values read from sensor
  */
  
  
  
  //atan approx
  double ratio = valx/valy;
  double atan_thetap = ratio-(ratio*ratio*ratio)/3.0;
  //acos approx
  ratio = valx/9.8;
  double acos_thetap = 3.1415/2.0-ratio-(ratio*ratio*ratio)/6.0; 
  //asin approx
  ratio = valy/9.8;
  double asin_thetap = ratio+(ratio*ratio*ratio)/6.0;

  double avg = (atan_thetap+acos_thetap+asin_thetap)/3.0;
  return avg;
}


acc::~acc(){
  
}

void acc::update(Publisher* who,Topic * topic){
  if (topic->get_name() == "deltaV"){
    this->read(topic->get_package_value());
  }
}


void acc::read(double deltaT){
  /*
    Function starts the control loop
  */

  using namespace std::chrono;

  const double microPerClkTic {
    1.0E6 * system_clock::period::num / system_clock::period::den
      };

  const milliseconds intervalPeriodMillis { deltaT };

  const int32_t numLoops { 300 + 1 };
  system_clock::time_point currentStartTime { system_clock::now() };
  system_clock::time_point nextStartTime { currentStartTime };

  std::vector<system_clock::duration> wakeupErrors {};
  wakeupErrors.reserve(numLoops);

  int32_t loopNum {};

  while (loopNum < numLoops) {
    currentStartTime = system_clock::now();
    wakeupErrors.push_back(currentStartTime-nextStartTime);
    nextStartTime = currentStartTime+intervalPeriodMillis;


    //Read sensors and notify subscribers
    double sensor_vals = this->read_sensor();
    double theta = this->calculate_angle(sensor_vals,sensor_vals);
    accV.set_package_value(theta);
    this->notify(&accV);

    std::this_thread::sleep_until(nextStartTime);
    ++loopNum;
  }
    
}

//////////////////////////////////////////////////////////////////////
// Topics

//AccV Topic
std::string AccV::get_name() { return this->name; };
void AccV::set_package_value(double package) { this->package = package; };
double AccV::get_package_value() { return this->package; };

//////////////////////////////////////////////////////////////////////
// $Log:$
//
