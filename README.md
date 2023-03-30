# gw2api

https://wiki.guildwars2.com/wiki/Template:Daily_Fractal_Schedule

https://api.guildwars2.com/v2/achievements/daily

https://api.guildwars2.com/v2/achievements?ids=1981

working script code
https://replit.com/ ### /IndigoLavishWorker

#daily call
https://replit.com/ *** /NeatNegativeHashmaps#main.py

I wanted to know when certain dailies were available.
To do this I leveraged the GW2 API found here.
In order to best accomplish this I set out to discover what ids coincided with the daily activities I was interested in.
I used a python script to check the dailies via the api and save the output with the name and associated ids. That save file also includes the date because I was curious if there was a pattern or loop for when acheivments are available or if it was random (more to come later).
After getting a list of ids of interest, I set out to create a twitter bot that would use python to check the dailies and if the ids match with those of interest, tweets those dailies out so I can see the fun ones without logging in!
at first I hosted the code locally. I then transitioned to using aws lambda to run the daily check and tweeting.

Local files 
