# birthdays

A simple daily job for wishing people "Happy Birthday" on slack.

## Usage

Set up a config file.

Example: `people.conf`

```conf
[DEFAULT]
message_url = https://www.alexrecker.com/vids/2021-09-07-fish.webm
webhook_url = https://hooks.slack.com/services/SUPER69/SECRET420/INCOMINGWEBHOOK

[Alex]
month = 9
day = 29
```

Then run the script!

```shell
CONFIG_FILE_PATH="people.conf" python ./birthdays.py
```
