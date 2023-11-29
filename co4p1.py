class Rectangle:
  def __init__(self,length,breadth):
     self.breadth=breadth
     self.length=length
  def area(self):
     return self.length*self.breadth
  def perimeter(self):
     return 2*(self.length+self.breadth)
print("First rectangle")
length=int(input("length: "))        	
breadth=int(input("breadth: "))
rectangle1=Rectangle(length,breadth)
ar1=rectangle1.area()
print("Area of rectangle1 is ",rectangle1.area())
print("Perimeter of rectangle1 is ",rectangle1.perimeter())
print("Second rectangle")
length=int(input("length: "))        	
breadth=int(input("breadth: "))
rectangle2=Rectangle(length,breadth)
ar2=rectangle2.area()
print("Area of rectangle2 is ",rectangle2.area())
print("Perimeter of rectangle2 is ",rectangle2.perimeter())
if(ar1>ar2):
  print("Rectangle1 is greater")
elif(ar2>ar1):
  print("Recatngle2 is greater")
else:
  print("Both are same")    
