# GW2 Daily Bot

I wanted to know when certain dailies were available.
To do this I leveraged the GW2 API found here.
In order to best accomplish this I set out to discover what ids coincided with the daily activities I was interested in.
I used a python script to check the dailies via the api and save the output with the name and associated ids. That save file also includes the date because I was curious if there was a pattern or loop for when acheivments are available or if it was random (more to come later).
After getting a list of ids of interest, I set out to create a twitter bot that would use python to check the dailies and if the ids match with those of interest, tweets those dailies out so I can see the fun ones without logging in!
at first I hosted the code locally. I then transitioned to using aws lambda to run the daily check and tweeting.

Local files that were used for testing and POC

dailyGetter.py - Script automated in task scheduler to run daily after the game dailies reset.

interestingIDs.txt - list of acheivment names and ids that I wanted to build my bot around. I used the output of DailyScraper.py as the source for the data in this text file. The ids from this file are later hard coded into my script in AWS for monitoring.

/AWS/lambda_function.py - Script that uses AWS SSM for creds, checks daily API for hard coded IDs of interest and bot tweets.

/AWS/requests.zip - Required dependancies for requests and tweepy.

See in action: https://twitter.com/EZ_Dailies_GW2

Ref:

https://wiki.guildwars2.com/wiki/Template:Daily_Fractal_Schedule

https://api.guildwars2.com/v2/achievements/daily

https://api.guildwars2.com/v2/achievements?ids=1981
