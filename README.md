# MyMath Module
The MyMath module is a Python module that contains user-defined functions for calculating the area, volume, and perimeter of various 2D and 3D shapes. This module provides a convenient way to perform common mathematical calculations related to shapes.
----
# Features
The module has about 66 functions which can be used the client program.
Some of the  following functions MyMath module includes:

# 2D Shapes

+ areaofrectangle(length, width): Calculates the area of a rectangle given its length and width.
+ areaofsquare(side): Calculates the area of a square given the length of its side.
+ areaofcircle(radius): Calculates the area of a circle given its radius.
+ perimeterofrectangle(length, width): Calculates the perimeter of a rectangle given its length and width.
+ perimeterofsquare(side): Calculates the perimeter of a square given the length of its side.
+ circumferenceofcircle(radius): Calculates the circumference of a circle given its radius.

# 3D Shapes
+ volumeofcube(side): Calculates the volume of a cube given the length of its side.
+ volumeofsphere(radius): Calculates the volume of a sphere given its radius.
+ lateralsurfaceareaofcube(side): Calculates the lateral surface area of a cube given the length of its side.
+ lateralsurfaceareaofsphere(radius): Calculates the lateral surface area of a sphere given its radius.

# Usage

````
import mymath as m
# Example usage
c=m.perimeterofsquare(4)
decimals=17
print("perimeter is:{0:.{1}f}m".format(c,decimals))
c=m.volumeofhollowcylinder(2,1,2)
decimals=17
print("area is:{0:.{1}f}m\u00b2".format(c,decimals))
c=m.volumeofcone(5,9)
decimals=17
print("volume is:{0:.{1}f}m\u00b3".format(c,decimals))
```
### Make sure that the MyMath module (mymath.py) is in the same directory as your Python script or accessible through the Python module search path.
# Requirements:
+ Python 3.6 and above
