from bson.objectid import ObjectId
import pymongo
class Restaurant:
    def __init__(self) -> None:
        self._client=pymongo.MongoClient("mongodb://localhost:27017/")
        self._db=self._client["hotel"]
        self._food=self._db["Food"]
        self.name="Restaurant name"
    def menu(self):
        return {"Pizza":800,"Burger":600,"Pasta":900,"Sandwich":400}

    def viewAllOrders(self):
        print("\n All Orders")
        print("Order ID\t\t\tTime Stamp\t\t\tCustomer ID\t\t\tFood\tServed")
        for x in self._food.find():
            print(str(x["_id"])+"\t"+str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["food"]+"\t"+str(x["served"]))

    def serveOrder(self,id):
        print("\n")
        try:
            self._food.update_one({"_id":ObjectId(id)},{"$set":{"served":True}})
            print("Order served")
        except Exception as e:
            print(e)


    def viewPendingOrders(self):
        print("\n Pending Orders")
        print("Order ID\t\t\tTime Stamp\t\t\tCustomer ID\t\t\tFood")
        for x in self._food.find({"served":False}):
            print(str(x["_id"])+"\t"+str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["food"])
