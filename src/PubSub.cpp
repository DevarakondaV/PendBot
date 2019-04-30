#include "../include/PubSub.h"
#include "../include/Topic.h"


/*
Function notifies subscriber
*/
void Publisher::notify(Topic* topic, Subscriber *s) {
  if (notifyEnabled){
    list<Subscriber*>::iterator p;
    for(p = subscribers.begin(); p != subscribers.end(); p++)
      if (*p != s) (*p)->update(this,topic);
  }
  notifyEnabled = true;
}
