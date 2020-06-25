# EmotionRecognition
Convolutional neural Network is used for image analysis, it basically takes an image as an input and classifies it on the basis of different factors.In this Project We are trying to make a real time Convolutional Neural Network, In total whenever the image though camera will be read (given) , the system will perform the tasks of face detection, gender classiﬁcation and emotion classiﬁcation simultaneously.
Initially we took the dataset of FER-2013 emotion dataset,The emotion dataset consists of mainly “angry”, “disgust”, “fear”, “happy”, “sad”, “surprise”, “neutral” features  and separated the dataset into different folders so that the dataset can be converted into images .After that we have used augmentation .Image augmentation is a technique used to expand the dataset, using existing images.It creates new and different images from the existing dataset and creates a large set of images used for dataset.In some cases , It is most likely that overfitting will take place , as in overfitting only accuracy is achieved in training data but fails in testing data, therefore by augmenting the images performance is increased and the model generalizes well.We have used Imgaug class for the same and the basic features that we have applied are flipping , rotation ,cropping etc.
After augmentation is completed , we have performed training on initially the original dataset and next time , with the augmented dataset along with original data set.
Using only CNN is complicated sometimes as cnn has hidden layers and we also need to balance between classification accuracy and parameters , therefore in this the gradient back propogation method is introduced.
After this , the model consisting of about 6000 parameters was trained on the IMDB gender dataset where each image was classified either into a man or woman and a decent accuracy will be achieved.The name of this model is named as sequential fully CNN.
At the end we will reduce the no of parameters keeping it real time possible inference.
So at the end of this project a real time convolutional network consisting of emotion classification , gender classification and face detection will be made by reducing the parameters and using back propogation visualization.

Accuracy :: Training :: 59 percent
            Training(of augmented images) 60
            
