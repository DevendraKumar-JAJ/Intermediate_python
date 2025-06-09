try:
  a=5
  b='b'
  print(a+b)
except(TypeError):
  print(TypeError)
  
try:
  a=5
  b=0
  print(a/0)
except ZeroDivisionError:
  print('There is a zero division error')
  
try:
  a=5
  b='c'
  print(a*b) # not a err
  print(a/b) #err
except:
  print("error")


class ValueTooHighError(Exception):
  pass

def test_value(x):
  if x>100:
    raise ValueTooHighError("Value is to high")


test_value(101)#  through error

