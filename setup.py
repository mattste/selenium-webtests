import platform
from distutils.core import setup
from distutils.command.build_py import build_py as _build_py

script = "scripts/runwebtests"
if platform.system() == "Windows":
    script = "scripts/runwebtests.cmd"

setup(
    name = 'selenium-webtests',
    packages = ['selenium-webtests'],
    version = '0.1',
    description = '',
    author = 'Jiri Kuchta',
    author_email = 'jiri.kuchta@live.com',
    url = 'https://github.com/jirikuchta/selenium-webtests',
    keywords = ['testing', 'selenium'],
    install_requires=[
        'selenium>=2.38.4',
        'browsermob-proxy>=0.6.0',
    ],
    scripts=[script],
)
