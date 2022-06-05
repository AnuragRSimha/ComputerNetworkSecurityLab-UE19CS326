ifconfig;
sudo ifconfig tun0 192.168.53.5/24 up;
ifconfig;
route -n;
sudo route add 93.184.216.34 tun0;
route -n;