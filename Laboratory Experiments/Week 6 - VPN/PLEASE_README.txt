Hello reader,
To configure the tunnel, you can take advantage of the shell scripts that is provided under the vpn directory. With no further thoughts, strictly follow these steps [This will complete 90% of task 2 with 100% triumph]:

NOTE: Head to the vpn directory on your local machine.

1) 
Convert the shell script to an executable on every VM with the aid of this command:
1. On the VPN Server:
	chmod +x setup_server_tunnel_vm.sh
2. On the VPN Client:
	chmod +x setup_client_tunnel_vm.sh
3. On Host V:
	chmod +x setup_host_tunnel_vm.sh

2)
On the VPN Server:
1. sudo ./vpnserver
2. Open a new terminal
3. setup_server_tunnel_vm.sh

3)
On the VPN Client:
1. sudo ./vpnclient <IP Address of the server>
2. Open a new terminal
3. setup_client_tunnel_vm.sh

4)
On Host V:
1. setup_host_tunnel_vm.sh

