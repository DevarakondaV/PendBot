#pragma once
#include <vector>

//Forward declare classes
class rasp;


class motor
{
public:
	motor(const rasp& m_rasp,int pin1,int pin2);
	~motor();

	//getters and setters
	double get_velocity() { return velocity; }
	void set_voltage(double new_voltage);

private:

	//private functions


	//raspberry interactor
	const rasp * m_rasp;

	//Changing params
	double voltage;
	double velocity;

	int rasp_pin1;
	int rasp_pin2;


	////Motor constant params
	//const float K = 0.58034283;			//Combination of motor constants
	//const float J = 0.12919318;			//Moment of inertia of rotor
	//const float L = 0.25841064;			//Electrical inductance
	//const float R = 0.13691642;			//Electrical resistance
	//const float b = 0.6356482;			//Motor viscous  friction constant
	//
	//// variables for wheel
	//// in metric units
	//const float wheel_diameter = .05;	
	//const float wheel_mass = .004;
	
};

