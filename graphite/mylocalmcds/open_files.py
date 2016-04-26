import os
import socket
from time import gmtime, strftime

from pykstats.common.base_statsd_plotter import BaseStatsdPlotter


class MylocalmcdsOpenFilesPlotter(BaseStatsdPlotter):
    def __init__(self):
        # Set default attributes
        super(MylocalmcdsOpenFilesPlotter, self).__init__()

        # Set custom attributes
        fqdn = socket.getfqdn().replace('.','_')
        self.metric = '%s.files.open' % fqdn

    def plot(self):
        config =  self.config['MylocalmcdsOpenFilesPlotter']
        # Get neo4j process id
        with open(self.config['neo4j']['pid_file_path'], 'r') as neo4j_pid_file:
            neo4j_pid = neo4j_pid_file.read()
        # Compute metric value
        command = os.popen("lsof -p $(%s)" % neo4j_pid)
        value = int(command.read())

        # Send data to statsd daemon.
        self.statsd.gauge(self.metric, value)
        print("[%s]: Plotted %s for %s to statsd." % (
              strftime("%Y-%m-%d-%H:%M:%S", gmtime()), value, self.metric))

if __name__ == '__main__':
    plotter = MylocalmcdsOpenFilesPlotter()
    print("[%s]: Starting MylocalmcdsOpenFilesPlotter plotter..." %
          strftime("%Y-%m-%d", gmtime()))
    plotter.run()
