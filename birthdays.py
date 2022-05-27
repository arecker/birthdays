import configparser
import datetime
import json
import logging
import os
import platform
import random
import sys
import urllib.error
import urllib.parse
import urllib.request

logging.basicConfig(stream=sys.stderr,
                    level=logging.INFO,
                    format='birthdays: %(message)s')


def load_config(path=''):
    config = configparser.ConfigParser()
    config.read(path)
    logging.info('loaded %d section(s) from config %s', len(config.sections()),
                 path)
    return config


def build_message(name, message_url):
    variations = [
        'Hey, happy birthday to {}!',
        'HAPPY BIRTHDAY {}!!!',
        '{}.  IT IS YOUR BIRTHDAY.',
        'Guess who was born today.  {}, that\'s who.',
        'Hey everyone, let\'s wish {} a happy birthday!',
    ]
    message = random.choice(variations).format(name)
    message += '\n' + message_url
    return message


def open_request(request, data, encoding):
    try:
        response = urllib.request.urlopen(request)
        response_data = response.read().decode(encoding)
        response_data = json.loads(data)
        logging.info('webhook returned HTTP: %d %s, data: %s', response.code,
                     response.reason, response_data)
    except urllib.error.HTTPError as e:
        error_data = e.read().decode(encoding)

        try:
            error_data = json.loads(error_data)
        except json.decoder.JSONDecodeError:
            error_data = '"' + error_data + '"'

        logging.error('webhook returned HTTP %d: %s, data: %s', e.code,
                      e.reason, error_data)


def post(name, section, encoding='utf-8'):
    headers = {'Content-type': 'application/json'}
    data = {
        'username': section['username'],
        'channel': section['channel'],
        'icon_emoji': section['emoji'],
        'text': build_message(name=name, message_url=section['message_url']),
    }
    data = json.dumps(data)
    data = data.encode(encoding)
    request = urllib.request.Request(headers=headers,
                                     url=section['webhook_url'],
                                     data=data)
    open_request(request, data, encoding=encoding)


def main():
    logging.info('starting script with python %s (%s)',
                 platform.python_version(), sys.executable)

    config = load_config(
        path=os.environ.get('CONFIG_FILE_PATH', 'people.conf'))
    today = datetime.date.today()
    logging.info('the current date is %s', today)

    for name, info in config.items():
        if name == 'DEFAULT':
            continue

        is_today = int(info['day']) == today.day and int(
            info['month']) == today.month

        if is_today:
            logging.info('building birthday message for %s', name)
            post(name=name, section=info)
        else:
            logging.info('skipping %s, not birthday yet', name)


if __name__ == '__main__':
    main()
