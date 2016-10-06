Datadog Wordpress Vulnerabilities
=================================

Adds a check to Datadog which checks the local installed Wordpress installation for vulnerabilities.

The wpvulndb.com API is used to check the installed Wordpress version for vulnerabilities.

The metric returned to Datadog contains a numeric value of the amount of known vulnerabilities. This means only value `0` is a positive outcome.

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

Remove Playbook
---------------

To remove this playbook remove the following files from the server and restart datadog-agent:

- `/etc/dd-agent/checks.d/wordpress_vulnerabilities.py`
- `/etc/dd-agent/checks.d/wordpress_vulnerabilities.pyc`
- `/etc/dd-agent/conf.d/wordpress_vulnerabilities.conf`

Troubleshooting
---------------

When something is not working you can perform the following checks:

- Update Datadog Agent to the latest release
- Make sure the path to the installed Wordpress installation is correct
- Manually execute `wp core version` in the above directory, this should return the version of the installed Wordpress installation
- Check the response of the wpvulndb.com API by executing `curl https://wpvulndb.com/api/v2/wordpresses/461` (replace 461 with the current installed version, without dots, so 4.6.1 becomes 461)
- Run `sudo /etc/init.d/datadog-agent info` to see if the check is running and if it shows any errors
- Use the Datadog Metrics Explorer to check if the metric is available and what it's value is

License
-------

BSD

Author Information
------------------

See https://www.erikdevries.com or https://github.com/edv for more information
