from Adafruit_PWM_Servo_Driver import PWM

import alsaaudio
import struct, numpy, threading, time

input = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NORMAL, 'hw:1,0')
print input.cardname()
input.setformat(alsaaudio.PCM_FORMAT_S16_LE)
input.setrate(48000)
input.setchannels(2)
input.setperiodsize(1024)

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)

pwm.setPWMFreq(1600)                        # Set frequency to 600 Hz

data = None
l = 0

def readAudio():
	global data, l
	while True:
		l, data = input.read()

reader = threading.Thread(target=readAudio)
reader.start()

while True:
	#readAudio()
	#l, data = input.read()
	if l <= 0 : continue

	format = '<%dH' % (l * 2)
	data = numpy.array(struct.unpack(format, data), dtype='h')
	try:
		output = numpy.fft.fft(data, 10)
		freqs = numpy.fft.fftfreq(len(output)) * 48000

		ffty = numpy.abs(output[0:len(output)/2])/1000
		ret = []
		for val in ffty:
			ret.append(round(val, 3))
		
		for i, val in enumerate(ret):
			pwm.setPWM(i, 0, int(val * 10))

	except IndexError:
		pass
