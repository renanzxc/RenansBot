import json

def learnName(chatID,name):
    try:
        with open('users.json') as json_file:
            users = json.load(json_file)
        if(chatID in users):
            users[chatID]['name'] = name
            with open('users.json', 'w') as json_file:
                json.dump(users, json_file)
            return users[chatID]['name']
        else:
            users.update({chatID: {'name': name}}) 
            with open('users.json', 'w') as json_file:
                json.dump(users, json_file)
            return users[chatID]['name']
    except: # Runs only when bot learns first name
        users = {}
        users.update({chatID: {'name': name}}) 
        with open('users.json', 'w') as json_file: # Create the json file 
                json.dump(users, json_file)
        return users[chatID]['name']

def checkName(chatID):
    try:
        with open('users.json') as json_file:
            users = json.load(json_file)
        if(chatID in users):
            with open('users.json', 'w') as json_file:
                json.dump(users, json_file)
            return users[chatID]['name']
        else:
            return None
    except:
        learnName(chatID,None)