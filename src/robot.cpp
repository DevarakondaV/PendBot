#include <stdio.h>
#include <assert.h>
#include "robot.h"




/*
  pre: count_pin == 12
  post: m_con,m_driver,m_acc != nullptr
*/
robot::robot(int * pins, int count_pins)
{
  /* 
     Function creats robot components
     args:
     pins: Array contain pins on rsp
     count_pins: lenght of the array
  */
  assert(
	//Constructing required objects
	
	

}

void robot::get_motor_voltage_inputs(double error,double & left_motor, double & right_motor)
{
	/*
	Function  gets left right wheel inputs according to controller
	args:
		left_wheel:		Reference double. Left wheel controller output
		right_wheel:	Reference double. Right wheel controller output

	returns:
		null
	*/

	auto voltage = robot_controller->calculate_input(error);
	left_motor = right_motor = voltage;
}

void robot::set_motor_voltage(double & left_motor, double & right_motor)
{
	motorL->set_voltage(left_motor);
	motorR->set_voltage(right_motor);
}

void robot::periodic_function()
{
	//Get error for controller input
	double error = calc_error();	//This function reads gyro for pendulum
	
	//get controller signal
	double input = robot_controller->calculate_input(error);
	
	//send controller signal to motors
	motorL->set_voltage(input);
	motorR->set_voltage(input);
}


robot::~robot()
{
  delete m_con,m_driver,m_acc;
}



void robot::run()
{
	/*
	Functions starts the control loop
	*/

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

void robot::start_cart_pend_simulation()
{

}

double robot::controller::calculate_input(double error)
{
	return 0.0;
}
