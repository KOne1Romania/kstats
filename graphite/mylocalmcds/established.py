import os
import socket
from time import gmtime, strftime

from pykstats.common.base_statsd_plotter import BaseStatsdPlotter

class MylocalmcdsSocketsEstablishedCountPlotter(BaseStatsdPlotter):
    def __init__(self):
        # Set default attributes
        super(MylocalmcdsSocketsEstablishedCountPlotter, self).__init__()

        # Set custom attributes
        fqdn = socket.getfqdn().replace('.','_')
        self.metric = '%s.socket.established.gc' % fqdn

    def plot(self):
        # Compute metric value
        command = os.popen(
            "netstat -tan | awk '{print $6}' | sort | uniq -c  | grep ESTABLISHED | awk '{print $1}'")
        value = int(command.read())

        # Send data to statsd daemon.
        self.statsd.gauge(self.metric, value)
        print("[%s]: Plotted %s for %s to statsd." % (
              strftime("%Y-%m-%d-%H:%M:%S", gmtime()), value, self.metric))


if __name__ == '__main__':
    established_plotter = MylocalmcdsSocketsEstablishedCountPlotter()

    print("[%s]: Starting MylocalmcdsSocketsEstablishedCountPlotter..." %
          strftime("%Y-%m-%d", gmtime()))
    established_plotter.run()
