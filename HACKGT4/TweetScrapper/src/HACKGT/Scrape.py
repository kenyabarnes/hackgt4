from twython import Twython
from twython import TwythonStreamer
import sys
import ast
import you_get
import os
import subprocess

#Application Key and Application Secret from app.twitter.com
APP_KEY = 'AzOXf1QIO4LUjbi7zpD0RzH6m'
APP_SECRET = 'tInkuiCumvbsuBcsBje7vi2yfUi4AdQyVKrvm2M429jGcsjcT9'

ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAANQQ2wAAAAAASOUsj2IFaj%2BlQCOPeJiijU0GH50%3Dw9cdMLGIGpiN82aY2AbfTyjvEOSBu8vLrHF6u093CkQ4n7S73m'

OAUTH_TOKEN = '724142590459826176-kpVZJ6mwP1oN3iMp9e3lccY0Rz8rL3M'
OAUTH_TOKEN_SECRET = 'BTw0VhVcp7mws7CzDwGSUwyzpApyIsxxz9Wj8toqzgND7'
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        temp=0
        if True:
            if 'retweet_count' in data:
                temp=data['retweet_count']
                print (temp)
                temp= int(temp)
                print (temp)
            if 'text' in data :
                user= data['user']
                print (data['id_str'])
                print (user['screen_name'])
                print (data['contributors'])
                print (data['retweet_count'])
                print (data['text'].encode('ascii','ignore'))
            if 'media' in data:
                print(data['media'])
        # Want to disconnect after the first result?

        #self.disconnect()
        print('\n')

    def on_error(self, status_code, data):
        print (status_code, data)



def getToken():
    twitter = Twython(APP_KEY, APP_SECRET,  oauth_version=2)
    print (twitter.obtain_access_token())
def getStatus(tweetID):
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        results = twitter.show_status(id=tweetID)
        return results

def getTimeline(screenName, tweetCount, excludeReplies,files):
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    results = twitter.get_user_timeline(screen_name=screenName, count=tweetCount)
    for result in results:
            dataprocess(result,files)

def currentTime():
    currentTime = time.strftime('%Y-%m-%d--%H-%M-%S')
    return currentTime
def dataprocess(status,file):
    ent=status['entities']
    us=status['user']
    temp="lol"
    #why try catch you say. im lazy.
    try:
        ent=status['entities']
        us=status['user']
        has=ent['hashtags']

        try:
            has1=has[0]
            has2=has1['text']
        except:
            has2="N/A"
        try:
            med=ent['media']
            string= med[0]
            videoProcess(string['expanded_url'])

        except:
            string={'expanded_url':'N/A'}
        try:
            typ=status['extended_entities']
            typ1=typ['media']
            typ2=typ1[0]
        except:
            typ2={'type':'Text'}
        string= str(us['screen_name']+" "+status['text']+" "+has2+" "+string['expanded_url']+" "+typ2['type'])+'\n'
        string.encode(sys.stdout.encoding, errors='replace')

        #file.write(str("[{text:" +status['text'] +",intent: None,entities:[{entity: FamilyMember,startPos: 4,endPos: 6}]},"))
        print(string)
        file.write(string)

    except Exception as e:# should never get here if it does we fucked
        print (e)
        print(us['screen_name'],status['text'],"fuck")

def videoProcess(vidURL):
    if(not(vidURL is 'N/A')):
        os.system("you-get "+vidURL)
    return
#steam
stream = MyStreamer(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#stream.statuses.filter(track=' twitter')


output= open("out.txt",'w', encoding='utf-8')
getTimeline('@realDonaldTrump', 5, True,output)
#getStatus()
#status= getStatus(918960024256434176)#(vid) 918960024256434176 (pic) 918894502185787392 (text) 919009334016856065
