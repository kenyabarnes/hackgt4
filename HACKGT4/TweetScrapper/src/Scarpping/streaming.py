'''
Created on Jun 22, 2017

@author: joshua
'''


from twython import TwythonStreamer

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
                user= (data['user'])
                print (data['id_str'])
                print (user['screen_name'])
                print (data['contributors'])
                print (data['retweet_count'])
                print (data['text'].encode('ascii','ignore'))
        # Want to disconnect after the first result?
        
        #self.disconnect()
        print('\n')

    def on_error(self, status_code, data):
        print (status_code, data)

# Requires Authentication as of Twitter API v1.1
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream.statuses.filter(track='#MAGA')
#stream.user()
# Read the authenticated users home timeline
# (what they see on Twitter) in real-time
#stream.site(follow='twitter')
