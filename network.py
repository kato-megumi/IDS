import subprocess
import time


def capture_traffic(interface):
	while True:
		file_name = "pcap/"+str(int(time.time()*1000))+".pcap"
		pcap_cmd = ["sudo","tcpdump", "-i", interface, "-s", "0", "-w",file_name ,"-c","5000"]
		# pcap_cmd = ["sudo","tcpdump", "-i", interface, "-s", "0", "-w","-" ,"-c","5000"]
		process = subprocess.Popen(pcap_cmd,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
		process.wait()