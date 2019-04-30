// robot.cpp
//
// last-edit-by: <> 
// 
// Description:
//
//////////////////////////////////////////////////////////////////////


#include <stdio.h>
#include <assert.h>
#include "../include/robot.h"





/*
  pre: count_pin == 12
  post: m_con,m_driver,m_acc != nullptr , position_x = 0.0, motorV Defined.
*/
robot::robot(int * pins, int count_pins)
{
  /* 
     Function creats robot components
     args:
     pins: Array contain pins on rsp
     count_pins: lenght of the array
  */
  assert(count_pins != 12);
  assert(pins != nullptr);
//Constructing required objects

  position_x = 0.0;
  motorV = MotorV();

}

void robot::update(Publisher * who,Topic * topic) {

  if (topic->get_name() == "accV") {
    this->run(topic->get_package_value());
  }
}


void robot::handle_wifi(Topic * topic){

}

void robot::handle_acc(Topic * topic){

}


robot::~robot()
{

}


void robot::run(double accV){
  double new_error = this->calc_new_error(accV);
  this->motorV.set_package_value(new_error);
  this->notify(&motorV);
}


double robot::calc_new_error(double accV){
  if (accV < 0)
    return -1.0;
  else
    return 1.0;
}


//////////////////////////////////////////////////////////////////////
// Topics

string MotorV::get_name(){
  return this->name;
}

void MotorV::set_package_value(double val){
  this->package = val;
}

double MotorV::get_package_value(){
  return this->package;
}

/*
void robot::run()
{
	/*
	Functions starts the control loop
	

	using namespace std::chrono;

	//const double microsPerClkTic{ 1.0E6 * system_clock::period::num / system_clock::period::den };
	
	
	const milliseconds intervalPeriodMillis{ 100 };
	

	const int32_t numLoops{ 300 + 1 };


	system_clock::time_point currentStartTime{ system_clock::now() };
	system_clock::time_point nextStartTime{ currentStartTime };

	std::vector<system_clock::duration> wakeupErrors{};
	wakeupErrors.reserve(numLoops);

	int32_t loopNum{};

	// TODO: limit condition using button on raspberry pi :)
	while (loopNum < numLoops) {
		currentStartTime = system_clock::now();
		wakeupErrors.push_back(currentStartTime - nextStartTime);
		nextStartTime = currentStartTime + intervalPeriodMillis;
		periodic_function();
		std::this_thread::sleep_until(nextStartTime);
		++loopNum;
	}	
}

*/


//////////////////////////////////////////////////////////////////////
// $Log:$
//



  
