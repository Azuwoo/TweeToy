import twitter
import os
import config

f = open('text.txt', 'w') # open file write mode

api = twitter.Api(                                                                                                                                                        
    consumer_key = config.twDict['consumer_key'],
    consumer_secret = config.twDict['consumer_secret'],
    access_token_key = config.twDict['access_token_key'],
    access_token_secret = config.twDict['access_token_secret']
)

statuses = api.GetUserTimeline(screen_name='@dave_spector')

#statuses = api.GetUserTimeline('dave_spector')
#statuses = api.GetPublicTimeline()  it's removed

print statuses[0].created_at
print statuses[0].text + '\n'

for s in statuses:
    f.write(s.text.encode('utf_8'))

# write data
f.close() #close file
