import time

class RGBDevice:
	def __init__(self, pwm, baseAddress):
		self.pwm = pwm
		self.baseAddress = baseAddress
		self.master = 1
		self.values = {'red':0, 'green':0, 'blue':0}
		self.setChannels(self.values)

	def setChannels(self, values):
		if 'red' in values: 
			self.pwm.setPWM(self.baseAddress + 1, 0, int(values['red'] * self.master))
			self.values['red'] = values['red']
		if 'green' in values:
			self.pwm.setPWM(self.baseAddress + 2, 0, int(values['green'] * self.master))
			self.values['green'] = values['green']
		if 'blue' in values:
			self.pwm.setPWM(self.baseAddress + 0, 0, int(values['blue'] * self.master))
			self.values['blue'] = values['blue']

	def fadeTo(self, values, stepSize = 1, sleep = .01):
		maxDelta = 0
		directions = {}
		for key in values:
			if not key in self.values: continue
			delta = values[key] - self.values[key]
			maxDelta = max(maxDelta, abs(delta))
			directions[key] = 1 if delta > 0 else -1
		for i in range(0, maxDelta / stepSize):
			iteration = {}
			for key in values:
				if (self.values[key] + stepSize * directions[key]) * directions[key] > values[key] * directions[key]:
					iteration[key] = values[key]
				else:
					iteration[key] = self.values[key] + stepSize * directions[key]
			self.setChannels(iteration)
			time.sleep(sleep)
		self.setChannels(values)
