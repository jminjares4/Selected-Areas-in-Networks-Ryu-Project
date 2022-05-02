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
```python
class Layer2Switch(app_manager.RyuApp):
```
## Set the OpenFlow version
```python
OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
```
## Define class constructor
```python
def __init__(self, *args, **kwargs):
super(SimpleSwitch13, self).__init__(*args, **kwargs)
```
