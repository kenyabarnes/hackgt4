'''
Created on Jun 21, 2017

@author: joshua
'''
from twython import Twython
import time
import codecs

#Fill these with your application key and application secret, taken from Twitter.
APP_KEY ='oRJBbEynRmneoi4W5Ljppp2j3' 
#YOUR_APP_KEY
APP_SECRET ='RrdUobkR8gLv3CjbP68SINyOhk6p0uZ8u2Elc4h0O8DWiOkpjZ'
#'YOUR_APP_SECRET'

#Use getToken() to get your application-only access token, then replace it here.
ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAJHf1AAAAAAAM7KCyABf4Hd4iNSa4DNgewvppno%3DwNjJJHVa1WhDmjbrtbSAvpSUf4tgqfuvEFwy7VeSTwti1zC90T'
#'YOUR_ACCESS_TOKEN'

#Fill these with your oauth token and token secrets, taken from your Twitter.
OAUTH_TOKEN = '1385580451-y593FuyJ50ZmbdFcgGioLwYtf33DF8Lb5f4OTtV'
OAUTH_TOKEN_SECRET = 'U2lxB00PfcToAVuW0WTR21uCGZVIh4hGsUmkhYZbWFHOJ'

def getToken():
    twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2);
    print (twitter.obtain_access_token())

def getTimeline(screenName, tweetCount, excludeReplies):
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    results = twitter.get_user_timeline(screen_name=screenName, count=tweetCount)
    if tweetCount <= 100:
        for result in results:
            try:
                temp= 'Tweet ID: %s \n Text: ', result['text'],'\nCreated: ', result['created_at']
                print((temp))
                '''
                print ('Tweet ID: ', result['id'])
                print ('Text: ', result['text'])
                print ('Created: ', result['created_at'])
                print ('===================//===================\n')'''
            except:
                x=0
    else:
        fp = open('TIMELINE.txt', 'w')
        for result in results:
            fp.write('Tweet ID: '+str(result['id'])+'\r\n')
            fp.write('Text: '+result['text']+'\r\n')
            fp.write('Created: '+str(result['created_at'])+'\r\n')
            fp.write('===================//===================\r\n')

def getStatus(tweetID):
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        results = twitter.show_status(id=tweetID)
        fp = codecs.open('.\Results\\'+currentTime()+' (STATUS).txt', 'w','utf-8')
        fp.write('Created: '+results['created_at'])
        fp.write('\r\n')
        fp.write(str(results['text']+'\r\n\r\n'))
        fp.close()
        

def getFollowers(screenName, userCount = 200, skipStatus = True):
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    results = twitter.get_followers_list(screen_name=screenName, count=userCount, skip_status=skipStatus)

    if userCount <= 5:
        for result in results['users']:
            print ('ID: ', result['id'])
            print ('Screen Handle: ', result['screen_name'])
            print ('===================//===================')
            print (' ')
    else:
        fp = codecs.open('.\Results\\'+currentTime()+' (FOLLOWERS).txt', 'w', "utf-8")
        for result in results['users']:
            fp.write('ID: '+str(result['id'])+'\r\n')
            fp.write('Screen Handle: '+result['screen_name']+'\r\n')
            fp.write('===================//===================\r\n')

def getFollowing(screenName, userCount = 200,skipStatus = True):
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    results = twitter.get_friends_list(screen_name=screenName, count=userCount, skip_status=skipStatus)
    if userCount <= 5:
        for result in results['users']:
            print ('ID: ', result['id'])
            print ('Screen Handle: ', result['screen_name'])
            print ('===================//===================')
            print (' ')
    else:
        fp = codecs.open('.\Results\\'+currentTime()+' (FOLLOWING).txt', 'w', "utf-8")
        for result in results['users']:
            fp.write('ID: '+str(result['id'])+'\r\n')
            fp.write('Screen Handle: '+result['screen_name']+'\r\n')
            fp.write('===================//===================\r\n')

def currentTime():
    currentTime = time.strftime('%Y-%m-%d--%H-%M-%S')
    return currentTime

def getHastTagSearch(hashtag,count):
    t = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    search = t.search(hashtag,count)
    tweets = search['statuses']
    return tweets
print (getTimeline('@realDonaldTrump', 10, True))

    
    
    
    