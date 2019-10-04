# Vehicle-Detection
Vehicle(object) detection and counting the type of different vehicles in a video feed.
With the evolution of artificial intelligence and, specially, machine learning, tech Automatic
detecting and counting vehicles in unsupervised video on railway crossings is a very challenging
problem with important practical applications such as to monitor activities for detecting the need of
bridge and load of vehicles on bridge if need be, and then predict the traffic flow which assists in
bridge requirement specifications. Manually reviewing the large amount of data they generate is
often impractical.\
We will be developing an object detection system with neural networks using the Yolo (You Only
Look Once) network architecture to detect and classify vehicle by training and evaluating the model
using various datasets. A counting algorithm based on checking existence of same object in some
particular area to count the detected vehicles in a video and extract conclusions on the need for the
bridge to build with certain specifications.
In our approach we will be using a fully connected convolutional neural network (CNN) model,
called YOLO. YOLO reframes object detection as simple regression problem, straight from image
pixels to bounding box coordinates and class probabilities.

#### Data Gathering
We first collected the image data to train our model. The images are collected from Google images
and Image.net. Around 1500 images of every class of vehicle (car, heavy vehicle and two wheeler)
are collected. The data gathering is done with the help of the python script.

#### Data Cleaning and Annotations
All the images that does not contain our labelled object or images in which the object is unclear are
removed from our data set. The cleaned data is then annotated using a python script. In this we are
storing the area of interest or the area where the object is present in the corresponding xml file.
We created two python script one for creating the bounding box for selecting the object
and the other one for generating xml of the selected object.
The content of xml file include the folder name of corresponding images, image’s filename , the
label of the object selected, the dimension of the bounding box of the object etc. And all these xml
file are stored inside the Annotations folder.
#### Training
We have used pre-trained weights for this project. YOLO weights and cfg file are downloaded and
placed in our Bin and cfg folder of our project directory. The weights and cfg file are available to
user on Darknet, website to help user pre-train their own image detection model in YOLO. We
downloaded tiny_yolo_voc.cfg and tiny_yolo.weights files for our model training. Training the
model takes approximately 1 day for our dataset and with processing power of our laptop. The time
required for training depends on the size of dataset and the processing power.

