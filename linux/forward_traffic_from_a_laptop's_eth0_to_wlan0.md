Forward traffic from a laptop's eth0 to wlan0
=============================================


###To laptop

Specify an IP address to eth0 (here 192.168.56.1)

    sudo ifconfig eth0 192.168.56.1 netmask 255.255.255.0

Enable IP forwarding

    sudo sysctl -w net.ipv4.ip_forward=1

Forward packets from eth0 to wlan0

    sudo iptables -A FORWARD --in-interface eth0 -j ACCEPT
    sudo iptables --table nat -A POSTROUTING --out-interface wlan0 -j MASQUERADE

###To device connected to laptop

Setup IP address for eth0,and add gateway
 
    sudo ifconfig eth0 192.168.56.2 netmask 255.255.255.0
    sudo route add default gw 192.168.56.1