#include "motor.h"
#include "rasp.h"


motor::motor(const rasp& m_rasp, int pin1,int pin2)
{
	/*
	Motor constructor

	args:
		pin1:	GPIO Pin on rasp
		pin2:	GPIO Pin on rasp
	*/
	voltage = 0;
	velocity = 0;
	rasp_pin1 = pin1;
	rasp_pin2 = pin2;
	this->m_rasp = & m_rasp;
}


motor::~motor()
{
	delete m_rasp;
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
	voltage = new_voltage;
	const int count_pins = 2;
	int pins[count_pins] = { rasp_pin1, rasp_pin2 };
	m_rasp->set_voltage_on_pins(pins, count_pins,new_voltage);
}

