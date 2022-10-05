## Assignment 6: crontab

### Crontab Commands and Syntax

- Once a day: 0 0 * * * /usr/bin/python3 /home/israelmiller/crontab/bitcoinprice.py
- On sunday at 10pm: 0 22 * * 0 /usr/bin/python3 /home/israelmiller/crontab/bitcoinprice.py
- Once at the end of every quarter: 0 0 1 */3 * /usr/bin/python3 /home/israelmiller/crontab/bitcoinprice.py

### Commands needed to set up the crontab jobs:

- To see current crontab jobs: crontab -l
- To edit crontab jobs: crontab -e
- to reload crontab service: sudo service cron reload



