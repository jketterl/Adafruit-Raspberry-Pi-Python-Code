class RGBDevice:
	def __init__(self, pwm, baseAddress):
		self.pwm = pwm
		self.baseAddress = baseAddress
		self.master = 1

	def setRGB(self, red, green, blue):
		self.pwm.setPWM(self.baseAddress + 1, 0, int(red * self.master))
		self.pwm.setPWM(self.baseAddress + 2, 0, int(green * self.master))
		self.pwm.setPWM(self.baseAddress + 0, 0, int(blue * self.master))
