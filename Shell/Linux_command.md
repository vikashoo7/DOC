sending email:
  -------
       #mail -s "Test Subject" my_emailid@email.com
       body of the mail. (ctrl+d)
       
       ######Sending Email with the specific sender
       #echo "This is the main body of the mail" | mail -s "Subject of the Email" -S  from=some@mail.tld  sender@mail.com

check the remote port is open or not
-------
      #echo > /dev/tcp/server_ip/port_no
      #nc -zv server_name port_number
      
      ######To check the remote host port active or not
      #nc -w 5 172.24.230.247  25

- Extending the xfs file system
------
    #xfs_growfs /mount/point -D size       ##Where: -D option allow us to give the filesystem extnsion. if no -D option will be there then it will extend to the maximum size.
 
- Scan disk
------
    #for i in /sys/class/scsi_host/*; do echo "- - -"> $i/scan; done

- SAR  command
------
    #sar -r  -f /var/log/sa/sa09 -s 12:00:00 -e 12:50:00   
 
- Finding a file with a specific size
------
    #find /etc -size +100k
    #find / -xdev -size +100M -exec ls -alh {} \; | sort -rn -k 5        //it will be in more readable format


- Find the largest  top 10 file 
------
    #du -a /var | sort -n -r | head -n 10
    #du -hsx * | sort -rh | head                  //this is more readable  format


- Finding the size of each directory
------
    #du -sh *
  
- File system extension
------
    #lvresize --resizefs --size +50GB /dev/RootVG/lv_mylvm                       #use in rhel 6
 

  
- df –h output
------
    #df -h  | egrep '/opt|/app' | rev | awk '{ print $1 $2 $3 $4 $5 }' |rev
 
- running  script remotely by passing the argument.
------
    #ssh -q myserver.com 'cat | bash /dev/stdin /myValue '  < chklist.sh

- Changing the password without input ( Changing the password using echo )
    * echo "linuxpassword" | passwd --stdin linuxuser
  
- Finding the port name(WWPN)  for the Physical Server
    * #cat /sys/class/scsi_host/host*/device/fc_host/host*/port_name      or 
    * #systool -c fc_host -v | grep "port_name"

- Clearing the mailq 
    * postsuper -d ALL
  
- How to increse the size of  "tmpfs"
    * #df -h
    * #vi /etc/fstab
    * tmpfs                   /dev/shm                tmpfs   defaults,size=48G        0 0
    * remount the "/dev/shm "
    * #mount -o remount /dev/shm
  
- How to list all  process that  is swapping.
    * #for file in /proc/*/status ; do awk '/VmSwap|Name/{printf $2 " " $3}END{ print ""}' $file; done | sort -k 2 -n -r | less
 
- Deleting tons of file at a time
    * #find . -type f -print –delete
 
- Finding the rpm for a particular file
    * #repoquery --whatprovides '*bin/grep'
    * #yum whatprovides '*bin/grep'
 
- Command to check the output of the 3 hand shake using tcpdump
    * #tcpdump -n -i eth0 src host 10.10.10.10 or dst host  20.20.20.20
    * #tcpdump -n -i eth0 src host 10.10.10.10 or dst host  20.20.20.20
 
- Caputing the packet in the file:
    * #tcpdump -s0 -i eth0 host Distination_IP -w  /tmp/filname.pcap
    * Note: eth0 is the source IP address.
    * #tcpdump -w port.pcap -s 1550 -i bond0 host 10.10.10.10 and host 20.20.20.20
    * #tcpdump -w port.pcap -s 1550 -i bond0:1 host 10.10.10.10 and host 20.20.20.20
 
- Command for sync the time to the ntp server
    * #systemctl stop ntpd
    * #systemctl status ntpd
    * #ntpdate ntp.myserver.com
    * #systemctl start ntpd
    * #date
    * #systemctl status ntpd
 
- How to add the crontab which runs  at the end of the month
    * 55 23 28-31 * * [[ "$(date --date=tomorrow +\%d)" == "01" ]] && myjob.sh
 
- Changing the MTU value 1400 for the interface.
    * #ifconfig bond0 mtu 1400 
    * #ifconfig eth0 mtu 1400 
    * #ifconfig eth4 mtu 1400 
    * #ifconfig bond0:1 mtu 1400 
    * #ifconfig bond0:2 mtu 1400

- See the Content of the Initramfs
    * #lsinitrd initramfs-3.10.0-862.3.2.el7.x86_64.img

- Rebuilding the initrd image
    * #dracut /tmp/3.10.0-862.3.2.el7.x86_64.img 3.10.0-862.3.2.el7.x86_64

- Checking for the disk status in the dell
  #/opt/dell/srvadmin/bin/omreport storage pdisk controller=0 

- This command show the raid level
    * #omreport storage vdisk controller=0 

- udev setting
  * [root@myserver ~]# cat /etc/udev/rules.d/12-dm-permissions.rules  | egrep -v "^#|^$"
    ACTION!="add|change", GOTO="dm_end"
    ENV{DM_UDEV_RULES_VSN}!="?*", GOTO="dm_end"
    ENV{DM_VG_NAME}=="dataGroup", ENV{DM_LV_NAME}=="lv*", OWNER:="user", GROUP:="mygroup", MODE:="660"
    ENV{DM_VG_NAME}=="dataGroup", ENV{DM_LV_NAME}=="lv*", OWNER:="user", GROUP:="mygroup", MODE:="660"
    LABEL="dm_end"
  [root@myserver ~]#
  [root@myserver ~]# udevadm control --reload-rule
  [root@myserver ~]# udevadm trigger --action=change
  
- VMWAREF BALLOON
    * #/sbin/modprobe -r vmware_balloon   ##for RHEL6
    * #/sbin/modprobe -r vmw_balloon    ##for RHEL7
  
- To unlock the user
    * #faillock --user oracle --reset

- To insert a line before the last ($) one:
    * #sed '$i<pattern>!' filename

- Create the file using dd command
   * dd if=/dev/zero of=output.dat  bs=1024  count=100000  ##create 100M file
