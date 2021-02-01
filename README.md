# CoinGecko

## Summary
An automated script to get daily rewards from CoinGecko. Thanks to Heroku, the deployment is stress-free and easy. All the deployment is done in one click (almost). 

## Deployment

1. Click the **Deploy to Heroku** Button below

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

2. Setup the `USERNAME` and `PASSWORD` variables

Update the `USERNAME` and `PASSWORD` values with your CoinGecko username and password. 

<img src="https://i.imgur.com/jV8a7fQ.png" width="600px">



3. Deploy and Build

Hit **Deploy App** and wait until the build is finished. Click `Manage App` redirects to the main page.

<img src="https://i.imgur.com/UnHlu8Q.png" width="600px">

4. Setup Schedules

* Click `Resources` > `Heroku Scheduler` > `Create Job`
* Choose `Every day at ...` with anytime you like
* Copy and paste `python main.py` in the command input below
* Save job

<img src="https://i.imgur.com/hj6adwI.png">


5. All set!

## Credit

Inspired by: [CryoliteZ/1point3auto](https://github.com/CryoliteZ/1point3auto)

I found the script for receiving 1point3auto rewards daily and believe that the same concept could be applied on getting CoinGecko's daily checkin rewards.