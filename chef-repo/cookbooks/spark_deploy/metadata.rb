name             'spark_deploy'
maintainer       'YOUR_COMPANY_NAME'
maintainer_email 'YOUR_EMAIL'
license          'All rights reserved'
description      'Installs/Configures spark_deploy'
long_description IO.read(File.join(File.dirname(__FILE__), 'README.md'))
version          '0.1.0'

depends "apache_spark"
depends "tar"
depends "monit_wrapper"
depends "logrotate"
depends "java"
