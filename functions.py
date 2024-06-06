import time
from urllib.request import urlopen
import re
from sqlite import *

def today(user):
    start = time.time()
    URL = f'https://paceman.gg/stats/api/getSessionStats/?name={user}&hours=24&hoursBetween=5'
    site = urlopen(URL)
    f = str(site.read())
    times = re.findall(r'\d+:\d+|\d+', f)
    return f'Second structres: {times[8]}, avg: {times[9]}; Nether exits: {times[10]}, avg: {times[11]}; Strongholds: {times[12]}, avg: {times[13]}; Ends: {times[14]}, avg: {times[15]} ({round(time.time() - start, 2)}s)'

def enters(user):
    try:
        start = time.time()
        URL = f"https://paceman.gg/stats/api/getSessionNethers/?name={user}&hours=24&hoursBetween=5"
        site = urlopen(URL)
        f = str(site.read())
        temp = re.findall(r'\d\d|\d+', f)
        if int(temp[0]) == 0:
            return (f'No enters for {user}')
        else:
            return (f'{user} has {temp[0]} enters, avg {temp[1]}:{temp[2]} ({round(time.time() - start, 2)}s)')
    except:
        return ("Invalid username, usage: !enters <minecraft username>")
    
def leaders(argument):
    people = {}
    def enters_count(user):
        try:
            URL = f"https://paceman.gg/stats/api/getSessionNethers/?name={user}&hours=16&hoursBetween=5"
            site = urlopen(URL)
            f = str(site.read())
            temp = re.findall(r'\d+', f)
            people[user] = int(temp[0])
        except:
            return
        
    def leaderboard(argument):
        if argument:
            for i in get_group_user(argument):
                enters_count(i[0])
        else:
            for i in get_user():
                enters_count(i[0])
        people_sorted = dict(sorted(people.items(), key=lambda x:x[1], reverse=True))
        first2pairs = {k: people_sorted[k] for k in list(people_sorted)[:5]}
        return str(', '.join('%s : %s' % (k,first2pairs[k]) for k in first2pairs.keys())).replace(" :", ":")
    return leaderboard(argument)

def leaders_alltime(argument):
    people = {}
    def enters_count(user):
        try:
            URL = f"https://paceman.gg/stats/api/getSessionNethers/?name={user}&hours=9999999&hoursBetween=9999999"
            site = urlopen(URL)
            f = str(site.read())
            temp = re.findall(r'\d+', f)
            people[user] = int(temp[0])
        except:
            return
        
    def leaderboard(argument):
        if argument:
            for i in get_group_user(argument):
                enters_count(i[0])
        else:
            for i in get_user():
                enters_count(i[0])
        people_sorted = dict(sorted(people.items(), key=lambda x:x[1], reverse=True))
        first2pairs = {k: people_sorted[k] for k in list(people_sorted)[:5]}
        return str(', '.join('%s : %s' % (k,first2pairs[k]) for k in first2pairs.keys())).replace(" :", ":")
    return leaderboard(argument)