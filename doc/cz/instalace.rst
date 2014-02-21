Instalace
---------

Příprava prostředí a instalace (Selenium HUB)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Na stroji, na kterém chceme SW rozběhnout, musí být nainstalovaný Python 2.7 (vyšší verze jsem nezkoušel) a Java 7.

2. Ze stránek https://code.google.com/p/selenium/downloads/list stáhneme Selenium Standalone Server (selenium-server-standalone-<verze>.jar).

3. Ze stránek http://bmp.lightbody.net/ stáhneme BrowserMob Proxy (.zip) a rozbalíme.

4. Stáhneme nebo vyclonujeme SW balík::

    git clone https://github.com/jirikuchta/selenium-webtests.git

5. Dále je potřeba otevřít soubor config.py v balíku a upravit v něm cesty ke staženému Selenium Serveru, spuštěcímu souboru proxy a IP stroje.

  .. note::

    Na uvedené IP adrese musí být stroj, na kterém SW instalujeme, dostupný pro všechny vzdálené stroje, na kterých běží testovací prohlížeče. Je možné vyplnit "localhost" pro spouštění testů na lokálních prohlížečích.

6. Pak stačí vlézt do hlavního adresáře staženého balíku a tento nainstalovat.::

    sudo python setup.py install

  .. note::

    Pokud by si instalátor stěžoval, že mu chybí setuptools, bude potřeba `balík setuptool nainstalovat <https://pypi.python.org/pypi/setuptools#windows>`_.

Po úspěsné instalaci by měl být SW připraven. Zbývá zaregistrovat stroje s testovacími prohlížeči.

Registrace testovacích prohlížečů (Selenium Nodes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Následující postup je potřeba provést na všech strojích, na kterých běží prohlížeče pro testování. Na strojích musí být nainstalovaná Java 7.

1. Zalogujeme se na stroj.

2. Ze stránek https://code.google.com/p/selenium/downloads/list stáhneme Selenium Standalone Server (selenium-server-standalone-<verze>.jar).

3. Na stroj nakopírujeme soubor nodeconfig.json uložený v adresáři examples/ v balíku SW a zeditujeme ho.

- **capabilities** Pole objektů obsahujících informace o dostupných prohlížečích na tomto stroji

  - **browserName** Název prohlížeče. Standardní názvy jsou internet explorer, firefox, chrome, opera, safari. Selenium na jejich základě hledá spustitelný soubor.

  - **version** Verze prohlížeče.

  - **platform** Název platformy. Standardizované názvy jsou WINDOWS, LINUX, MAC

  - **maxInstances** Maximální počet současně spuštěných instancí prohlížeče. Větší počet je lepší v případě, že testy zároveň spustí více uživatelů. Nemusí pak čekat, než doběhnou testy jiných uživatelů. U IE musí být nastaveno na 1. Je to kvůli proxy. Internet Explorer nastavuje proxy pro celý systém. Pokud by své testy spustilo více lidí na IE, navzájem by si přepisovali nastavení proxy a nemohli by pak spolehlivě testovat síťové požadavky.

- **configuration** Konfigurace stroje

  - **maxSession** Maximální počet souběžně běžících testů.

  - **port** Port, na kterém bude poslouchat Selenium Server.

  - **host** IP tohoto stroje. Stroj na této adrese musí být viditelný pro stroj, na kterém jsme nainstalovali SW.

  - **register** Boolean hodnota rozhodující o tom, jestli se má stroj automaticky pokoušet připojit na Selenium HUB, pokud se mu to napoprvé nepodaří.

  - **registerCycle** Interval pokusů o připojení v Selenium HUBu v ms.

  - **hubPort** Port, na kterém poslouchá Selenium HUB (hodnota klíče SELENIUM_SERVER_PORT z config.py)

  - **hubHost** IP adresa Selenium HUBu (hodnota klíče IP z config.py)

  - **timeout** Maximální doba v ms, po kterou prohlížeč čeká na další příkazy. Pokud do této doby žádný neobdží, tak se uzavře. Je to pojistka pro případ, kdy test z nějakého důvodu nedoběhne do konce a neuzavře za sebou prohlížeč. Tím by se rychle vyčerpal počet dostupných instancí prohlížeče. Pokud je timeout nastavený, musíme s ním počítat i v testech, ve kterých nastavujeme :ref:`waits`. Není možné nastavit delší čekání než je timeout prohlížeče.

   Pro spouštění testů v Chrome je potřeba stáhnout chromedriver z http://chromedriver.storage.googleapis.com/index.html a nakopírovat ho do C:\Windows\System32,       resp. do /bin.

   Podobné je to v případě IE. Driver je dostupný http://code.google.com/p/selenium/downloads/list jako IEDriverServer_<verze>.zip. Driver stáhneme a  nakopírujeme      do stejné složky jako v případě Chrome.

   Opera je podporována pouze do verze 12.x. Na novějších verzích založených na WebKitu není možné testy spouštět.

4. Spustíme node příkazem

   ::

        java -jar cesta-ke-stazenemu-selenium-stanalene-serveru.jar -role node -nodeConfig cesta-k-nodeconfig.json

   Otevře se konzole v ní by se měla peridicky zobrazovat následující chybová hláška:

   ::

        INFO - couldn't register this node : Hub is down or not responding : Connection refused

   To je způsobené tím, že se node snaží připojit k HUBu, který ale zatím neběží. Spustí se až při prvním spuštění testů.

5. Vrátíme se zpět na stroj, na který jsme instalovali SW (Selenium HUB). Vlezeme do adresáře examples/example_test ve staženém balíku a spustíme testy příkazem

   ::

        runwebtests

   V konzoli by se mělo objevit zhruba toto:

   ::

        Proxy server seems not running. Trying to start on 192.168.56.1:3128...
        Selenium HUB seems not running. Trying to start on 192.168.56.1:4444...

        test_vyhledavani (homepage.homepage) on firefox,ANY,ANY ... ok

        ----------------------------------------------------------------------
        Ran 1 test in 13.280s

        OK

   Pokud ano, je vše potřebné nainstalováno a správně nakonfigurováno a můžeme začít psát testy.

.. note::

  Na adrese Selenium HUBu (v našem případě 192.168.56.1:4444) je k dispozici konzole ukazující, které prohlížeče jsou k HUBu zaregistrovány a můžeme je tak použít k testování. Stačí vlézt na adresu http://192.168.56.1:444/grid/console

.. toctree::
   :numbered:

   index
   instalace
   psani_testu
   api
