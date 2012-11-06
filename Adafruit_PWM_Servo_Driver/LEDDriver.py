#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
from RGBDevice import RGBDevice
import tornado.ioloop
import tornado.web
import tornado.websocket
import json
from Show import Automatic

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)

pwm.setPWMFreq(1600)                        # Set frequency to 600 Hz

devices = [
	RGBDevice(pwm, 0),
	RGBDevice(pwm, 3)
]

automatic = None

class LEDWebSocket(tornado.websocket.WebSocketHandler):
	def open(self):
		pass
	def on_message(self, message):
		val = json.loads(str(message))
		if 'auto' in val:
			if val['auto']:
				global automatic
				if automatic is not None and automatic.isAlive(): return
				automatic = Automatic(devices)
				automatic.start()
			else:
				if automatic is None: return
				automatic.stop()
			return
		for key in val:
			val[key] *= 40.95
		for device in devices:
			device.setChannels(val)
	def on_close(self):
		pass

app = tornado.web.Application([
	(r"/socket", LEDWebSocket)
])

if __name__ ==	"__main__":
	app.listen(8080)
	tornado.ioloop.IOLoop.instance().start()
