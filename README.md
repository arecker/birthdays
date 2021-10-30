# birthdays

A simple daily job for wishing people "Happy Birthday" on slack.

## Usage

Set up a config file.

Example: `people.conf`

```conf
[DEFAULT]
webhook_url = https://hooks.slack.com/services/SUPER69/SECRET420/INCOMINGWEBHOOK
channel = #birthdays
emoji = :reckerbot:
username = reckerbot

[Alex]
month = 9
day = 29
message_url = https://youtu.be/Y6JnYnA9Tzo
```

Then run the script every day!

![](./screenshot.png)

```shell
CONFIG_FILE_PATH="people.conf" python ./birthdays.py
```

## Backup

Save configuration to pass.

    $ make save
    saving people.conf to pass://birthdays
    cat people.conf | pass insert -f -m "birthdays"
    Enter contents of birthdays and press Ctrl+D when finished:
    
    [master 4d93d27] Add given password for birthdays to store.
     1 file changed, 0 insertions(+), 0 deletions(-)
     rewrite birthdays.gpg (100%)

Load configuration from pass.

    arecker@25732-arecker:~/src/birthdays$ make load
    loading people.conf from pass://birthdays
    pass birthdays > people.conf
