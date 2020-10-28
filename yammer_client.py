import yampy
import json

access_token = ''

yammer = yampy.Yammer(access_token=access_token)

with open('file.json') as json_file:
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

