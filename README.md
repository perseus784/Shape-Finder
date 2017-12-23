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

Image supplied:
<p align="center">
<img src="/media/triangles.png" alt="tri" width="700" height="400">
</p>

Heirarchical Clustering:
<p align="center">
<img src="/media/Clustering.png" alt="matplot" width="700" height="400">
</p>

Applied HC in the image:
<p align="center">
<img src="/media/Clustered_image.png" alt="opencv" width="700" height="400">
</p>

Output:
<p align="center">
<img src="/media/ouput.png" alt="op" width="800" height="300">
</p>

