ifconfig;
sudo ifconfig tun0 192.168.53.1/24 up;
sudo sysctl net.ipv4.ip_forward=1;
ifconfig;
sudo iptables -F;
sudo iptables -t nat -F;
sudo iptables -t nat -A POSTROUTING -j MASQUERADE -o enp0s3;