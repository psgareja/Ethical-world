import subprocess
import optparse
import re

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
def get_current_mac(interface):
	ifconfig_result=subprocess.check_output(["ifconfig",interface])
	print(ifconfig_result)
	mac_address_search_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("[-] Could not read MAC address")

options=get_argument()
current_mac=get_current_mac(options.interface)
print("current mac : "+str(current_mac))

change_mac(options.interface,options.new_mac)
current_mac=get_current_mac(options.interface)
if current_mac==options.new_mac:
	print("[+] mac address successfuly changed to "+ current_mac)
else:
	print("[-] mac did not get changed")
