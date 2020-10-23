def f(x=100, y=100):
   return(x+y, x-y)


x, y = f(y=200, x=100)
print(x, y)
