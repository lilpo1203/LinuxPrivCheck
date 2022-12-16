#!/usr/bin/python3
import subprocess as sub


print("FINDING PRIVESC VECTORS WITH PO !!!!!")

def user_id():
	print("\n ++++++ User Info Checking ++++++")
	cmd = "id"
	return sub.run(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True, text=True)

def kernel_checking():
	print("\n ++++++ Kernel Checking ++++++")
	cmd = "uname -a"
	return sub.run(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True, text=True)

def sudo_right():
	print("\n ++++++ Sudo Right Checking ++++++")
	cmd = "sudo -ln"
	return sub.run(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True, text=True)


def suid_checking():
	print("\n ++++++ SUID Checking ++++++")
	cmd = "find / -perm -u=s -type f 2>/dev/null"
	a = sub.run(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True, text=True)
	x = a.stdout.split("\n")
	print("All SUID Executable Binaries")
	print(a.stdout)
	print('\n')
	print('\n')
	print('\n')
	print('Highly Vulnerable SUID Executable Binaries')
	default_suid = ['/usr/lib/openssh/ssh-keysign', '/usr/lib/xorg/Xorg.wrap', '/usr/lib/dbus-1.0/dbus-daemon-launch-helper', '/usr/bin/kismet_cap_nrf_mousejack', '/usr/bin/chfn', '/usr/bin/vmware-user-suid-wrapper', '/usr/bin/kismet_cap_linux_wifi', '/usr/bin/umount', '/usr/bin/pkexec', '/usr/bin/kismet_cap_nrf_52840', '/usr/bin/ntfs-3g', '/usr/bin/kismet_cap_ubertooth_one', '/usr/bin/gpasswd', '/usr/bin/kismet_cap_nxp_kw41z', '/usr/bin/kismet_cap_rz_killerbee', '/usr/bin/newuidmap', '/usr/bin/sudo', '/usr/bin/newgidmap', '/usr/bin/chsh', '/usr/bin/passwd', '/usr/bin/kismet_cap_ti_cc_2540', '/usr/bin/su', '/usr/bin/kismet_cap_nrf_51822', '/usr/bin/fusermount3', '/usr/bin/kismet_cap_ti_cc_2531', '/usr/bin/newgrp', '/usr/bin/kismet_cap_linux_bluetooth', '/usr/bin/mount', '/usr/sbin/mount.nfs', '/usr/sbin/mount.cifs', '/usr/sbin/pppd', '/usr/libexec/lxc/lxc-user-nic', '/usr/libexec/polkit-agent-helper-1']
	for i in range(0,len(x)):
		if x[i] not in default_suid:
			print(x[i])


def crontab_check():
	print("\n ++++++ Crontab Checking ++++++")
	cmd = "cat /etc/crontab"
	return sub.run(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True, text=True)


def capabilities_check():
	print("\n ++++++ Capabilities Checking ++++++")
	cmd = "getcap -r / 2>/dev/null"
	return sub.run(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True, text=True)


def NFS_check():
	print("\n ++++++ NFS Checking ++++++")
	cmd = "cat /etc/exports"
	return sub.run(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True, text=True)


def rootproc_checking():
	print("\n ++++++ Root Process Checking ++++++")
	cmd = "ps -aux | grep root"
	return sub.run(cmd, stdout=sub.PIPE, stderr=sub.PIPE, shell=True, text=True)

if __name__ == '__main__':

	### User id checking
	user_info = user_id()
	print(user_info.stdout)


	### Kernel Checking
	print(kernel_checking().stdout)


	### Sudo Right Checking
	a = sudo_right()
	print(a.stderr)
	print(a.stdout)


	### SUID checking
	suid_info = suid_checking()


	### Crontab checking
	print(crontab_check().stdout)


	### Capabilities Checking
	print(capabilities_check().stdout)


	### NFS Checking
	print(NFS_check().stdout)


	### Root Process Checking
	print(rootproc_checking().stdout)







