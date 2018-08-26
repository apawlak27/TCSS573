# Public Safety Surveillance System
### TCSS 573 - Group 9
### Sonal Goswami & Alex Pawlak


For our project we have designed and implemented a security system built on a Raspberry Pi with GrovePi+. The security systems uses an attached motion sensor, sound sensor, and camerapi as the hardware devices. The system is built on Node-Red and integrated with IBM Watson. A Node-Red Dashboard is also used for monitoring purposes. The system monitors for motion and sound and updates the dashboard in real-time.
and upon detection of either captures images which are sent and stored on IBM Watson cloud. The images are also classified on a custom built model on IBM Watson's Visual Recognition. The classification is either threat or safe. Upon classifying the image, if a threat is detected then an email is sent with the timestamp, sensor ID, and attached image.

## Getting Started 

The program is run on Node-Red. The Node-Red flow is included in the zip file as flow.txt in the code folder. Node-Red needs to be installed and running on the Raspberry Pi.  

The images taken by the camera are temporarily saved on the RPi. The file path included on the flow is /home/pi/Desktop/project/images/ If changed, the file path must be changed in "Take Photo" node and "save photo" node.  

The email node is set to send notifications to IoTgr09@gmail.com and can be changed.  

The flow is set up to connect to our custom IBM Visual Recognition classifier and save to our IBM Cloudant database.  

There are two "inject nodes" included in the flow that have been used for testing. They are setup with URL's to images that have been classified as "threat" and "safe".  

They are not needed for running to program, simply there to test connections with IBM without having to set the motion or sound detection off every time.  

The images used for training the IBM Watson Visual Recognition custom model are included in our zip file in the code folder. They are split into two folders, safe and threat, as used to train the model.  

## Prerequisites

The sensors need to be attached to the Raspberry Pi as follows:
  PIR Motion Sensor - GPIO04 (Pin 7)
  Sound Sensor - GrovePi+ A0 port
  CameraPi - Raspberry Pi input  

Node-Red Nodes that need to be installed from the Pallete Manager:
  *node-red-dashboard
  *node-red-grovepi-nodes
  *node-red-contrib-grovepi
  *node-red-contrib-camerapi
  *node-red-contrib-scx-ibmiotapp
  *node-red-ibm-watson-iot
  *node-red-node-cf-cloudant
  *node-red-node-email

## Deployment

To run the security system:

  *Boot up the Raspberry Pi and open a new console

  *Run "node-red start" in the console

  *Once running, direct the internet browser to the ip address and port listed at the top of the console output. Example: http://http://10.0.1.15:1880/

  *Running the first time: import the flow from clipboard on Node-Red

  *Deploy to start the program

  *Direct a second window on the browser to the same ip address and port with "/ui" at the end. Example: http://http://10.0.1.15:1880/ui

  *Once the flow is deployed, the system will begin monitoring for motion and sound and capturing images for classification. The dashboard will show details of the system immediately upon deployment, including timestamps for motion and sound detected, images captured, and the classification of the images.

To stop the security system:
  Either:
    Disable the flow on Node-Red by double clicking the flow name and switching to disabled and then clicking Deploy again.

    or

    Run "node-red stop" in the console
