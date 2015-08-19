import os
from time import gmtime, strftime

from pykstats.common.base_statsd_plotter import BaseStatsdPlotter


class MylocalmcdsNeo4jGCPlotter(BaseStatsdPlotter):
    def __init__(self):
        # Set default attributes
        super(MylocalmcdsNeo4jGCPlotter, self).__init__()

        # Set custom attributes
        node_env = os.environ.get('NODE_ENV', 'local')
        self.metric = 'mylocalmcds.%s.neo4j.gc.count' % node_env

    def plot(self):
        value = os.system(
            "cat /var/lib/neo4j/data/graph.db/messages.log | grep '%s' | grep 'GC Monitor: Application threads blocked for' | wc -l" %
            strftime("%Y-%m-%d", gmtime()))

        self.statsd.gauge(self.metric, value)

        print("[%s]: Flushed %s for %s to statsd." % (
              strftime("%Y-%m-%d-%H:%M:%S", gmtime()), value, self.metric))

if __name__ == '__main__':
    plotter = MylocalmcdsNeo4jGCPlotter()
    print("[%s]: Starting MylocalmcdsNeo4jGC plotter..." %
          strftime("%Y-%m-%d", gmtime()))
    plotter.run()
