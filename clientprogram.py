#client program
import mymath as m
c=m.perimeterofsquare(4)
decimals=17
print("perimeter is:{0:.{1}f}m".format(c,decimals))
c=m.volumeofhollowcylinder(2,1,2)
decimals=17
print("area is:{0:.{1}f}m\u00b2".format(c,decimals))
c=m.volumeofcone(5,9)
decimals=17
print("volume is:{0:.{1}f}m\u00b3".format(c,decimals))
  

