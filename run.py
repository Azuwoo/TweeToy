import twitter

f = open('text.txt', 'w') # open file write mode

api = twitter.Api(consumer_key='consumer_key',
                  consumer_secret='consumer_key',
                  access_token_key='consumer_key',
                  access_token_secret='consumer_key')


statuses = api.GetUserTimeline(screen_name='@dave_spector')

#statuses = api.GetUserTimeline('dave_spector')
#statuses = api.GetPublicTimeline()  it's removed

print statuses[0].created_at
print statuses[0].text + '\n'

print statuses[1].created_at
print statuses[1].text + '\n'

print statuses[2].created_at
print statuses[2].text + '\n'

for s in statuses:
    f.write(s.text.encode('utf_8'))

# write data
f.close() #close file
