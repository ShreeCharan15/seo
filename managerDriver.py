from manager import Manager
manager=Manager()
choice=0
while choice!=-1:
    print("\nEnter -1 at any stage to exit")
    print("1. View Booking Requests")
    print("2. Acept Booking Request")
    print("3. Reject Booking Request")
    print("4. List Customers")
    print("5. List Staff")
    print("6. Allot tasks to staff")

    choice=int(input())
    if choice==-1:
        break
    elif choice==1:
        manager.listBookings()
    elif choice==2:
        b=manager.listBookings()
        if len(b)==0:
            print("No booking requests")
            break
        else:
            while True:
                print("Enter the index of the booking request you want to accept")
                index=int(input())
                if index==-1:
                    break
                elif index>=len(b):
                    print("Please enter a valid index")
                    continue
                else:
                    rn=input("Enter room no: ")
                    manager.acceptBooking(b[index]["_id"],rn)
                    break
    elif choice==3:
        b=manager.listBookings()
        if len(b)==0:
            print("No booking requests")
            break
        else:
            while True:
                print("Enter the index of the booking request you want to reject")
                index=int(input())
                if index==-1:
                    break
                elif index>=len(b):
                    print("Please enter a valid index")
                    continue
                else:
                    manager.rejectBooking(b[index]["_id"])
                    break
    elif choice==4:
        manager.listCustomers()
    elif choice==5:
        manager.listStaff()
    elif choice==6:
        s=manager.listStaff()
        if len(s)==0:
            print("No staff")
            break
        else:
            while True:
                print("Enter the index of the staff you want to allot tasks to")
                index=int(input())
                if index==-1:
                    break
                elif index>=len(s):
                    print("Please enter a valid index")
                    continue
                else:
                    task=input("Enter task: ")
                    manager.allotTask(s[index]["_id"],task)
                    break
