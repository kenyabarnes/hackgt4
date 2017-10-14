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
import ffmpeg_normalize as FFMPEG

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
#getTimeline('@realDonaldTrump', 5, False).encode('ascii', 'ignore')
#getStatus()
status= getStatus(918960024256434176)
ent=status['entities']
med=ent['media']

print(med)
string= med[0]
print(string)

print (string['expanded_url'])
cmd='you-get -n' + string['expanded_url']
#cmd='you-get http://www.fsf.org/blogs/rms/20140407-geneva-tedx-talk-free-software-free-society'
proc='hi'
#proc = subprocess.run(["you-get","-n" ,string['expanded_url']], stdout=subprocess.PIPE)
#os.system(cmd)
#print(proc)
#temp =ffmpeg_concat_mp4_to_mp4(proc,"output")
command = "cmd.exe"
stdin=''
stdout=''
proc = subprocess.Popen(command, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
proc.stdin.write(cmd)
print(stdout)
