listId=[]
listName=[]
listAddress=[]
listMobile=[]


def addcustomer(id,name,address,mobile):
 listId.append(id)
 listName.append(name)
 listAddress.append(address)
 listMobile.append(mobile)
 print("customer added sucessfully")
 return


def searchcustomer(id):
     if(listId.__contains__(id)):
         i=listId.index(id)
         print("Id= ",listId[i])
         print("Name= ",listName[i])
         print("Address= ", listAddress[i])
         print("Mobile= ", listMobile[i])
         return
     else:
         print("Id not found")




def deletecustomer(id):
   if(listId.__contains__(id)):
     i=listId.index(id)
     listId.pop(i)
     listName.pop(i)
     listAddress.pop(i)
     listMobile.pop(i)
     print("customer deleted sucessfully")
   else:
     print("id not found")
     return


def modifycustomer(id,name,address):
    if(listId. __contains__(id)):
        i=listId.index(id)
        listName[i]=name
        listAddress[i]=address
        print("customer modified sucessfully")
        return
def showcustomer():
    print(listId,listName, listAddress,listMobile)




while(True):

    print("1.add customer \n2. search customer\n 3.delete customer")
    ch=input("enter  your choice  : ")

    if(ch=='1'):
      id=int(input("enter customer id : "))
      name=(input("enter customer name : "))
      address=(input("enter customer address : "))
      mobile=(input ("enter customer  mobile : "))1
      addcustomer(id,name,address,mobile)
      print("customer added sucessfully")

    elif(ch=='2'):
        id = int(input("enter id to be search : "))
        searchcustomer(id)


    elif(ch=="3"):
        id = int(input(" enter customer id to be deleted : "))
        deletecustomer(id)


    elif(ch=="4"):
        id=int(input ("enter id to be modify : "))
        name=input("enter customer name to be modified : ")
        address=input("enter cutomer address to be modified: ")
        modifycustomer(id,name,address)

    elif(ch=="0"):
        print("exit")

    elif(ch==6):
        showcustomer()
