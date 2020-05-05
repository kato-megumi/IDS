import threading
import pickle
import subprocess
import pandas as pd
import sklearn
import time
from utils import *
import sys
import os

from network import capture_traffic
from evaluator import Evaluator

class IDS(object):
	"""docstring for IDS"""
	def __init__(self, interface):
		super(IDS, self).__init__()
		self.interface = interface

	
	def start(self):
		evaluator = Evaluator()
		evaluator.load_model()
		run = threading.Thread(target=capture_traffic, args=(self.interface,))
		run.start()
		while True:
			pcap_list = os.listdir("pcap")
			while len(pcap_list) < 2:
				time.sleep(0.5)
				pcap_list = os.listdir("pcap")
			pcap = "pcap/"+str(min([int(fname[:-5]) for fname in pcap_list]))+'.pcap'
			evaluator.evaluate_traffic(pcap)


def main():
	if len(sys.argv) < 2:
		ids = IDS("vboxnet0")
	else:
		ids = IDS(sys.argv[1])

	try:
		os.mkdir("log") 
		os.mkdir("pcap") 
	except:
		pass

	ids.start()

if __name__ == '__main__':
	main()