import numpy as np
import matplotlib.pyplot as plt

#Intro
name = input('USER, please enter your name?\n')
print('Hello %s, Welcome to the TRIG PLOTTER EXPERIENCE\n' % name)

#user adjustable parameters
trig_func = input('which trig function would you like plotted?\n'
                  'sine\n'
                  'cosine\n'
                  'tangent\n')

periods = int(input('how many periods of pi would you like graphed?\n'))

dots = int(input('how many data points would you like displayed?\n'))

#initialize variables to be used as arguments
#adjusts periods to multiples of pi

pi_mult = periods * 2

#determines spacing between data points

step_size = pi_mult * np.pi / dots

#builds list of range data points from 0 to n*pi

theta_range = np.arange(0, pi_mult * np.pi, step_size)

#each function operates a trig function on theta_range and creates plot
def plotsine():
    sin = np.sin(theta_range)
    plt.plot(theta_range, sin, 'b+', label='sines are lit')
    plt.title('%d Periods of Sine with %d points' % (periods,dots))
    plt.ylabel('sine of x')
    plt.xlabel('x')

def plotcosine():
    cos = np.cos(theta_range)
    plt.plot(theta_range, cos, 'r+', label='cosines are dope')
    plt.title("%d Periods of Cosine with %d points" % (periods,dots))
    plt.ylabel('Cosine of x')
    plt.xlabel('x')

def plottangent():
    tan = np.tan(theta_range)
    plt.plot(theta_range, tan, 'yo--', label='tangents are fly')
    plt.ylim(10,-10)
    plt.title('%d Periods of Tangent with %d points' % (periods, dots))
    plt.ylabel('Tangent of x (asymptote limited at +/-10)')
    plt.xlabel('x')

#Selects which plot function based on user input
if trig_func == 'sine':
    plotsine()
elif trig_func == 'cosine':
    plotcosine()
elif trig_func == 'tangent':
    plottangent()
#dynamic range tick marks
ticks = []
#want first tick to be 'zero' instead of '0pi'
tick_labels = ['0']
x = 0
while x <= pi_mult:
    ticks.append(x*np.pi)
    x += 2
    tick_labels.append('%dpi' % x)
plt.xticks(ticks, tick_labels)

#what to show
plt.legend()
plt.show()

print('\nThanks!')