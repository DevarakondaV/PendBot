#ifndef __PUBSUB__
#define __PUBSUB__



#include <list>
using namespace std;
class Publisher;
class Topic;

class Subscriber {
 public:
  virtual ~Subscriber() {};
  virtual void update(Publisher* who,Topic * what = 0) = 0;
};


class Publisher {
 public:
  Publisher() {notifyEnabled = true;}
  virtual ~Publisher() {}
  void subscribe(Subscriber* s) {subscribers.push_back(s);}
  void unsubscribe(Subscriber* s) {subscribers.remove(s);}
  void notify(Topic* what = 0,Subscriber *s = 0);
  void setNotifyEnabled(bool flag) {notifyEnabled = flag;}
  bool getNotifyEnabled() const { return notifyEnabled;}

 private:
  list<Subscriber*> subscribers;
  bool notifyEnabled;
};




#endif
