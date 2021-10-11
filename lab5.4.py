#student id:1201200152
#STUDENT NAME:TEY MEI QUN

def rectangle(width,length):
    r_area=width*length
    return r_area

def traingle(width,length):
    t_area=(width*length)/2
    return t_area

def main():
  width=float(input("Enter width:"))
  length=float(input("Enter length:"))
  rarea=rectangle(width,length)
  tarea=traingle(width,length)
  print("Rectangle area : {:.2f}".format(rarea))
  print("Triangle area : {:.2f}".format(tarea))

i=0
while(i<2):

    main()
    i+=1


