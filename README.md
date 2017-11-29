# DSI Capstone Project
## Image Classification on CIFAR-10

### Introduction

In 2012, CNN's achieved state-of-the-art status when the AlexNet "large, deep convulutional neural network" won the 2012 ImageNet Large-Scale Visual Recognition Challenge. AlexNet, programmed by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton achieved a top 5 test error rate of 15.4%. The runner up achieved only 26.2%. These results stunned the community and quickly led to CNN's being adopted by the computer vision community. (Deshpande, Adit)

CIFAR-10 is an image classification dataset comprising of 60,000 images, each of which is a 32x32 RBG image. Ten classifications exist. The relatively small scale and number of classifications make this dataset an ideal set for training a convulutional neural network to prove viability. 

Convulutional neural networks are complex and require a deep understanding of calculus and programming. 

The files and their description can be found on the cs.toronto.edu website, linked below. 

https://www.cs.toronto.edu/~kriz/cifar.html

### Notebooks & Scripts

00. EDA 
 - Load the files
 - Show a unique set of images
 - Show another set of unique images
 - Display the first set of unique images with each of the three color bands individually set to all 0's.
 - Investigate Color histograms for an image in each class
 - Confirm class balance
01. CNN from example
 - First stab at a convulutional neural network
 - Follow along with example provided in keras git repo
 - Achieve baseline performance
 - Ensure proper formating for array's (update __init__.py with changes and removed from notebook). 

__init__.py imports required libraries and sets up the data in numpy arrays for training in CNN's. 

### Questions / To Do
1. Not sure whether my implementation of the color histograms was the correct idea. 
2. Understand backpropagation to discover why the model is getting worse as it trains.
3. Eventually, do feature selection to make the model even better. 

#### References:
Deshpande, Adit. “The 9 Deep Learning Papers You Need To Know About (Understanding CNNs Part 3).” CS Undergrad at UCLA ('19), 24 Aug. 2016, https://adeshpande3.github.io/adeshpande3.github.io/The-9-Deep-Learning-Papers-You-Need-To-Know-About.html.
