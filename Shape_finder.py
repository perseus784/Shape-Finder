import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils
import Heirarchical_Clustering as hc

lower = {'red': (168, 100, 100), 'green': (24, 100, 100),'blue':(93, 100, 100)}
upper = {'red': (188, 255, 255), 'green': (44, 255, 255),'blue':(113, 255, 255)}

#Image Pre-processing
img = cv2.imread("triangles.png")
img=imutils.resize(img,width=600,height=600)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(img, lower['red'], upper['red'])
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

dist_dict={}
def euclidean_dist(x,y):
    dist=np.linalg.norm(x-y)
    dist_dict[dist]=[x,y]
    pass

def slope(x1, y1, x2, y2):
    return (y1 - y2) / (x1 - x2)

def color_centers(x,lower,upper):
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        rect=cv2.minAreaRect(np.array(c))
        print rect
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            cv2.circle(img, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(img, center, 5, (0, 255, 0), -1)
            return center
    else:return 0

dst = cv2.cornerHarris(mask,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
x,y = np.nonzero(dst > 0.1* dst.max())
coordinates = zip(x, y)
new=[]
for i in coordinates:
    new.append(list(i))
# coverting range of points to a single point using heirarchial cluster.
actual_points=hc.auto_cluster(radius=5,data=np.array(new))
n_points=len(actual_points)
if n_points==2:print "It's a line"
elif n_points==3:print "Triangle"
elif n_points==4:print "Square"
elif n_points==5:print "Pentagon"
elif n_points==6:print "Hexagon"

##################################### ADDITIONAL STUFF ################
euclidean_dist(actual_points[0],actual_points[1])
euclidean_dist(actual_points[1],actual_points[2])
euclidean_dist(actual_points[2],actual_points[0])
hyp=max(dist_dict)
print "length of hypotenuse is",hyp

#you can do more operations from this
hyp_values=dist_dict[hyp]
x1,y1=hyp_values[0]
x2,y2=hyp_values[1]
m=slope(x1,y1,x2,y2)
print "printing slope of the hypotensue",m
print "tilt of the hypotenuse",np.degrees(np.arctan(m)),"degrees"
thres=5
cent=actual_points
#IMPORTANT TRANSFORMATION REQUIRED
[plt.scatter(y,-x,30) for x,y in new]
cv2.circle(img,(100,50), 5, (0, 255, 0), -1)

for c in cent:
    plt.scatter(cent[c][1],-cent[c][0] , s=300, marker='*',c='b')
# Threshold for an optimal value, it may vary depending on the image.

img[dst>0.1*dst.max()]=[250,0,0]
cv2.imshow('dst',img)
plt.show()

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
