import configparser
import datetime
import logging
import os
import platform
import sys

logging.basicConfig(stream=sys.stderr,
                    level=logging.INFO,
                    format='birthdays: %(message)s')


def load_config(path=''):
    config = configparser.ConfigParser()
    config.read(path)
    logging.info('loaded %d section(s) from config %s', len(config.sections()),
                 path)
    return config


def main():
    logging.info('starting script with python %s (%s)',
                 platform.python_version(), sys.executable)

    try:
        config = load_config(path=os.environ['CONFIG_FILE_PATH'])
    except KeyError:
        logging.fatal('CONFIG_FILE_PATH="..." not set!')
        sys.exit(1)

    today = datetime.date.today()
    logging.info('the current date is %s', today)

    for name, info in config.items():
        if name == 'DEFAULT':
            continue

        is_today = int(info['day']) == today.day and int(
            info['month']) == today.month

        if is_today:
            logging.info('building birthday message for %s', name)
        else:
            logging.info('skipping %s, not birthday yet', name)


if __name__ == '__main__':
    main()
