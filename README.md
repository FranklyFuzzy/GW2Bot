# GW2 Daily Bot

dailyGetter.py - Script automated in task scheduler to run daily after the game dailies reset.

interestingIDs.txt - list of acheivment names and ids harvested by dailyGetter.

/AWS/lambda_function.py - Script running in lambda that uses AWS SSM for creds, checks daily API for hard coded IDs and tweets results.

/AWS/requests.zip - Required dependancies for requests and tweepy.

See in action [HERE](https://twitter.com/EZ_Dailies_GW2)

Ref:

https://wiki.guildwars2.com/wiki/Template:Daily_Fractal_Schedule

https://api.guildwars2.com/v2/achievements/daily

https://api.guildwars2.com/v2/achievements?ids=1981
