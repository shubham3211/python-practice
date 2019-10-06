class Complex:
  count = 0

  def __init__(self, real, imaginary):
    Complex.count = Complex.count +1
    self.real = real
    self.imaginary = imaginary
  
  def __mul__(self, o):
    r = self.real*o.real - self.imaginary*o.imaginary
    i =  self.real*o.real + self.imaginary*o.imaginary
    c = Complex(r, i)
    return c
  
  def __eq__(self, o):
    return self.real == o.real and self.imaginary == o.imaginary
  
  def noOfObjectsCreated(self):
    return Complex.count
