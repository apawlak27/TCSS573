from gpiozero import MotionSensor
import json
import time
import picamera
import datetime
from grovepi import *
from watson_developer_cloud import VisualRecognitionV3

pir = MotionSensor(4)  # GPIO pin 4
camera = picamera.PiCamera()
sound = 1  # sound sensor uses analog port A1

# Set sound sensor for input
pinMode(sound, 'INPUT')

# IBM Watson Visual Recognition Connection
visual_recognition = VisualRecognitionV3(
	version = '2018-03-19',
	api_key = '18d4c1e894c94a600bce36b0aab3b6c17ee14a1f'
)


def classify_image(image):
	'''
	Sends image(s) to IBM Watson VR custom classifier and returns
	class (safe or threat) of given image(s) and corresponding score
	'''
	with open(image, 'rb') as image_file:
		classes = visual_recognition.classify(
			image_file,
			threshold='0.6',
			classifier_ids='DefaultCustomModel_992034364')
		print(json.dumps(classes, indent=2))


def motion_picture():
	'''
	Continually senses for motion. When motion is detected, 
	image is captured via picamera, saved to system, and sent 
	to IBM Watson for classification.
	'''
	while True:
		try:
			time.sleep(0.25)
			pir.wait_for_motion()
			#print("Motion detected!")
			picture = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S') + '.jpg'
			camera.capture(picture)
			time.sleep(0.25)
			classify_image(picture)

		except KeyboardInterrupt:
			break
			
		except:
			print('error')


def sound_picture():
	'''
	Coninually senses for sounds. When sound over the given 
	threshold is detected, image is captured via picamera, 
	saved to system, and sent to IBM Watson for classification.
	'''
	while True:
		try:
			time.sleep(0.25)
			volume = analogRead(sound)
			#print("sound value: %d" % volume)
			if (volume > 400):
				picture = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S') + '.jpg'
				camera.capture(picture)
				time.sleep(0.5)
				classify_image(picture)

		except KeyboardInterrupt:
			break
			
		except:
			print('error')


def motion_video():
	'''
	Continually senses for motion. When motion is detected, 
	video is captured via picamera and saved to system.
	'''
	while True:
		try:
			time.sleep(0.25)
			pir.wait_for_motion()
			#print("Motion detected!")
			video = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S') + '.h264'
			camera.start_recording(video)
			time.sleep(5)
			camera.stop_recording()

		except KeyboardInterrupt:
			break
			
		except:
			print('error')


def sound_video():
	'''
	Coninually senses for sounds. When sound over the given 
	threshold is detected When motion is detected, 
	video is captured via picamera and saved to system.
	'''
	while True:
		try:
			time.sleep(0.25)
			volume = analogRead(sound)
			#print("sound value: %d" % volume)
			if (volume > 400):
				print('Sound Detected')
				video = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S') + '.h264'
				camera.start_recording(video)
				time.sleep(5)
				camera.stop_recording()
		except KeyboardInterrupt:
			break
		except:
			print('error')
	


# motion_picture()			
# motion_video()		
