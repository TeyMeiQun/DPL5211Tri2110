#student id:1201200152
#STUDENT NAME:TEY MEI QUN

def get_bonus(sold,salary):

    if(sold>1000):
        bonus=20/100*salary
    elif(sold>500 and sold<1001):
        bonus=10/100*salary
    return bonus

def get_nett_salary(bonus,salary):
    nett=bonus+salary
    return nett
def display(id,salary,sold,bonus,nett):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("               SALARY SLIP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Staff ID                : ",id)
    print("Staff salary            :  RM {:.2f}".format(salary))
    print("Units sold              :  ",sold)
    print("Bonus                   :  RM {:.2f}".format(bonus))
    print("Nett Salary             :  RM {:.2f}".format(nett))


def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                DATA ENTRY")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    id=input("Enter staff id          :")
    salary=float(input("Enter staff salary      : RM"))
    sold=int(input("Enter total units sold  : "))
    bonus=get_bonus(sold,salary)
    nett=get_nett_salary(bonus,salary)
    display(id,salary,sold,bonus,nett)

main()



