from distutils.core import setup

setup(
    name = 'py-selenium-skeleton',
    packages = ['py-selenium-skeleton'],
    version = '0.1',
    description = '',
    author = 'Jiri Kuchta',
    author_email = 'jiri.kuchta@live.com',
    url = 'https://github.com/jirikuchta/py-selenium-skeleton',
    keywords = ['testing', 'logging', 'example'],
    classifiers = [],
    install_requires=[
        'selenium>=2.38.4',
        'browsermob-proxy>=0.6.0',
    ],
    scripts=['scripts/huml'],
)
