import os
from time import gmtime, strftime

from statsd import StatsClient


if __name__ == '__main__':
    statsd = StatsClient()

    node_env = os.environ.get('NODE_ENV', 'local')
    value = os.system("cat /var/lib/neo4j/data/graph.db/messages.log | grep '%s' | grep 'GC Monitor: Application threads blocked for' | wc -l",
                      strftime("%Y-%m-%d", gmtime()))
    metric = 'mylocalmcds.%s.neo4j.gc.count' % node_env

    statsd.incr(metric, value)
