import time

class RGBDevice:
	def __init__(self, pwm, baseAddress):
		self.pwm = pwm
		self.baseAddress = baseAddress
		self.master = 1
		# mapping of channel names against PWM channels
		self.channelMap = {
			'red'   : self.baseAddress + 1,
			'green' : self.baseAddress + 2,
			'blue'  : self.baseAddress + 0
		}
		# reset to 0
		self.values = {'red':0, 'green':0, 'blue':0}
		self.setChannels(self.values)

	def setChannels(self, values):
		for color in values:
			if not color in self.channelMap: continue
			self.pwm.setPWM(self.channelMap[color], 0, self.lightnessCorrect(int(values[color] * self.master)))
			self.values[color] = values[color]

	def lightnessCorrect(self, value):
		return int(round(4095.0 * (value / 4095.0) ** 2.2))

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
