from pyspark import SparkContext

logFile = "muenchen.osm" # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'node' in s).count()
numBs = logData.filter(lambda s: 'railway' in s).count()

print "Number of nodes in Munich: %i, lines with Recorded railways: %i" % (numAs, numBs)
