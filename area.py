#area of shape calculator to find the rupee to paint it 
n=input('enter the shape whose area is to be calculated-rectangle/triangle/square/rightangletriangle')
def rectangle(x,y,apm):
    area=x*y
    price=apm*area
    print('The area required is',price,'to get it painted')
def square(x,apm):
    area=x*x
    price=area*apm
    print('The area required is',price,'to get it painted')
def triangle(a,b,c,apm):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    ps=apm*area
    print('The area required is',price,'to get it painted')
def rightangletriangle(b,h,apm):
    area=b*h*0.5
    price=apm*area
    print('The area required is',price,'to get it painted')
if n.lower()=='rectangle':
    t=int(input('Enter the length:'))
    y=int(input('Enter the breadth:'))
    pp=int(input('Enter the prize per sq m:'))
    rectangle(a,b,pp)
if n.lower()=='square':
    s=input('enter the length of square')
    ps=int(input('Enter the prize per sq m:'))
    square(s,ps)
if n.lower()=='triangle':
    a=int(input('enter the length of 1st side:'))
    b=int(input('enter the length of 2nd side:'))
    c=int(input('enter the length of 3rd side:'))
    pr=int(input('Enter the prize per sq m:'))
    triangle(a,b,c,pr)
if n.lower()=='rightangletriangle':
    h=int(input('enter the height of triangle'))
    b=int(input('enter the base of triangle'))
    pt=int(input('Enter the prize per sq m:'))
    rightangletriangle(h,b,pt)
