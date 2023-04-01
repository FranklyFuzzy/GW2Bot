# GW2 Daily Bot

dailyGetter.py - Script automated in task scheduler to run daily after the game dailies reset.

interestingIDs.txt - list of acheivment names and ids that I wanted to build my bot around. I used the output of DailyScraper.py as the source for the data in this text file. The ids from this file are later hard coded into my script in AWS for monitoring.

/AWS/lambda_function.py - Script that uses AWS SSM for creds, checks daily API for hard coded IDs of interest and bot tweets.

/AWS/requests.zip - Required dependancies for requests and tweepy.

See in action [HERE](https://twitter.com/EZ_Dailies_GW2)

Ref:

https://wiki.guildwars2.com/wiki/Template:Daily_Fractal_Schedule

https://api.guildwars2.com/v2/achievements/daily

https://api.guildwars2.com/v2/achievements?ids=1981
