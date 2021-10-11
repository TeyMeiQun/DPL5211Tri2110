#student id:1201200152
#STUDENT NAME:TEY MEI QUN

print("======================================")
print("                MENU")
print("  1.    Convert centimeter to meter")
print("  2.    Convert meter to centimeter")
print("======================================")

choice=float(input("Enter your choice :"))
if(choice==1):

    def cm_to_meter(centimeter):
        meter=centimeter/100
        return meter

    def get_cm():
        cm=float(input("Enter centimeter :"))
        m=cm_to_meter(cm)
        print("{:.2f} centimeters equals to {:.2f} meter ".format(cm,m))


    get_cm()

elif(choice==2):
  def meter_to_cm(meter):
        centimeter=meter*100
        return centimeter

  def get_m():
        m=float(input("Enter meter :"))
        cm=meter_to_cm(m)
        print("{:.2f} meters equals to {:.2f} centimeter ".format(m,cm))


  get_m()



