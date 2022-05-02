# Getting Started with RYU :dragon:

## Ryu Overview
Ryu is a component-based software defined network (SDN) framework that is fully
developed in python. Ryu provides a well defined API’s easy for developers to create new network management and control applications.

## How to run a RYU Application
* Ryu is developed in python, therefore it was design to run with the same concept, instead of using python we would use ryu-manager. 
  * ryu-manager is the executable for Ryu applications. ryu-manager loads Ryu applications and run it.

`ryu-manager  <application file name>`

## Ryu Approach
* Ryu application are object-oriented, as it requires to always pass the ryu.app_manager base class to your application.