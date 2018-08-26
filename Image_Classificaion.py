from watson_developer_cloud import VisualRecognitionV3
import json
import glob


# IBM Watson Visual Recognition Connection
visual_recognition = VisualRecognitionV3(
	version="2018-03-19",
	api_key="18d4c1e894c94a600bce36b0aab3b6c17ee14a1f"
)


def classify_images(images):
	'''
	Input:
		Either single image or zip file of images
	Output:
		Image classification
	Sends image(s) to IBM Watson VR custom classifier and returns
	class (safe or threat) of given image(s) and corresponding score
	'''
	with open(images, 'rb') as image_files:
		classes = visual_recognition.classify(
			image_files,
			threshold='0.6',
			classifier_ids='DefaultCustomModel_992034364')
		print(json.dumps(classes, indent=2))

# Classify folder of images (zip file)
classify_images('./images.zip')

# Classify single image
#classify_images('./images/crime2.jpeg')
