// Topic.h
//
// last-edit-by: <> 
//
// Description:
//
//////////////////////////////////////////////////////////////////////

#ifndef TOPIC_H
#define TOPIC_H 1
#include <string>

using namespace std;


class Topic {
public:
  
  ~Topic(){};
  virtual string get_name() = 0;
  virtual void set_package_value(double val) = 0;
  virtual double get_package_value() = 0;

private:
};



#endif // TOPIC_H
//////////////////////////////////////////////////////////////////////
// $Log:$
//
