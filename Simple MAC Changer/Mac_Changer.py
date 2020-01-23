import subprocess
import optparse

def get_argument():
  parser=optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface",help="Interface to Change if MAC")
	parser.add_option("-m","--mac",dest="new_mac",help="new mac address")
	(options,arguments)=parser.parse_args()
	if not options.interface:
		parser.error("[-] please specify the interface , --help for more info.")
	elif not options.new_mac:
		parser.error("[-] plase specify the new mac, --help for more info.")
	return options

def change_mac(interface,new_mac):
	print("[+] Changing mac address for"+ interface +" to " + new_mac)
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])

options=get_argument()
change_mac(options.interface,options.new_mac)
