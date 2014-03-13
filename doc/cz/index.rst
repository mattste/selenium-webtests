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

- možnost parametrizovat příkaz **runwebtests**
- vylepšit práci s proxy
- možnost předat **wait** metodě funkci, která se bude periodicky spouštět a vracet true/false
- nebude pak implicitly_wait zbytečné?
- jak vyřešit různé loginy pro .dev, .test, provoz?
- nebylo by lepší a rychlejší vytvářet instanci browseru per celý test popř. per testcase?
- IE8 a error click mimo view
- vyřešit zamrznuté instance browserů, které se nezavřou

.. toctree::
   :numbered:

   instalace
   psani_testu
   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
