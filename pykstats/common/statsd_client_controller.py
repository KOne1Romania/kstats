import time

import statsd


class StatsdClientController(object):
    def __init__(self):
        # Create connection to StatsD Server
        self.statsd = statsd.StatsClient()
        # Default time interval for flushing data in seconds
        self.timeout = 10

    def compute(self):
        pass

    def run(self):
        while True:
            self.compute()
            print("[%s]: Flushed data to statsd." %
                  time.strftime("%Y-%m-%d-%H:%M:%S", time.gmtime()))

            time.sleep(self.timeout)

        else:
            print("[%s]: Controller is exiting..." %
                  time.strftime("%Y-%m-%d", time.gmtime()))
