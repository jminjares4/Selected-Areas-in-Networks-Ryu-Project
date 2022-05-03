# Layer 2 with Ryu :dragon:

In order to create a Layer 2 switch in Ryu, we must get familiar of how to use its API. Ryu requires few generate packages for all its applications.

Creating application with Ryu is interesting as there are developed in software using python. Here are the instruction in creating and understanding Ryu Applications: 

* [Creating Applications With Ryu](CreatingApplicationWithRyu.md)

## Creating Layer 2 Switch
1) Create Layer 2 Class
```python
class Layer2Switch(app_manager.RyuApp):
```
2) Intialize constructor
```python
def __init__(self, *args, **kwargs):
    super(Layer2Switch, self).__init__(*args, **kwargs)
```
3) Add events
* Capture switch events
```python 
@set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
```
* Capture packets events
```python
@set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
def _packet_in_handler(self, ev):      
```
1) Add flows
```python
def add_flow(self, datapath, priority, match, actions, buffer_id=None):
```
2) Run Ryu application
```bash
ryu-manager layer2.py
```

## Topology
Run [topology](TopologyWithRyu.md) to generate graph. Here is the graph of the network in **layer2.sh** script.

![alt text](https://github.com/jminjares4/Selected-Areas-in-Networks-Ryu-Project/blob/main/Topology-images/Layer%202%20Topology.png)


## **Author:**
* [**Jesus Minjares**](https://github.com/jminjares4)<br>
  * Master of Science in Computer Engineering<br>
[![Outlook](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white&style=flat)](mailto:jminjares4@miners.utep.edu) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat)](https://www.linkedin.com/in/jesus-minjares-157a21195/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&style=flat)](https://github.com/jminjares4)
