import time
import requests
import sys

# Update interval in minutes
interval = 30

# DNS
ddns = 'paste here your ddns update url'


def main():
    log('DDNSUpdater is starting..')
    log('Interval set to ' + str(interval) + ' minutes.')

    while True:
        log('Trying to update DDNS..')

        # Update DNS
        try:
            result = requests.get(ddns)

            # Print out result
            log('Status: ' + str(result.status_code))
        except requests.exceptions.ConnectionError:
            log('Status: Connection refused')

        # Sleep for the given interval
        time.sleep(interval * 60)


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
