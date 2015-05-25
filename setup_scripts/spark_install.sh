#/bin/bash!

# Install Oracle's version of Java
echo -ne '\n' | add-apt-repository ppa:webupd8team/java
apt-get update
echo debconf shared/accepted-oracle-license-v1-1 select true | \
  debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | \
  debconf-set-selections
apt-get install -y oracle-java6-installer
echo "JAVA_HOME=/usr/lib/jvm/java-6-oracle" >> /etc/environment

# Install Scala
apt-get install -y scala
echo "SCALA_HOME=/usr/share/java" >> /etc/environment
source /etc/environment

# Install Spark
wget http://d3kbcqa49mib13.cloudfront.net/spark-1.3.1-bin-hadoop2.6.tgz
tar -xzvf spark-1.3.1-bin-hadoop2.6.tgz

# Add hostname to /etc/hosts file
echo "127.0.0.1 localhost $(hostname)" >> /etc/hosts
