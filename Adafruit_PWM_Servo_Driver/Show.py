import time
import threading

pattern = [
        {'red':4095},
        {'red':0, 'green':4095},
        {'green':0, 'blue':4095},
        {'blue':0, 'red':4095},
        {'green':4095},
        {'red':0},
        {'blue':4095},
        {'green':0},
        {'red':4095},
        {'blue':0},
        {'green':4095, 'blue':4095},
        {'green':0},
        {'green':4095},
        {'blue':0},
        {'blue':4095},
        {'red':0},
        {'red':0, 'green':0, 'blue':0}
]

#while (True):


class Automatic(threading.Thread):
	def __init__(self, devices):
		self.doStop = False
		self.devices = devices
		threading.Thread.__init__(self)

	def setChannels(self, values):
		for device in self.devices:
			device.setChannels(values)

	def run(self):
		self.setChannels({'red':0,'blue':0,'green':0})
		while not self.doStop:
			for value in pattern:
				if not self.doStop:
					self.devices[0].fadeTo(value)
					time.sleep(1)
		self.setChannels({'red':0,'blue':0,'green':0})

	def stop(self):
		self.doStop = True
