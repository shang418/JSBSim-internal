import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.image as image
from arrow3d import Arrow3D
import math

def eulerAnglesToRotationMatrix(theta) :
     
    R_x = np.array([[1,         0,                  0                   ],
                    [0,         math.cos(theta[0]), -math.sin(theta[0]) ],
                    [0,         math.sin(theta[0]), math.cos(theta[0])  ]
                    ])
         
         
                     
    R_y = np.array([[math.cos(theta[1]),    0,      math.sin(theta[1])  ],
                    [0,                     1,      0                   ],
                    [-math.sin(theta[1]),   0,      math.cos(theta[1])  ]
                    ])
                 
    R_z = np.array([[math.cos(theta[2]),    -math.sin(theta[2]),    0],
                    [math.sin(theta[2]),    math.cos(theta[2]),     0],
                    [0,                     0,                      1]
                    ])
                     
                     
    R = np.dot(R_z, np.dot( R_y, R_x ))
 
    return R



def plotter_3d(position,angles,ax):
    # unpack position data
    x = position[0]
    y = position[1]
    z = position[2]
    
    # #unpack angle data 
    # theta = angles[0]
    # phi = angles[1]
    # psi = angles[2]
    data_size = len(x)
    print(data_size)
    v = np.array([[1,0,0],[0,1,0],[0,0,1]])
    c = ['r','g','b']
    for i in range(data_size):
        x_i = x[i]
        y_i = y[i]
        z_i = z[i]
        j=0
        for vec in v:
            R = eulerAnglesToRotationMatrix(angles[i])
            vec = np.dot(R,vec)
            a = Arrow3D([x_i, x_i + vec[0]], [y_i, y_i + vec[1]], [z_i, z_i +vec[2]], mutation_scale=10, lw=1, arrowstyle="-|>", color=c[j])
            ax.add_artist(a)
            ax.plot(x[0:i+1],y[0:i+1],z[0:i+1],'m-')
            j+=1
        plt.pause(0.01)

