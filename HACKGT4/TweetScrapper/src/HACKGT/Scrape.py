'''
Created on Oct 14, 2017

@author: Kenya Barnes
'''
from twython import Twython
import json
import ast


#Application Key and Application Secret from app.twitter.com
APP_KEY = 'AzOXf1QIO4LUjbi7zpD0RzH6m'
APP_SECRET = 'tInkuiCumvbsuBcsBje7vi2yfUi4AdQyVKrvm2M429jGcsjcT9'

#
ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAANQQ2wAAAAAASOUsj2IFaj%2BlQCOPeJiijU0GH50%3Dw9cdMLGIGpiN82aY2AbfTyjvEOSBu8vLrHF6u093CkQ4n7S73m'

OAUTH_TOKEN = '724142590459826176-kpVZJ6mwP1oN3iMp9e3lccY0Rz8rL3M'
OAUTH_TOKEN_SECRET = 'BTw0VhVcp7mws7CzDwGSUwyzpApyIsxxz9Wj8toqzgND7'

def getToken():
    twitter = Twython(APP_KEY, APP_SECRET,  oauth_version=2)
    print (twitter.obtain_access_token())
def getStatus(tweetID):
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        results = twitter.show_status(id=tweetID)
        return results

        '''fp = codecs.open('.\Results\\'+currentTime()+' (STATUS).txt', 'w','utf-8')
        fp.write('Created: '+results['created_at'])
        fp.write('\r\n')
        fp.write(str(results['text']+'\r\n\r\n'))
        fp.close()'''
def getTimeline(screenName, tweetCount, excludeReplies):
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    results = twitter.get_user_timeline(screen_name=screenName, count=tweetCount)
    if tweetCount <= 100:
        for result in results:
            try:
                '''temp= 'Tweet ID: ',esult['id'],'\n Text: ', result['text'],'\n Created: ', result['created_at']
                print((temp))
                '''
                print ('Tweet ID: ', result['id'])
                '''print ('Text: ', result['text'])
                print ('Created: ', result['created_at'])
                print ('===================//===================\n')'''
            except:
                print ("Failed to ")
    else:
        fp = open('TIMELINE.txt', 'w')
        for result in results:
            fp.write('Tweet ID: '+str(result['id'])+'\r\n')
            fp.write('Text: '+result['text']+'\r\n')
            fp.write('Created: '+str(result['created_at'])+'\r\n')
            fp.write('===================//===================\r\n')
def currentTime():
    currentTime = time.strftime('%Y-%m-%d--%H-%M-%S')
    return currentTime
def getTweet(tweetID):
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    return
#getTimeline('@realDonaldTrump', 5, False).encode('ascii', 'ignore')
#getStatus()
status= getStatus(918960024256434176)
ent=status['entities']
med=ent['media']

print(med)
string= med[0]
print(string)
print(ast.literal_eval(string))
