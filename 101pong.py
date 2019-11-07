#!/usr/bin/python3
import sys
from math import *

def main():
    if len(sys.argv) != 8:
        help()
    else:
        argv = sys.argv
        vect_v1 = 3
        vect_v2 = 3
        vect_v3 = -3
        try :
            x0, y0, z0 = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
            x1, y1, z1 = float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
            n = int(sys.argv[7])
        except ValueError:
            help()
            sys.exit(84)
        V1 = x1 - x0 
        V2 = y1 - y0
        V3 = z1 - z0
        print ("The velocity vector of the ball is:")
        print ("(%.2f, %.2f, %.2f)" %(V1, V2, V3))
        x4 = x1 + V1 * 4
        y4 = y1 + V2 * 4
        z4 = z1 + V3 * 4
        print("At time t + 4, ball coordinates will be:")
        print ("(%.2f, %.2f, %.2f)" %(x4, y4, z4))
        
        produit_scalaire = sqrt(pow(V1, 2) + pow(V2, 2) + pow(V3, 2))
        ang = 90 - (acos((abs(V3)) / produit_scalaire)) * 180 / pi

        #gestion du cas 'si la balle ne touche pas le plan'
        if ((z1 - z0 == 0) & (z1 != 0)):
            print ("The ball won't reach the paddle.")
            sys.exit(0)
        if (-z1/(z1-z0) < 0):
            print ("The ball won't reach the paddle.")
            sys.exit(0)   
        if (ang == 0):
            print ("The ball won't reach the paddle.")
            sys.exit(0)

        print ("The incidence angle is :")
        print ("%.2f degrees" % ang)
def help():
        print(" USAGE")
        print("    ./101pong x0 y0 z0 x1 y1 z1 n\n")
        print(" DESCRIPTION")
        print("     x0  ball abscissa at time t - 1")
        print("     y0  ball ordinate at time t - 1")
        print("     z0  ball altitude at time t - 1")
        print("     x1  ball abscissa at time t")
        print("     y1  ball ordinate at time t")
        print("     z1  ball altitude at time t")
        print("     n   time shift (greater than or equal to zero, integer)") 
if __name__ == "__main__":
    main()