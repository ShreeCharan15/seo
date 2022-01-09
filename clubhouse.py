from bson.objectid import ObjectId
import pymongo
class ClubHouse:
    def __init__(self) -> None:
        self._client=pymongo.MongoClient("mongodb://localhost:27017/")
        self._db=self._client["hotel"]
        self._services=self._db["Services"]
        self.name="Clubhouse"
    def menu(self):
        return {"Pool":800,"Gym":600,"Spa":900}

    def viewAllRequests(self):
        print("\nAll Requests")
        print("Time Stamp\t\t\tCustomer ID\t\t\tService\t\tFulfilled")
        # print("Request ID\t\t\tTime Stamp\t\t\tCustomer ID\t\t\tService\t\tFulfilled")
        for x in self._services.find({"service":{"$nin":["Housekeeping","Room Service"]}}):
            print(str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["service"]+"\t\t"+str(x["fulfilled"]))
            # print(str(x["_id"])+"\t"+str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["service"]+"\t\t"+str(x["fulfilled"]))

    def fulfilRequest(self,id):
        print("\n")
        try:
            self._services.update_one({"_id":ObjectId(id)},{"$set":{"fulfilled":True}})
            print("Request Fulfilled")
            #TODO:UPDATE BILL
        except Exception as e:
            print(e)


    def viewPendingRequests(self):
        print("\nPending Requests")
        # print("Request ID\t\t\tTime Stamp\t\t\tCustomer ID\t\t\tService")
        print("Index\t\tTime Stamp\t\t\tCustomer ID\t\t\tService")
        index=0
        pr=list(self._services.find({"fulfilled":False,"service":{"$nin":["Housekeeping","Room Service"]}}))
        if len(pr)==0:
            print("No pending requests")
        else:
            for x in pr:
                # print(str(x["_id"])+"\t"+str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["service"])
                print(str(index)+"\t\t"+str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["service"])
                index+=1
        return pr

