# Directory where the tests we want to run are saved
TESTS_DIR = "tests"

# If relative URL is used in the tests, this will be used as its base URL
BASE_URL = "http://zbozi.cz"

# This machine IP
IP = "localhost"

#------------------------------------------------------------------------------
# SELENIUM
#------------------------------------------------------------------------------

# Absolute path to selenium standalone server file (.jar)
SELENIUM_SERVER_FILE = "/home/jk/Git/py-selenium-skeleton/3rdparty/selenium-server-standalone-2.39.0.jar"

# Port number the selenium server will be running on
SELENIUM_SERVER_PORT = 4444

#------------------------------------------------------------------------------
# PROXY
#------------------------------------------------------------------------------

# Absolute path to the browsermob-proxy start file (.sh or .bat)
PROXY_START_SCRIPT = "/home/jk/Git/py-selenium-skeleton/3rdparty/browsermobproxy/bin/browsermob-proxy"

# This machine port number the browsermob-proxy server will be running on
PROXY_PORT = 8080