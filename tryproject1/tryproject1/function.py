import  math


def greating(hotel, jobtitle):
    print('Hello I am Roman', jobtitle,  ' of this' , hotel , 'hotel')
    print('May I help You')
greating('Lambada', jobtitle='manager')


def multiply(a,b):
    print(a//b)
multiply(9,2)




# Function for volume of cylinder

#V=πr2h

#V=πr^2h
r = float(input('Radius of cilinder: '))
h = float(input('Height of cilinder: '))
def volume_of_cilinder(radius, height):
  volume = math.pi*radius**2*height
  return volume
v = volume_of_cilinder(r, h)
print('Volume cilinder of: ', v)

