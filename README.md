Datadog Wordpress Vulnerabilities
=================================

Adds a check to Datadog which checks the local installed Wordpress installation for vulnerabilities.

The wpvulndb.com API is used to check the installed Wordpress version for vulnerabilities.

Requirements
------------

Both Datadog Agent and WP CLI should be installed 

Role Variables
--------------

Below is a list of default values along with a description of what they do.

```
# path to Wordpress installation
dwv_wordpress_path: /srv/www/example.com/current

# path where Datadog Agent stores its checks, this is the default directory
dwv_datadog_checks_path: /etc/dd-agent/checks.d

# path where Datadog Agent stores its configurations, this is the default directory
dwv_datadog_conf_path: /etc/dd-agent/conf.d

# interval for this check to run, it will run as often as the specified interval (in seconds)
dwv_datadog_check_interval: 1800
```

Example Playbook
----------------

```
datadog-wordpress-vulnerabilities:
    - dwv_wordpress_path: /srv/www/example.com/current
    - dwv_datadog_check_interval: 900
```

License
-------

BSD

Author Information
------------------

See https://www.erikdevries.com or https://github.com/edv for more information
