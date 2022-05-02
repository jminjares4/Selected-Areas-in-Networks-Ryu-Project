# Layer 2 with Ryu :dragon:

In order to create a Layer 2 switch in Ryu, we must get familiar of how to use its API. Ryu requires few generate packages for all its applications.

These are the general and useful packages: 
```python
from ryu.base import app_manager

from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls

from ryu.ofproto import ofproto_v1_3

from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
```
The packages list can be overwhelming, however the most importants ones are listed below with its description. 
|**Package** | **Description**|
| :---   | :---       |
| **app_manager** | main entry point for the application|
| **set_ev_cls**<br>**ofp_event**<br>**Dispatcher** | capture openflow event when openflow packets are received|
|**ofproto_v1_3** | OpenFlow version |
|**packet**<br>**ethernet**<br>**ether_types** | packet processing library|

## Create Class
When creating an ryu application class, always pass the `app_manager.RyuApp`.
```python
class Layer2Switch(app_manager.RyuApp): 
```

## Set the OpenFlow version
Set the OpenFlow version that the application will use.
```python
OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
```
## Define class constructor
For the constructor of the class, you must user `super` to inheritance Ryu properties.
```python
def __init__(self, *args, **kwargs):
super(SimpleSwitch13, self).__init__(*args, **kwargs)
```

## Add Events 
In a Ryu controller, you could add events that you would want to listen too. With the use of decocrators in python we can add functionality to the controller: `@set_ev_cls`. For instance, the code below will be trigger for any event at the OpenFlow switch. 
```python
 @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
def switch_features_handler(self, ev):
```
Next, we will add another event to listen to the packets that are being received. With the same functionality of the previous event, this `_packet_in_handler` function will be trigger once packets are being captured.
```python
@set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
def _packet_in_handler(self, ev):
```

## Run Ryu Application
This section will take in consideration that you know how to use, and run *Ryu* as well as *Mininet*. I will provide installation and getting started instructions.
* [Installation](../ryu_install/README.md)
* [Getting Started with Ryu](GettingStarted.md)

First, you must run the ryu application that hold the layer 2 switch.
```bash
ryu-manager layer2.py
```
However, we will still need a topology for the controller to have functionality. We would be using `Mininet` to create the different topologies to test.  

```bash
sudo mn mininet-topo/layer2.sh
```

## Topology
Run [topology](TopologyWithRyu.md) to generate graph. Here is the graph of the network in **layer2.sh** script.
<img src="../Topology-images/Layer%202%20Topology.png">


## **Author:**
* [**Jesus Minjares**](https://github.com/jminjares4)<br>
  * Master of Science in Computer Engineering<br>
[![Outlook](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white&style=flat)](mailto:jminjares4@miners.utep.edu) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat)](https://www.linkedin.com/in/jesus-minjares-157a21195/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&style=flat)](https://github.com/jminjares4)
