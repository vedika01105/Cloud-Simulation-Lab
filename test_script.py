import datetime

with open("cron_log.txt","a") as f:
    f.write(f"Script ran at {datetime.datetime.now()}\n")
