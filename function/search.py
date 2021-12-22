from typing_extensions import IntVar
import requests as req

def convert_name_into_id(name):
    r = req.get(f"https://api.roblox.com/users/get-by-username?username={name}").json()
    return r

def dividetime(format):
    datelist = format[:10].split("-")
    year = datelist[0]
    month = datelist[1]
    day = datelist[2]
    return year, month, day

class userdata:
    def __init__(self, userid, groupid=None):
        self.userid = userid
        self.groupid = groupid
    
    def get_raw_data(self):
        r = req.get(f"https://users.roblox.com/v1/users/{self.userid}").json()
        description = r["description"]
        created = r["created"]
        isBanned = r["isBanned"]
        id = r["id"]
        name = r["name"]
        displayname = r["displayName"]

        year, month, day = dividetime(created)

        r = req.get(f"https://users.roblox.com/v1/users/{self.userid}/username-history?limit=10&sortOrder=Asc").json()
        pastusername = []
        if len(r["data"]) == 0:
            pass
        else:
            for i in r["data"]:
                pastusername.append(i["name"])
        
        return name, displayname, id, description, year, month, day, isBanned, pastusername


def smart_user_algorithm(basicdata, groupid=None):
    userid = None
    #Check the basicdata's type
    #<@!631441731350691850>
    if basicdata.startswith("<@!") and basicdata.endswith(">"):
        discordid = basicdata[3:-1]
        #extract discordid into userid
    else:
        res = convert_name_into_id(basicdata)
        try:
            userid = res["Id"]
        except:
            try:
                userid = int(basicdata)
            except:
                return None
    
    data = userdata(userid, groupid)
    data.get_raw_data()