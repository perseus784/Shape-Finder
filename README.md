# Shape-Finder
A Shape Finder using Corner-Harris and Heirarchical Clustering.

*Prerequisite:*
- Python 2.7.
- [OpenCV Contributed version](https://pypi.python.org/pypi/opencv-contrib-python) is needed to CornerHarris Corner detection.
- Other libs: Matplotlib, numpy, imutils.


How is this method different from other shape finders:  
Generally, all shape finders will use number of arcs to determine the shape of an object.
But this method uses Corners of an object to determine it's shape.
Using this method we can find the length of the arcs, angles and more.

**Okay, how it is done ?**
Glad you asked, We can easily find corners using Corner-Harris method!  
The issue is Corner-Harris is not very accurate in real time. If we give it a triangle, it should give only 3 corners.
Instead, it gives us 30-40 nearby points for each corner.

Now our task is convert this 120 points into 3 corners.  
After some search and learnings from AI techniques, it's found that Heirarchical Clustering is the way to do it.

## Heirarchical Clustering:  
Two liner: It's a Machine Learning technique used to group bunch of points without giving any idea or mentioning number of groups required. Unlike traditional Clustering, we don't have to give to how many groups it should be seperated.  
*It is simply demonstrated [here](https://github.com/perseus784/Shape-Finder/blob/master/Heirarchical_Clustering.py).*  

Those *stars* represent an individual group for each cluster.
<p align="center">
<img src="/media/hr.png" alt="hr" width="700" height="400">
</p>

## Groupify the seperate clusters:

**Supply Image:**  
For simplicity, we give it a image containg triangles.  
We did some contour detection for selecting the triangle for a particular color.  
In this case, we select *Red* one as our target triangle.  
<p align="center">
<img src="/media/triangles.png" alt="tri" width="400" height="250">
</p>

**Find Corners:**  
Now apply **Corner-Harris** to find the corners in the contour.  
We found some bunch of points in each corner, we will have find the actual corners from this by applying Heirarchical Clustering.  
Once we apply HC, it is gonna look like this in graph:  
That *Star* represents the center that it found for each cluster.
<p align="center">
<img src="/media/Clustering.png" alt="matplot" width="700" height="400">
</p>

**Visualization:**
<p align="center">
<img src="/media/Clustered_image.png" alt="opencv" width="600" height="350">
</p>

### Output:
Once we got our 3 corners, it is easy to determine it's shape and we can do more operations from other informations like below:  
<p align="center">
<img src="/media/ouput.png" alt="op" width="800" height="300">
</p>

