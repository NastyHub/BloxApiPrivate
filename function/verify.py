import requests as req
import random
import json
import os

path = ""

def convert_name_into_id(name):
    r = req.get(f"https://api.roblox.com/users/get-by-username?username={name}").json()
    try:
        return r["Id"]
    except:
        return None

class verification:
    def __init__(self, userid, discordid):
        self.userid = userid
        self.discordid = discordid
    
    def get_status(self):
        #Assuming valid id was provided
        r = req.get(f"https://users.roblox.com/v1/users/{self.userid}").json()
        try:
            return r["description"]
        except:
            return None
    
    def generate_code(self):
        thislist = [
            "apple",
            "core",
            "happy",
            "salad",
            "juice",
            "pizza",
            "word",
            "world",
            "chicken",
            "rice",
            "spain",
            "america",
            "korea",
            "red",
            "blue",
            "pink",
            "orange",
            "yellow",
            "green",
            "black",
            "white",
            "brown",
            "purple",
            "gray",
            "japan",
            "fashion",
            "code",
            "python",
            "monkey",
            "lion",
            "tiger",
            "bear",
            "cat",
            "dog",
            "pig",
            "cow",
            "elephant",
        ]
        i = 0
        result = ""
        while i <= 7:
            random_element = random.choice(thislist)
            if i == 7:
                result = result + random_element
            else:
                result = result + random_element + " "
            i += 1
        return result
    
    def create_data(self):
        #name: robloxid
        try:
            jsondata = {
                "robloxid" : self.userid
            }

            with open(path+f"/{self.discordid}.json", "w") as f:
                json.dump(jsondata, f, indent=2)
                f.close()
            return 1
        except:
            return 0
    
    def remove_data(self):
        if os.path.isfile(path+f"/{self.discordid}.json"):
            os.remove(path+f"/{self.discordid}.json")
            return 1
        else:
            return 0