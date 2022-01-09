from customer import Customer
cust=Customer()
def checkin():
    while True:
        try:
            print("\nEnter -1 at any stage to exit")
            print("1. Make a booking")
            print("2. List your bookings")
            print("3 Check in")
            choice=int(input())
            if choice==-1:
                break
            elif choice==1:
                cust.makeBooking()
            elif choice==2:
                cust.listBookings()
            elif choice==3:
                bookings=cust.listConfirmedBookings()
                if len(bookings)==0:
                    print("Please wait until your booking is accepted")
                    break
                else:
                    while True:
                        print("Enter the index of the booking you want to check in")
                        index=int(input())
                        if(index==-1):
                            break
                        elif(index>=len(bookings)):
                            print("Please enter a valid index")
                        else:
                            print("Check in complete!")
                            cust.checkIn()
                            return 
        except Exception as e:
            print(e)


def showMenu():
    print("\nEnter -1 at any stage to exit")
    print("1. Order Food")
    print("2. View Food Orders")
    print("3. Request Room Service")
    print("4. Request Housekeeping")
    print("5. Request Club House services")
    print("6. List requested Services\n")

choice=0
while choice!=-1:
    if(cust.checkedIn):
        showMenu()
        choice=int(input("Enter your choice: "))
        if choice==-1:
            break
        elif choice==1:
            cust.orderFood()
        elif choice==2:
            cust.listFoodOrders()
        elif choice==3:
            cust.requestRoomService()
        elif choice==4:
            cust.requestHouseKeeping()
        elif choice==5:
            cust.requestClubHouseService()
        elif choice==6:
            cust.listServices()
        else:
            print("Invalid choice")
    else:
        checkin()