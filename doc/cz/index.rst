*****************
Selenium Webtests
*****************

Selenium Webtests (dále jen SW) je nadstavba nad Selenium Python API. Jejím cílem je zjednodušit psaní a spouštění seleniových testů. Využívá Remote WebDriver pro spouštění testů na vzdálených strojích. Díky tomu je možné weby testovat v různých verzích prohlížečů na různých operačních systémech. Díky proxování požadavků je možné psát testy ověřující odeslání a výsledek síťového požadavku.

Použité technologie
~~~~~~~~~~~~~~~~~~~
- **selenium**: python selenium wrapper (http://selenium-python.readthedocs.org/ )
- **Selenium Remote WebDriver** - pro ovládání prohlížeče. Jeho metody jsou popsány v :ref:`webdriverapi`
- **unittest** - python modul pro organizaci a spouštění testů (http://docs.python.org/2/library/unittest.html)
- **BrowserMob proxy** - proxy pro odchytávání síťových požadavků (http://bmp.lightbody.net/)
- **browsermob-proxy-py** - python wrapper nad BrowserMob proxy API (https://github.com/AutomatedTester/browsermob-proxy-py)
- **xmlrunner** - python modul pro generování XML reportu

TODO
~~~~

- nebylo by lepší a rychlejší vytvářet instanci browseru per celý test popř. per testcase? (užitečné hlavně při nutnosti přihlašování před testem)
- info o browseru do XML reportů
- každé spuštění testu otevírá nový port. Nešlo by nějak využít porty otevřené při předchozích testech?
- ukončit instanci browseru při abortu úlohy v Jenkinsu
- spouštět testy paralelně v různých browserech
- BUG: při js chybě se ignoruje volba "retryonerror" 


.. toctree::
   :numbered:

   instalace
   psani_testu
   api
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
