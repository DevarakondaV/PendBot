#include "gyro.h"
#include <math.h>


gyro::gyro(const rasp & m_rasp,int pin1,int pin2)
{
	/*
	Function creaats gyroscope interaction object
	
	args:
		m_rasp:		Reference to rasp interactor class
		pin1:	int. GPIO pin 1
		pin2:	int. GPIO pin 2

	
	*/

	this->m_rasp = &m_rasp;

	gyro_pin1 = pin1;
	gyro_pin2 = pin2;
}

double gyro::get_pendulum_angle()
{
	int sensor_vals = 1;
	return calculate_angle(sensor_vals);
}


double gyro::calculate_angle(double val)
{
	/*
	Function calculates the angles according to vals
	
	arsg:
		vals:	acceleration values read from sensor
	*/

	double thetap = acos(val / g);	//pendulum angle
	return thetap;
}


gyro::~gyro()
{
	delete m_rasp;
}


