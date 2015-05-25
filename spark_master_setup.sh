#/bin/bash!

# Install Oracle's version of Java
sudo echo -ne '\n' | add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install -y oracle-java6-installer
sudo echo "JAVA_HOME=/usr/lib/jvm/java-6-oracle" >> /etc/environment

# Install Scala
sudo apt-get install -y scala
sudo echo "SCALA_HOME=/usr/share/java" >> /etc/environment
sudo source /etc/environment

ssh-keygen -t rsa -P ""
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Install Spark
wget http://d3kbcqa49mib13.cloudfront.net/spark-1.3.1-bin-hadoop2.6.tgz
tar -xzvf spark-1.3.1-bin-hadoop2.6.tgz

# Add hostname to /etc/hosts file
echo "127.0.0.1 localhost $(hostname)" >> /etc/hosts
