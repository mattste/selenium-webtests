*****************
Selenium Webtests
*****************

Selenium Webtests (dále jen SW) je nadstavba nad Selenium Python API. Jejím cílem je zjednodušit psaní a spouštění seleniových testů. Využívá Remote WebDriver pro spouštění testů na vzdálených strojích. Díky tomu je možné weby testovat v různých verzích prohlížečů na různých operačních systémech. Díky proxování požadavků je možné psát testy ověřující odeslání a výsledek síťového požadavku.

Tato dokumentace vychází z dokumentace k Selenium Python API dostupné na adrese http://selenium-python.readthedocs.org/ Rozšiřuje ji o popis funcionalit specifických pro SW a o popis metod, o které bylo API obohaceno.

Použité technologie
~~~~~~~~~~~~~~~~~~~
- **Selenium Remote WebDriver** - pro ovládání prohlížeče. Jeho metody jsou popsány v :ref:`webdriverapi`
- **unittest** - python modul pro organizaci a spouštění testů (http://docs.python.org/2/library/unittest.html)
- **BrowserMob proxy** - proxy pro odchytávání síťových požadavků (http://bmp.lightbody.net/)
- **browsermob-proxy-py** - python wrapper nad BrowserMob proxy API (https://github.com/AutomatedTester/browsermob-proxy-py)

TODO
~~~~

- nebylo by lepší a rychlejší vytvářet instanci browseru per celý test popř. per testcase? (užitečné hlavně při nutnosti přihlašování před testem)
- info o browseru do XML reportů
- každé spuštění testu otevírá nový port. Nešlo by nějak využít porty otevřené při předchozích testech?
- automatické propisování verze ze setup.py do dokumentace a do **__version__**
- ukončit instanci browseru při abortu úlohy v Jenkinsu


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
