import threading
import pickle
import subprocess
import pandas as pd
import sklearn
import time
from utils import *
import sys
import os

class Evaluator(object):
	"""docstring for Evaluator"""
	def __init__(self):
		super(Evaluator, self).__init__()
		

	def load_model(self):
		with open('model', 'rb') as f:
			self.model = pickle.load(f)

	def evaluate_traffic(self,file):
		print("start eval "+file)
		process = subprocess.Popen(["./kdd99extractor",file], stdout=subprocess.PIPE)
		stdout = process.communicate()[0]
		if len(stdout) == 0:
			print(file)
			exit()
		out = [line.split(',') for line in stdout.decode('utf-8').split('\n')[:-1]]
		traffic = pd.DataFrame(out,columns=allow)[select]

		result = self.model['classifier'].predict(
					self.model["scaler"].transform(
						self.model["preprocessor"].transform(traffic)))

		print("done eval "+file)

		timestamp = file[5:-5]
		log_file = "log/"+timestamp+".log"

		self.log(log_file,result)

		#remove pcap file
		subprocess.Popen(["sudo","rm",file]).wait()

	def log(self,log_file,result):
		with open(log_file,'w') as f:
			f.write(str(result))

if __name__ == '__main__':
		
	e = Evaluator()
	e.load_model()
	e.evaluate_traffic("pcap/1588686965506.pcap")