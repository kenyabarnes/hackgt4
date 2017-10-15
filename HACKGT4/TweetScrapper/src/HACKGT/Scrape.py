'''
Created on Oct 14, 2017

@author: Kenya Barnes
'''
from twython import Twython
import json
import ast
import you_get
import os
import subprocess


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

def getTimeline(screenName, tweetCount, excludeReplies,files):
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    results = twitter.get_user_timeline(screen_name=screenName, count=tweetCount)
    for result in results:
            dataprocess(result,files)

def currentTime():
    currentTime = time.strftime('%Y-%m-%d--%H-%M-%S')
    return currentTime

def ffmpeg_concat_mp4_to_mp4(files, output='output.mp4'):
    print('Merging video parts... ', end="", flush=True)
    # Use concat demuxer on FFmpeg >= 1.1
    if FFMPEG == 'ffmpeg' and (FFMPEG_VERSION[0] >= 2 or (FFMPEG_VERSION[0] == 1 and FFMPEG_VERSION[1] >= 1)):
        concat_list = generate_concat_list(files, output)
        params = [FFMPEG] + LOGLEVEL + ['-y', '-f', 'concat', '-safe', '-1',
                                        '-i', concat_list, '-c', 'copy',
                                        '-bsf:a', 'aac_adtstoasc', output]
        subprocess.check_call(params, stdin=STDIN)
        os.remove(output + '.txt')
        return True

    for file in files:
        if os.path.isfile(file):
            params = [FFMPEG] + LOGLEVEL + ['-y', '-i']
            params.append(file)
            params += ['-c', 'copy', '-f', 'mpegts', '-bsf:v', 'h264_mp4toannexb']
            params.append(file + '.ts')

            subprocess.call(params, stdin=STDIN)

    params = [FFMPEG] + LOGLEVEL + ['-y', '-i']
    params.append('concat:')
    for file in files:
        f = file + '.ts'
        if os.path.isfile(f):
            params[-1] += f + '|'
    if FFMPEG == 'avconv':
        params += ['-c', 'copy', output]
    else:
        params += ['-c', 'copy', '-absf', 'aac_adtstoasc', output]

    subprocess.check_call(params, stdin=STDIN)
    for file in files:
        os.remove(file + '.ts')
    return True
def dataprocess(status,file):
    ent=status['entities']
    us=status['user']
    temp="lol"
    #print(status)
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
        print(us['screen_name'],status['text'], has2,string['expanded_url'],typ2['type'])

        file.write(str("[{text:" +status['text'] +",intent: None,entities:[{entity: FamilyMember,startPos: 4,endPos: 6}]},"))


    except Exception as e:# should never get here if it does we fucked
        print (e)
        print(us['screen_name'],status['text'],"fuck")

def videoProcess(vidURL):
    if(not(vidURL is 'N/A')):
        os.system("you-get "+vidURL)
    return
output= open("out.txt",'w')
getTimeline('@realDonaldTrump', 20, False,output)
#getStatus()
#status= getStatus(918960024256434176)#(vid) 918960024256434176 (pic) 918894502185787392 (text) 919009334016856065
#print(status)
#dataprocess(status,output)
#videoProcess(string['expanded_url'])
#os.system("you-get https://m.twitter.com/realDonaldTrump/status/918960024256434176/video/1")


'''cmd='you-get -n' + string['expanded_url']
#cmd='you-get http://www.fsf.org/blogs/rms/20140407-geneva-tedx-talk-free-software-free-society'
proc='hi'
#proc = subprocess.run(["you-get","-n" ,string['expanded_url']], stdout=subprocess.PIPE)
os.system(cmd)
#print(proc)
#temp =ffmpeg_concat_mp4_to_mp4(proc,"output")
command = "cmd.exe"
stdin=''
stdout=''
proc = subprocess.Popen(command, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
proc.stdin.write(cmd)
print(stdout)'''
