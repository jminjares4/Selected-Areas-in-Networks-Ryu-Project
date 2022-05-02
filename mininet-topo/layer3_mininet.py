# Author: Jesus Minjares

# Import Mininet modules
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

# Instantiate Mininet
net = Mininet()

# Create hosts, switches, remote controller, and links between hosts and switches.
h1 = net.addHost('h1', mac='00:00:00:00:00:01', ip='192.168.1.11/24')
h2 = net.addHost('h2', mac='00:00:00:00:00:02', ip='192.168.1.12/24')
h3 = net.addHost('h3', mac='00:00:00:00:00:03', ip='192.168.2.13/24')
h4 = net.addHost('h4', mac='00:00:00:00:00:04', ip='192.168.2.14/24')

# Add switches
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')

# Add remote controller
net.addController('c0', controller=RemoteController)

# Link all components
# Link H1 -> S1
net.addLink('h1', 's1')
# Link H2 -> S1
net.addLink('h2', 's1')
# Link H3 -> S2
net.addLink('h3', 's2')
# Link H4 -> S2
net.addLink('h4', 's2')
# Link S1 -> S3
net.addLink('s1', 's3')
# Link S2 -> S3
net.addLink('s2', 's3')

# Start mininet network
net.start()

# Set gateway ip_address and mac_address
# H1 configuration
h1.cmd("ip route add default via 192.168.1.1")
h1.cmd("arp -s 192.168.1.1 00:00:00:01:01:00")
h1.cmd("arp -s 192.168.1.12 00:00:00:00:00:02")

# H2 configuration
h2.cmd("ip route add default via 192.168.1.1")
h2.cmd("arp -s 192.168.1.1 00:00:00:01:01:00")
h2.cmd("arp -s 192.168.1.11 00:00:00:00:00:01")

# H3 configuration
h3.cmd("ip route add default via 192.168.2.1")
h3.cmd("arp -s 192.168.2.1 00:00:00:02:02:00")
h3.cmd("arp -s 192.168.2.14 00:00:00:00:00:04")

# H4 configuration
h4.cmd("ip route add default via 192.168.2.1")
h4.cmd("arp -s 192.168.2.1 00:00:00:02:02:00")
h4.cmd("arp -s 192.168.2.13 00:00:00:00:00:03")

# Initialize CLI
CLI( net )

# Stop mininet network
net.stop()