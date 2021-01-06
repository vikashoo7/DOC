import paramiko

host='my-server'
port=22
user='<my-user>'
password='<my-password>'
s=paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
	s.connect(host, port, user, password)
	command='ls -l /tmp/'
	stdin, stdout, sterr = s.exec_command(command)
	status=stdout.channel.recv_exit_status()		##this is will check the status of the command
	out=stdout.read()					                  ##this will store the output value of the command
	if status == 0:
		print("\033[1;32;40m%s - File is listed \033[00m" %(host))
	else:
		print("\033[1;31;40m%s - The password less key is pushed Unsuccessfully\033[00m" %(host))
	s.close()
except Exception as e:
	print("%s not able to connect : %s" %(host, e))
