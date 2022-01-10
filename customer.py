from datetime import datetime
from bson.objectid import ObjectId
import pymongo
from restaurant import Restaurant
from clubhouse import ClubHouse
class Customer:
    
    def __init__(self,id=None) -> None:
        self._client=pymongo.MongoClient("mongodb://localhost:27017/")
        self._db=self._client["hotel"]
        self._bookings=self._db["Bookings"]
        self._customers=self._db["Customers"]
        self._food=self._db["Food"]
        self._services=self._db["Services"]
        if (id==None):
            self.name=None
            self.email=None
            self.phone=None
            self.cid=None
            self.login()
        else:
            self.cid=id
            user=self._customers.find_one({"_id":ObjectId(self.cid)})
            self.name=user["name"]
            self.email=user["email"]
            self.phone=user["phone"]
            self.checkedIn=user["checkedIn"] if "checkedIn" in user else False
    def login(self):
        print("\n")
        while True:
            print("Please enter email id")
            email=input()
            # email="a@gmail.com"
            user=self._customers.find_one({"email":email})
            if(user==None):
                print("Signing up new user")
                print("Please enter your name")
                name=input()
                print("Please enter your phone number")
                phone=input()
                print("Please enter a password")
                password=input()
                self._customers.insert_one({"name":name,"email":email,"phone":phone,"password":password})
                print("User created")
                break
            else:
                print("Please enter your password")
                password=input()
                # password="a"
                if(password==user["password"]):
                    print("Login Successful")
                    self.name=user["name"]
                    self.email=user["email"]
                    self.phone=user["phone"]
                    self.cid=str(user["_id"])
                    self.checkedIn=user["checkedIn"] if "checkedIn" in user else False
                    break
                else:
                    print("Login Failed")
    def checkIn(self):
        self._customers.update_one({"_id":ObjectId(self.cid)},{"$set":{"checkedIn":True}})
        self.checkedIn=True

    def makeBooking(self):
        print("\n")
        while True:
            print("Enter -1 at any time to go back")
            day=int(input("Enter Day: "))
            if day==-1:
                break

            month=int(input("Enter Month: "))
            if month==-1:
                break

            year=int(input("Enter Year: "))
            if year==-1:
                break
            try:
                self._bookings.insert_one({"customer_id":self.cid,"name":self.name,"email":self.email,"phone":self.phone,"date":datetime(year,month,day),"room":None})
                break
            except Exception as e:
                print(e)

    def listBookings(self):
        print("\nBookings")
        bookings=self._bookings.find({"customer_id":self.cid})
        if self._bookings.count_documents({"customer_id":self.cid})==0:
            print("No confirmed bookings")
        else:
            for x in bookings:
                print(x["name"]+"\t\t"+x["email"]+"\t\t"+str(x["phone"])+"\t\t"+str(x["date"])+"\t\t"+("Room No :"+str(x["room"]) if x["room"]!=None else "Not Confirmed"))
        return bookings
    def listConfirmedBookings(self):
        print("\nConfirmed Bookings:")
        bookings=list(self._bookings.find({"customer_id":self.cid,"room":{'$ne':None}}))
        if self._bookings.count_documents({"customer_id":self.cid,"room":{'$ne':None}})==0:
            print("No confirmed bookings")
        else:
            index=0
            for x in bookings:
                print(str(index)+")\t\t"+x["name"]+"\t\t"+x["email"]+"\t\t"+str(x["phone"])+"\t\t"+str(x["date"])+"\t\t"+("Room No :"+str(x["room"]) if x["room"]!=None else "Not Confirmed"))
                index+=1
        
        return bookings

    def orderFood(self):
        print("\nMenu")
        menu=Restaurant().menu()
        index=0
        for key,value in menu.items():
            print(str(index)+". "+key+"\t"+str(value))
            index+=1
        while True:
            print("Enter -1 at any time to go back")
            food=int(input("Enter Food index: "))
            if food==-1:
                break
            elif food>=len(menu):
                print("Invalid index")
                continue
            try:
                key=list(menu.keys())[food]
                print(key)
                self._food.insert_one({"customer_id":self.cid,"timestamp":datetime.now(),"food":key,"served":False})
                print("Food Ordered\n")
                break
            except Exception as e:
                print(e)

    def listFoodOrders(self):
        orders=self._food.find({"customer_id":self.cid})
        if self._food.count_documents({"customer_id":self.cid})==0:
            print("No food orders")
        else:
            print("\nFood Orders")
            print("Timestamp\t\t\t\tFood\t\tServed")
            for x in orders:
                print(str(x["timestamp"])+"\t\t"+str(x["food"])+"\t\t"+str(x["served"]))
        return orders

    def requestRoomService(self):
        print("\n")
        self._services.insert_one({"customer_id":self.cid,"timestamp":datetime.now(),"service":"Room Service","fulfilled":False})
        print("Request successful")

    def requestHouseKeeping(self):
        print("\n")
        self._services.insert_one({"customer_id":self.cid,"timestamp":datetime.now(),"service":"Housekeeping","fulfilled":False})
        print("Request successful")

    def requestClubHouseService(self):
        print("\n Clubhouse Menu")
        menu=ClubHouse().menu()
        index=0
        for key,value in menu.items():
            print(str(index)+". "+key+"\t"+str(value))
            index+=1
        while True:
            print("Enter -1 at any time to go back")
            service=int(input("Enter Service index: "))
            if service==-1:
                break
            elif service>=len(menu):
                print("Invalid index")
                continue
            try:
                key=list(menu.keys())[service]
                self._services.insert_one({"customer_id":self.cid,"timestamp":datetime.now(),"service":key,"fulfilled":False})
                break
            except Exception as e:
                print(e)
    def listServices(self):
        services=self._services.find({"customer_id":self.cid})
        if self._services.count_documents({"customer_id":self.cid})==0:
            print("No services requested")
        else:
            print("\nRequested Services")
            print("Timestamp\t\t\t\tService\t\tFulfilled")
            for x in services:
                print(str(x["timestamp"])+"\t\t"+str(x["service"])+("\t\t" if (x["service"]=="Spa" or x["service"]=="Pool") else "\t")+str(x["fulfilled"]))
        return services

