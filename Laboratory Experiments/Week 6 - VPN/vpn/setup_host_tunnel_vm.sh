ifconfig;
route -n;
sudo route add -net 10.0.2.0/24 enp0s3;
route -n;
ifconfig;