# Canny to Detect Lane Lines

Let’s try our Canny edge detector on this image. This is where OpenCV gets useful. First, we'll have a look at the parameters for the OpenCV Canny function. You will call it like this:

		edges = cv2.Canny(gray, low_threshold, high_threshold)

The algorithm will first detect strong edge (strong gradient) pixels above the **high_threshold**, and reject pixels below the **low_threshold**. Next, pixels with values between the **low_threshold** and **high_threshold** will be included as long as they are connected to strong edges. 

This range implies that derivatives (essentially, the value differences from pixel to pixel) will be on the scale of tens or hundreds. **So, a reasonable range for your threshold parameters would also be in the tens to hundreds**.

As far as a ratio of **low_threshold** to **high_threshold**, John Canny himself recommended a low to high ratio of 1:2 or 1:3.

# Hough Transform

In image space, a line is plotted as x vs. y, but in 1962, Paul Hough devised a method for representing lines in parameter space, which we will call “Hough space” in his honor.

In Hough space, I can represent my "x vs. y" line as a point in "m vs. b" instead. The Hough Transform is just the conversion from image space to Hough space. So, the characterization of a line in image space will be a single point at the position (m, b) in Hough space.

y = mx + b

Since vertical lines have infinite slope so we need a new parameterization.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=xcos\theta_0+ysin\theta_0=\rho_0">

Within the Hough Space, <img src="http://chart.googleapis.com/chart?cht=tx&chl=\rho"> is the distance of the line from the origin, <img src="http://chart.googleapis.com/chart?cht=tx&chl=xcos\theta_0+ysin\theta_0=\theta"> is the angle away from horizontal.

## Implementing a Hough Transform on Edge Detected Image

Let's look at the input parameters for the OpenCV function HoughLinesP that we will use to find lines in the image. You will call it like this:

		lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

First off, rho and theta are the distance and angular resolution of our grid in Hough space. The units are pixel and radian. 


