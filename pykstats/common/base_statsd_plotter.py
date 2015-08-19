import time

import statsd


class BaseStatsdPlotter(object):
    """ An interface used to send messages to statsd. Each message is
    computed by a plotter and sent via statsd client to statsd daemon.

    Each plotter has to extend this interface, in order to send custom
    metric to statsd daemon.
    """

    def __init__(self):
        # Create connection to StatsD Server
        self.statsd = statsd.StatsClient()
        # Default time interval for flushing data in seconds
        self.timeout = 10

    def plot(self):
        """ The method has to be implemented by the plotter. """
        pass

    def run(self):
        """ While the plooter """
        while True:
            self.plot()
            time.sleep(self.timeout)

        else:
            print("[%s]: Controller is exiting..." %
                  time.strftime("%Y-%m-%d", time.gmtime()))
