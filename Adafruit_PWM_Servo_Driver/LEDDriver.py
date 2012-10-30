#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
from RGBDevice import RGBDevice
import tornado.ioloop
import tornado.web
import tornado.websocket
import json

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)

pwm.setPWMFreq(600)                        # Set frequency to 600 Hz

device = RGBDevice(pwm, 0)

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
#	for value in pattern:
#		device.fadeTo(value)
#		time.sleep(1)

class LEDWebSocket(tornado.websocket.WebSocketHandler):
	def open(self):
		pass
	def on_message(self, message):
		val = json.loads(str(message))
		for key in val:
			val[key] *= 40.95
		device.setChannels(val)
	def on_close(self):
		pass

app = tornado.web.Application([
	(r"/socket", LEDWebSocket)
])

if __name__ ==	"__main__":
	app.listen(8080)
	tornado.ioloop.IOLoop.instance().start()
