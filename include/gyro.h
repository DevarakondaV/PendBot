#pragma once


//forawrd declared classes
class rasp;

class gyro
{
public:
	gyro(const rasp & m_rasp,int pin1,int pin2);
	double get_pendulum_angle();
	~gyro();
private:

	//private functions
	double calculate_angle(double vals);

	//raspberry interactor
	const rasp * m_rasp;

	//GPIO pins
	int gyro_pin1;
	int gyro_pin2;

	//other constants
	const double g = 9.81;	//gravity
};

