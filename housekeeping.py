from bson.objectid import ObjectId
from staff import Staff
class HouseKeeping(Staff):
    def __init__(self) -> None:
        super().__init__(id=id)
        self._services=self._db["Services"]
    def viewRequests(self):
        reqs=self._services.find({"service":"Housekeeping","fulfilled":False})
        print("\nHousekeeping Requests")
        print("Request ID\t\t\tTime Stamp\t\t\tCustomer ID\t\t\tService")
        for x in reqs:
            print(str(x["_id"])+"\t"+str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["service"])
        return reqs


    def fulfillRequest(self,id):
        print("\n")
        try:
            self._services.update_one({"_id":ObjectId(id)},{"$set":{"fulfilled":True}})
            print("Request Fulfilled")
        except Exception as e:
            print(e)