import json
import random

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
            return users[chatID]['name']
        else:
            return None
    except:
        learnName(chatID,None)

def learnPhrase(userPhrase, botPhrase):
    try:
        with open('phrases.json') as json_file:
            phrases = json.load(json_file)
        if(userPhrase in phrases):
            size = len(phrases[userPhrase])
            phrases[userPhrase][size+1] = botPhrase
            with open('phrases.json', 'w') as json_file:
                json.dump(phrases, json_file)
            return True
        else:
            phrases.update({userPhrase: {1: botPhrase}}) 
            with open('phrases.json', 'w') as json_file:
                json.dump(phrases, json_file)
            return True
    except: # Runs only when bot learns first phrase
        phrases = {}
        phrases.update({userPhrase: {1: botPhrase}}) 
        with open('phrases.json', 'w') as json_file: # Create the json file 
            json.dump(phrases, json_file)
        return True

def checkPhrase(userPhrase):
    try:
        with open('phrases.json') as json_file:
            phrases = json.load(json_file)
        if(userPhrase in phrases):
            size = len(phrases[userPhrase])
            return phrases[userPhrase][str(random.randint(1,size))]
        else:
            return False
    except:
        return False