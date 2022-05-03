# Layer 3 with Ryu :dragon:
Due to Ryu API, it allows to create simple and easy application with few changes from previous application. For instance, in order to create a Layer 3 switch change some application in layer2.py software. The difference between a Layer 2  and Layer 3 switch is 


|Layer 2 (L2) | Layer 3 (L3)|
| :---   | :---   |
|Operate on layer 2 (Data link) of OSI model. |	Operate on layer 3 (Network Layer) of OSI model.|
|Send “frames” to destination on the basis of MAC address.|Route Packet with help of IP address|
|Work with MAC address only	| Can perform functioning of both 2 layer and 3 layer switch|
|Used to reduce traffic on local network.	| Mostly Used to implement VLAN (Virtual Local area network)|
|Quite fast as they do not look at the Layer 3 portion of the data packets.	| Takes time to examine data packets before sending them to their destination|
|It has single broadcast domain	| It has multiple broadcast domain.|
| Can communicate within a network only. |	Can communicate within or outside network.|
* [Reference](https://www.geeksforgeeks.org/difference-between-layer-2-and-layer-3-switches/)


Creating application with Ryu is interesting as there are developed in software using python. Here are the instruction in creating and understanding Ryu Applications: 

* [Creating Applications With Ryu](CreatingApplicationWithRyu.md)

## Import packages
As previously mention in the table, L2 and L3 difference is the way it uses mac address and ip address to do its routing. Therefore, we have to import `ipv4` package to be able to use packets ip address in the switch.
```python
from ryu.lib.packet import ipv4 # New package
```

## Check IP instead of ETH
Add the flow section of code in `_packet_in_handler(self,ev):` event handler. 
```python
 # check IP Protocol and create a match for IP
if eth.ethertype == ether_types.ETH_TYPE_IP:
  ip = pkt.get_protocol(ipv4.ipv4)
  srcip = ip.src
  dstip = ip.dst
  match = parser.OFPMatch(eth_type=ether_types.ETH_TYPE_IP,
                          ipv4_src=srcip,
                          ipv4_dst=dstip
                          )
  # verify if we have a valid buffer_id, if yes avoid to send both
  # flow_mod & packet_out
  if msg.buffer_id != ofproto.OFP_NO_BUFFER:
      self.add_flow(datapath, 1, match, actions, msg.buffer_id)
      return
  else:
      self.add_flow(datapath, 1, match, actions)
```

## **Author:**
* [**Jesus Minjares**](https://github.com/jminjares4)<br>
  * Master of Science in Computer Engineering<br>
[![Outlook](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white&style=flat)](mailto:jminjares4@miners.utep.edu) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat)](https://www.linkedin.com/in/jesus-minjares-157a21195/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&style=flat)](https://github.com/jminjares4)
