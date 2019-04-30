// wifi.h
//
// last-edit-by: <> 
//
// Description:
//
//////////////////////////////////////////////////////////////////////

#ifndef WIFI_H
#define WIFI_H 1


#include "../include/PubSub.h"
#include "../include/Topic.h"

class wifiV: public Topic
{
  wifiV() {};
  ~wifiV() {};
  string get_name();
  void set_package_value(double package);
  double get_package_value();
private:
  string name="wifiV";
  double package=0;
};
  

class wifi : public Publisher {
public:
  wifi(int pin1, int pin2);
  ~wifi();
  
private: 
};


#endif // WIFI_H
//////////////////////////////////////////////////////////////////////
// $Log:$
//




