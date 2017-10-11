print('guess a number and keep it in your head')
print('give me a maximum(y) and minimum(z) range of the no you picked')
y=int(input('enter maximum: '))
z=int(input('enter minimum: '))
m=range(z,y)
n=list(m)
def guess(*x):
    b=len(n)
    c= int (b/2)
    d= n.pop(c)
    print ('the number is: ',d)
guess(n)
input('if my value is not between your given range help me to fix my guess by telling me "too high" or "too low":')




