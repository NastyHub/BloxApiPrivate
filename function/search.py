from typing_extensions import IntVar
import requests as req
import os
import json

"""
KEEP WORKING ON IT
"""

path = ""

def convert_name_into_id(name):
    r = req.get(f"https://api.roblox.com/users/get-by-username?username={name}").json()
    try:
        return r["Id"]
    except:
        return None

def check_rank_in_group(userid, groupid):
    r = req.get(f"https://groups.roblox.com/v1/users/{userid}/groups/roles").json()
    hit = False
    for i in r["data"]:
        if i["group"]["id"] == groupid:
            hit = True
            return i["role"]["name"]
    if hit == False:
        return None

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
        try:
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

            rankname = None
            if self.groupid != None:
                groupresult = check_rank_in_group(self.userid, self.groupid)
                if groupresult != None:
                    rankname = groupresult
            
            return name, displayname, id, description, year, month, day, isBanned, pastusername, rankname
        except:
            return None


def smart_user_algorithm(basicdata, groupid=None):
    userid = None
    #Check the basicdata's type
    #<@!631441731350691850>
    if str(basicdata).startswith("<@!") and basicdata.endswith(">"):
        discordid = basicdata[3:-1]
        newpath = path + f"/{discordid}.json"
        if os.path.isfile(newpath):
            with open(newpath) as f:
                jsondata = json.load(f)
                f.close()
            userid = jsondata["robloxid"]
        else:
            return None
    else:
        res = convert_name_into_id(basicdata)
        if res == None:
            try:
                userid = int(basicdata)
            except:
                return None
        else:
            userid = res
    
    data = userdata(userid, groupid)
    return data.get_raw_data()