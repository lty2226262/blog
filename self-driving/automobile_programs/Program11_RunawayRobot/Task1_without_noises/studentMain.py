# ----------
# Background
# 
# A robotics company named Trax has created a line of small self-driving robots 
# designed to autonomously traverse desert environments in search of undiscovered
# water deposits.
#
# A Traxbot looks like a small tank. Each one is about half a meter long and drives
# on two continuous metal tracks. In order to maneuver itself, a Traxbot can do one
# of two things: it can drive in a straight line or it can turn. So to make a 
# right turn, A Traxbot will drive forward, stop, turn 90 degrees, then continue
# driving straight.
#
# This series of questions involves the recovery of a rogue Traxbot. This bot has 
# gotten lost somewhere in the desert and is now stuck driving in an almost-circle: it has
# been repeatedly driving forward by some step size, stopping, turning a certain 
# amount, and repeating this process... Luckily, the Traxbot is still sending all
# of its sensor data back to headquarters.
#
# In this project, we will start with a simple version of this problem and 
# gradually add complexity. By the end, you will have a fully articulated
# plan for recovering the lost Traxbot.
# 
# ----------
# Part One
#
# Let's start by thinking about circular motion (well, really it's polygon motion
# that is close to circular motion). Assume that Traxbot lives on 
# an (x, y) coordinate plane and (for now) is sending you PERFECTLY ACCURATE sensor 
# measurements. 
#
# With a few measurements you should be able to figure out the step size and the 
# turning angle that Traxbot is moving with.
# With these two pieces of information, you should be able to 
# write a function that can predict Traxbot's next location.
#
# You can use the robot class that is already written to make your life easier. 
# You should re-familiarize yourself with this class, since some of the details
# have changed. 
#
# ----------
# YOUR JOB
#
# Complete the estimate_next_pos function. You will probably want to use
# the OTHER variable to keep track of information about the runaway robot.
#
# ----------
# GRADING
# 
# We will make repeated calls to your estimate_next_pos function. After
# each call, we will compare your estimated position to the robot's true
# position. As soon as you are within 0.01 stepsizes of the true position,
# you will be marked correct and we will tell you how many steps it took
# before your function successfully located the target bot.

# These import steps give you access to libraries which you may (or may
# not) want to use.
from robot import *
from math import *
from matrix import *
import random

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx


# This is the function you have to write. The argument 'measurement' is a 
# single (x, y) point. This function will have to be called multiple
# times before you have enough information to accurately predict the
# next position. The OTHER variable that your function returns will be 
# passed back to your function the next time it is called. You can use
# this to keep track of important information over time.
def estimate_next_pos(measurement, OTHER = None):
    """Estimate the next (x, y) position of the wandering Traxbot
    based on noisy (x, y) measurements."""

    # You must return xy_estimate (x, y), and OTHER (even if it is None)
    # in this order for grading purposes.
    if OTHER is None:
        OTHER = {'pre_p':measurement}
        xy_estimate = measurement
    else:
        pre_p = OTHER['pre_p']
        pre_x = pre_p[0]
        pre_y = pre_p[1]
        x = measurement[0]
        y = measurement[1]
        orientation = atan2(y - pre_y, x - pre_x)
        if 'pre_o' not in OTHER:
            OTHER['pre_o'] = orientation
            OTHER['pre_p'] = measurement
            xy_estimate = (2 * x - pre_x, 2 * y - pre_y)
        else:
            pre_o = OTHER['pre_o']
            theta = (orientation - pre_o) % (2. * pi)
            # print (pi-theta)/2.
            # r = distance_between(pre_p,measurement)/(2.*cos((pi-theta)/2.))
            # print distance_between(pre_p,measurement)
            # print r
            r = distance_between(pre_p, measurement)
            new_o = orientation + theta

            OTHER['pre_o'] = orientation
            OTHER['pre_p'] = measurement
            # x_est = x - 2. * r * sin((orientation * 2. + theta)/2.) * sin(theta/2.)
            # y_est = y + 2. * r * cos((orientation * 2. + theta)/2.) * sin(theta/2.)

            x_est = x + r * cos(new_o)
            y_est = y + r * sin(new_o)

            xy_estimate = (x_est, y_est)

    return xy_estimate, OTHER

# A helper function you may find useful.
def distance_between(point1, point2):
    """Computes distance between point1 and point2. Points are (x, y) pairs."""
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# This is here to give you a sense for how we will be running and grading
# your code. Note that the OTHER variable allows you to store any
# information that you want.
def demo_grading(estimate_next_pos_fcn, target_bot, OTHER = None):
    localized = False
    distance_tolerance = 0.01 * target_bot.distance
    ctr = 0
    # if you haven't localized the target bot, make a guess about the next
    # position, then we move the bot and compare your guess to the true
    # next position. When you are close enough, we stop checking.
    true_pos = []
    guess_pos = []
    while not localized and ctr <= 10:
        ctr += 1
        measurement = target_bot.sense()
        position_guess, OTHER = estimate_next_pos_fcn(measurement, OTHER)
        target_bot.move_in_circle()
        true_position = (target_bot.x, target_bot.y)
        # print "true:",true_position,"position_guess:",position_guess
        true_pos.append(true_position)
        guess_pos.append(position_guess)
        error = distance_between(position_guess, true_position)
        # print error
        if error <= distance_tolerance:
            print "You got it right! It took you ", ctr, " steps to localize."
            localized = True
        if ctr == 10:
            print "Sorry, it took you too many steps to localize the target."
    plt.figure()
    for idx in range(0,len(true_pos)-1):
        plt.quiver(true_pos[idx][0],
                  true_pos[idx][1],
                  true_pos[idx + 1][0] - true_pos[idx][0],
                  true_pos[idx + 1][1] - true_pos[idx][1],scale_units='xy', angles='xy', scale=1,
                  color='red')
        plt.quiver(guess_pos[idx][0],
                  guess_pos[idx][1],
                  guess_pos[idx + 1][0] - guess_pos[idx][0],
                  guess_pos[idx + 1][1] - guess_pos[idx][1],scale_units='xy', angles='xy', scale=1,
                  color='blue')
    plt.show()
    return localized

# This is a demo for what a strategy could look like. This one isn't very good.
def naive_next_pos(measurement, OTHER = None):
    """This strategy records the first reported position of the target and
    assumes that eventually the target bot will eventually return to that
    position, so it always guesses that the first position will be the next."""
    if not OTHER: # this is the first measurement
        OTHER = measurement
    xy_estimate = OTHER
    return xy_estimate, OTHER

# This is how we create a target bot. Check the robot.py file to understand
# How the robot class behaves.
test_target = robot(2.1, 4.3, 0.5, 2*pi / 34.0, 1.5)
test_target.set_noise(0.0, 0.0, 0.0)

demo_grading(estimate_next_pos, test_target)
