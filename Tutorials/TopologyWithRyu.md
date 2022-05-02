# Topology with Ryu :dragon:

Ryu has the functionality of creating graphs for the topology running in `Mininet`. This is quite useful as it will provide the visual representation of the network. Utilizing Ryu topology is easy and requires few steps. 

## How to use topology application
1) Run Ryu **gui_topology.py** 
    * `ryu run --observe-links ryu/app/gui_topology/gui_topology.py`
2) Have the mininet topology that you want to generate the graph
3) http://<ip_address of ryu controller>/8080

For instance, ryu controller with 127.0.0.1 ip address:
[http://127.0.0.1/8080](TopologyWithRyu.md)

## Script
```bash
chmod +x topology.sh
./topology.sh
```

## **Author:**
* [**Jesus Minjares**](https://github.com/jminjares4)<br>
  * Master of Science in Computer Engineering<br>
[![Outlook](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white&style=flat)](mailto:jminjares4@miners.utep.edu) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat)](https://www.linkedin.com/in/jesus-minjares-157a21195/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&style=flat)](https://github.com/jminjares4)
