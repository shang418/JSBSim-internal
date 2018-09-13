import matplotlib.pyplot as plt
from AileronRoll import AileronRoll
import numpy as np
# constants


fig = plt.figure()
ax = fig.add_subplot(111)
# plot our line with transparent markers, and markersize the size of our image
# we need to make the frame transparent so the image can be seen
# only in trunk can you put the image on top of the plot, see this link:
# http://www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg14534.html)

ail= AileronRoll(0,0,50,0.3)
state = []
t = []


for i in range(200):
    state.append(ail._getdesiredstate_(i*0.1)[0])
    print(state)
    t.append(0.1*i)
    ax.plot(t,state,'-r')
    plt.pause(0.001)
plt.show()