# Directory where all the tests are saved
SUITES_DIR = "suites"

#------------------------------------------------------------------------------
# SELENIUM
#------------------------------------------------------------------------------

# Path to selenium standalone server file (.jar)
SELENIUM_SERVER_FILE = "bin/selenium-server-standalone-2.39.0.jar"

# Port number the selenium server will be running on
SELENIUM_SERVER_PORT = 4444

#------------------------------------------------------------------------------
# PROXY
#------------------------------------------------------------------------------

# This machine IP/URL address
PROXY_ADDRESS = "192.168.56.1"

# Path to the browsermob-proxy start file (.sh or .bat)
PROXY_START_SCRIPT = "/home/jk/Desktop/selenium/browsermobproxy/bin/browsermob-proxy"

# This machine port number the browsermob-proxy server will be running on
PROXY_PORT = 3128

#------------------------------------------------------------------------------
# BROWSERS
#------------------------------------------------------------------------------

# default list of browsers on which the tests should be run
BROWSERS = [
	{
		"browserName": "firefox",
		"version": "ANY",
		"platform": "ANY"
	},
	{
		"browserName": "internet explorer",
		"version": "8.0",
		"platform": "ANY"
	}
]
