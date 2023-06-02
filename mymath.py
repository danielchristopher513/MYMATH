"""calculates areas,lateral surface area,volumes and perimeter  of different figures both 2d
and 3d  shapes and areas of special shapes using standard results.
----------------------mymath----------------------------------------
 this module consists of user defined functions, to calculate area,
 lateral surface area ,volume and perimeter of different shapes
-----------------------------------------------------------------
by team 08
"""
def areaofsquare(a):
    return a*a
def areaoftriangle(b,h):
    return 0.5*b*h
def areaofrectangle(l,b):
    return l*b
def areaofcircle(r):
    a=(((22/7))*((r**2)))
    return a
def areaofparalleogram(b,h):
    return b*h
def areaoftrapezium(a,b,h):
    b=(0.5*(a+b))*h
    return b
def areaofellipse(a,b):
    c=(22/7)*(a)*(b)
    return c
def areaofcube(a):
    d=(6*(a**2))
    return d
def areaofrectangularprism(l,w,h):
    e=(2*(w*l+h*l+h*w))
    return e
def areaofcylinder(r,h):
    f=(((2*(22/7))*(r)))*((r+h))
    return f
def areaofcone(r,l):
    g=(((22/7)*r))*((r+l))
    return g
def areaofsphere(r):
    i=(4*(22/7)*(r**2))
    return i
def areaofhemisphere(r):
    j=((3*(22/7))*((r**2)))
    return j
def areaofsector(r,α):
    k=(α/360)*((22/7)*r*r)
    return k
def areaofsemicircle(r):
    l=((((22/7))*((r**2)))/2)
    return l
def areaofcuboid(l,b,h):
    m=(2*(l*b+b*h+h*l))
    return m
def lateralsurfaceareaofcube(a):
    n=4*(a**2)
    return n
def lateralsurfaceareaofcuboid(l,b,h):
    o=(2*h)*((l+b))
    return o
def lateralsurfaceareaofsphere(r):
    p=(4*(22/7)*(r**2))
    return p
def lateralsurfaceareaofhemisphere(r):
    q=(2*(22/7)*(r**2))
    return q
def lateralsurfaceareaofcylinder(r,h):
    r=((2*(22/7))*(r)*(h))
    return r
def lateralsurfaceareaofcone(r,l):
    s=(((22/7))*((r)*(l)))
    return s
def areaofrhombus(b,h):
    return b*h
def volumeofcuboid(l,b,h):
    return l*b*h
def volumeofcube(a):
    return a*a*a
def volumeofcylinder(r,h):
    t=((22/7)*(r**2)*(h))
    return t
def volumeofprism(b,h):
    return b*h
def volumeofsphere(r):
    t=((4/3)*(22/7)*(r**3))
    return t
def areaofpyramid(p,l,b):
    u=(0.5*p*l)+b
    return u
def lateralsurfaceareaofpyramid(p,l):
    v=(0.5*p*l)
    return v
def areaofprism(p,h,b):
    w=(p*h)+(2*b)
    return w
def lateralsurfaceareaofprism(p,h):
    return p*h
def volumeofpyramid(b,h):
    x=(1/3)*b*h
    return x
def volumeofcone(r,h):
    y=((1/3)*(22/7)*(r**2)*h)
    return y
def volumeofrectangularpyramid(l,b,h):
    z=(1/3)*l*b*h
    return z
def volumeofellipsoid(a,b,c):
    a1=((4/3)*(22/7)*a*b*c)
    return a1
def areaofellipsoid(a,b,c):
    p=(8/5)
    b1=(4*(22/7))*(((((a**p)*(b**p))+((a**p)*(c**p))+((b**p)*(c**p)))/3)**0.5)
    return b1
def volumeoftetrahedron(a):
    c1=((a**3)/(6*(2**0.5)))
    return c1
def areaoftetrahedron(a):
    d1=((2*a)/(6**0.5))
    return d1
def perimeterofsquare(a):
    e1=4*a
    return e1
def perimeterofparallelogram(b,h):
    f1=2*(b+h)
    return f1
def perimeteroftriangle(a,b,c):
    g1=(a+b+c)
    return g1
def perimeteroftrapezoid(a,b,c,d):
    return a+b+c+d
def perimeterofrhombus(a):
    return 4*a
def perimeterofrectangle(l,b):
    h1=2*(l+b)
    return h1
def semiperimeteroftriangle(a,b,c):
    i1=(a+b+c)/2
    return i1
def circumferenceofcircle(r):
    j1=2*(22/7)*r
    return j1
def areabetweenparabolaandline(a,m):
    l1=8*((a**2)/((3*(m**3))))
    return l1
def areabetweentwoparabolas(a,b):
    m1=(16*a*b)/3
    return m1
def areabetweenparabolaandlatusrectum(a):
    n1=((8*(a**2))/3)
    return n1
def areabetweenarchofsinax(a):
    return 2*a
def areabetweenarchofcosax(a):
    return 2*a
def areaofsphericalsector(r,h,a):
    o1=(22/7)*r*(((2*h)+a))
    return o1
def volumeofsphericalsector(r,h):
    p1=(2*(22/7)*r*r*h)/3
    return p1
def lateralsurfaceareaofsphericalsector(r,h):
    q1=2*(22/7)*r*h
    return q1
def areaofcapsule(r,a):
    r1=(((2*(22/7)*r)*((2*r)+a)))
    return r1
def volumeofcapsule(r,a):
    s1=((22/7)*(r**2)*(((4/3)*r)+a))
    return s1
def areaoftube(r1,r2):
    t1=(22/7)*((r1**2)-(r2**2))
    return t1
def volumeoftube(r1,r2,h):
    u1=(h)*(22/7)*((r1**2)-(r2**2))
    return u1
def areaoftorus(r1,r2):
    v1=((2*(22/7))**2)*(r1*r2)
    return v1
def volumeoftorus(r1,r2):
    w1=((22/7)**2)*2*(r1*r1*r2)
    return w1
def volumeofhollowcylinder(R,r,h):
    x1=((22/7)*h)*((R**2)-(r**2))
    return x1
def areaofhollowcylinder(R,r,h):
    y1=2*(22/7)*((R+r)*(h+R-r))
    return y1
def lateralsurfaceareaofhollowcylinder(R,r,h):
    z1=2*(22/7)*(R+r)*h
    return z1
def areaofhollowsphere(R,r):
    a2=4*(22/7)*((R**2)-(r**2))
    return a2
def volumeofhollowsphere(R,r):
    b2=(4/3)*(22/7)*((R**3)-(r**3))
    return b2


