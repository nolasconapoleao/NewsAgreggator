import yampy
import json

file = open('ctwCrawler/publisher/access-token.txt', 'r')
access_token = file.readlines()[0].rstrip('\n')
print(access_token)

yammer = yampy.Yammer(access_token=access_token)

with open('result.json') as json_file:
    data = json.load(json_file)
    for row in data:
        domain = row['domain']
        for link in row['url']:
            if not 'http' in link:
                link = domain + link

            #TODO: CHECK if there's link was already pushed
            yammer.messages.create(link,
                                   group_id=43795390464,
                                   topics=["CTW", domain]
                                   )
