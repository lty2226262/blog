# Introduction to Neural Networks

## Linear Regression

Draw a line to best fit the data. 

How to find the line? 

1. start by drawing a random line and see how bad this line is:

	to compute the error, LSM

2. minimize the error

	general procedure is known as gradient descent.

## Logistic Regression

Find a best line to cut the data.
	
draw a random line and then gradient descent to minimize the error function: the number of incorrect points.

## Neural network

Our computer could do one thing at a time, so we divide the data by two lines.

## Perceptron

Or artificial neurons, they are the basic unit of a neural network.

### Weights

When input comes into a perception, it gets multiplied by a weight value that is assigned to this particular input. The network adjusts the weights based on any errors in categorization that results from the previous weights. This is called training the NN.

A higher weights means more important, otherwise.

### Summing the input data

1. weights multiply the inputs and sum

### Calulating the output with an activation function

feed the linear combination into an activation function.

## Gradient Descent

From before we saw that one weight update can be calculated as:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=\Delta w_i=\eta\delta x_i">

<img src="http://chart.googleapis.com/chart?cht=tx&chl=\delta"> is the error term:

<img src="http://chart.googleapis.com/chart?cht=tx&chl=\delta=(y-\hat{y})f'(h)=(y-\hat{y})f'(\sum w_i x_i)">

## Implementing gradient descent

### Data cleanup

If the numbers don't encode any sort of relative values. Rank 2 is not twice as much as rank 1. So we need to use dummy varibles to encode these variables.

Then need to standardize data, which means to scale the values such they have zero mean and a standard deviation of 1. This is necessary because the sigmoid function squashes really small and really large inputs.

### Calculate error

We're going to make a small change to how we calculate the error. Instead of the SSE, we're going to use the mean of the square errors(MSE). Summing up all the weight steps can lead to really large updates that make the gradient descent diverge.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=E=\frac{1}{2m}\sum_\mu (y^\mu-\hat{y}^\mu)^2">

Here's the general algorithm for updating the weights with gradient descent:

* Set the weights step to zero: <img src="http://chart.googleapis.com/chart?cht=tx&chl=\Delta w_i = 0">
* For each record in the training data:
	* Make a forward pass through the network, calculating the output  <img src="http://chart.googleapis.com/chart?cht=tx&chl=\hat{y}=f(\sum_iw_ix_i)">
	* Calculate the error gradient in the output unit, 