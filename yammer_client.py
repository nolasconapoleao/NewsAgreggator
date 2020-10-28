import yampy

access_token = ''

yammer = yampy.Yammer(access_token=access_token)

yammer.messages.create("Hello developers", group_id=43795390464,
                       topics=["Python", "API", "Yammer"])
