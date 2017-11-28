# DSI Capstone Project
## Image Classification on CIFAR-10

### Introduction



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