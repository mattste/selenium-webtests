Psaní testů
===========

Pokud máme SW modul nainstalovaný a zaregistrované všechny stroje s testovacími prohlížeči, můžeme začít psát samotné testy.

Příklad, jak takový test vypadá, je v examples/example_test staženého balíku SW. Na něm si můžeme vysvětlit základní strukturu testů.

Vysvětlení struktury testu na příkladu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V example_test jsou dva soubory:

1. V **settings.py** je toto:

   ::

    BASE_URL = "http://seznam.cz"

   Doména webu. Pokud v testech při navigaci prohlížeče uvedeme relativní URL (např. "/kategorie/notebooky"), hodnota této proměnné se použije jako prefix. Pokud bychom pak chtěli testy spustit v jiném prostředí (provoz, produktový test...), stačí změnit tuto proměnnou.

   ::

    BROWSERS = [
        {
            "browserName": "firefox",
            "version": "ANY",
            "platform": "ANY"
        }
    ]

   Pole prohlížečů, na kterých chceme testy spouštět. Každý zde uvedený prohlížeč musí být zaregistrovaný do Selenium HUBu. Jako hodnotu klíčů "version" a "platform" můžeme uvést "ANY", pokud nám nezáleží na tom, v jaké verzi prohlížeče nebo na jakém OS se testy spustí.

2. Soubor **homepage.py** představuje jednoduchý test vyhledávání z HP Seznamu. V adresáři může být libovolný počet takových souborů.

   ::

    # -*- coding: utf-8 -*-

   Nastavení kódování souboru

   ::

    from seleniumwebtests.testcase import *

   Naimportování funkcionality společné pro všechny testy.

   ::

    class homepage(TestCase):

   Třída testů. Musí dědit z seleniumwebtests.TestCase.
   Jeden soubor může obsahovat libovolný počet takových tříd. Díky tomu se testy dají členit do logických celků.

   ::

    def test_vyhledavani(self):

   Konkrétní test. Název metody musí začínat prefixem **test***. Třída jich může obsahovat libovolný počet. Průběh testu je většinou následující:

   - navigace prohlížeče na požadovanou URL

   - provedení akce

   - testování výsledku akce

   V prvních dvou krocích se využívají metody :ref:`webdriverapi`, :ref:`webelementapi` nebo :ref:`proxyapi`. Ve třetím kroku :ref:`assertmethods`.

Navigace prohlížeče
~~~~~~~~~~~~~~~~~~~

Pro nasměrování prohlížeče na určitou URL slouží metoda get:

::

    self.driver.get("/kategorie/notebooky")

Pokud je URL zadána takto bez protokolu a domény, použije se proměnná BASE_URL ze souboru settings.py
Adresy je možné zadávat i absolutně:

::

    self.driver.get("http://zbozi.cz/kategorie/notebooky")

Po přechodu na jinou stránku WebDriver čeká na JS událost "onload" než pokračuje dále v kódu testu. Díky tomu se dá spolehnout na to, že je DOM strom načtem a můžeme se stránkou dále pracovat. Jiná situace je při různých JS requestech, při kterých nedochází k reloadu stránky. Tam musíme WebDriveru explicitně říct, aby chvilku počkal. Více o tom v sekci :ref:`waits`.

Vyhledávání elementů
~~~~~~~~~~~~~~~~~~~~

Pro vyhledávání elementů na stránkce slouží řada metod. Dají se rozdělit do dvou kategorií:

Ty, které vrací vždy první nalezený výsledek:

- find_element_by_id
- find_element_by_name
- find_element_by_xpath
- find_element_by_link_text
- find_element_by_partial_link_text
- find_element_by_tag_name
- find_element_by_class_name
- find_element_by_css_selector

a metody, které vrací pole nalezených elementů:

- find_elements_by_name
- find_elements_by_xpath
- find_elements_by_link_text
- find_elements_by_partial_link_text
- find_elements_by_tag_name
- find_elements_by_class_name
- find_elements_by_css_selector

Příklad:

::

    elm = self.driver.find_element_by_css_selector("#page .content")
    elmArray = self.driver.find_elements_by_tag_name("form")

Vyplňování formuláře
~~~~~~~~~~~~~~~~~~~~

Pro jednodušší vyplňová formuláře rozšiřuje SW standardní API o šikovnou metodu **fill_form**. Té se jako první argument předává element formuláře a jako druhý objekt, ve kterém klíče představují hodnoty name atributů jednotlivých formulářových prvků a jejich hodnoty jsou pak hodnoty, které chceme těmto prvům nastavit. SW sám rozpozná, o jaký element se jedná a podle toho ho vyplní.

::

    self.driver.fill_form(form, {"firstname": u"Jára", "lastname": u"Cimrman"})

Pokud chceme po vyplnění formulář rovnou i odeslat, můžeme použít metodu **fill_form_and_submit** se stejnými argumenty.

Pro vyplnění jednoho elementu, který ani nemusí být ve formuláři, slouží metoda **fill_element**.

::

    self.driver.fill_element(elm, "Jára Cimrman")

Práce s proxy
~~~~~~~~~~~~~

Selenium samotné neposkytuje způsob jak testovat síťové požadavky. Proto SW využívá vlastní proxy a v případě potřeby dokáže síťový provoz na stránce ukládat a  výsledek na požádání vrátit jako JSON, který je strukturovám podle HAR specifikace. V tomto JSONu pak můžeme vyhledávat.

Nejprve je potřeba v testu zapnout logování:

::

    self.proxy.new_har("test")

Potom provedeme akci, při by mělo dojít o odeslání požadavku, který nás zajímá a následeně si proxy řekneme o zachycené výsledky:

::

    res = self.proxy.har

Případně můžeme ve výsledcích rovnou vyhledávat. Takto si například můžeme ověřit, že si homepage Seznamu říká o výdej reklamy na pozici "seznam.hp.tip.vikend":

::

    self.proxy.new_har("test")
    self.driver.get("http://seznam.cz")
    self.assertTrue(
        self.proxy.find_in_har(
            "i.imedia.cz",
            {
                "request.queryString":
                {
                    "name": "zoneId",
                    "value": "seznam.hp.tip.vikend"
                }
            }
        )
    )

Metoda **find_in_har** přijimá dva argumenty. První je URL nebo substring, který musí URL obsahovat. Pro každý požadavek, který stringu vyhovuje se pak provádí hledaní podle druhého parametru, ve kterém předáváme kritéria, kterým musí požadavek vyhovat. Kritéria se předávají jako objekt (dict), ve kterém klíče reprezentují položku v HARu. Použitím teček v názvu klíče lze přistupovat k datům zanořeným hlouběji v HARu. Abychom mohli v HARu vyhledávat, musíme znát jeho strukturu. Příklad, jak takový request v HARu vypadá, je v examples/har.json

.. _waits:

Čekání
~~~~~~

Při psaní testů je potřeba myslet na to, že ne vždy je než bude moci v kódu testu pokračovat dál, je potřeba chvilku počkat. Například na načtení nové stránky, doběhnutí requestu apod.

Sám Selenium WebDriver si dokáže poradit s případy, kdy ho pomocí metody **get** přesměrujeme na jinou stránku. S vykonáváním testu počká do doby, než bude stránka celá načtená.

Nedokáže si ale poradit s AJAX requesty a nejrůznějšími akcemi, které na stránce něco mění a zaberou delší čas. Pokud po takové akce chceme vyhledat nějaký element na stránce pomocí některé **find_*** metody, tak nic řešit nemusíme. Modul SW přidává k těmto metodám implicitní čekání, pokud napoprvé nevrátí žádný výsledek. Periodicky se pak po dobu 10s kontroluje, jestli se požadovaný element neobjeví. Pokud ne, teprve pak vyhodí chybu a test selže.

Pro všechny ostatní případy, kdy potřebujeme nějakou dobu počkat, je tu metoda **wait**:

::

  self.driver.wait(5) // čekej 5s

Zadávání znaků z klávesnice
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro odesílání stisku kláves z klávesnice slouží metoda **send_keys**. Pomocí ní se dá např. do inputu vložit text:

::

    self.driver.send_keys(u"kotě v botě")

Znaky se odešlou do elementu, na kterém je focus.

Existuje také metoda **send_keys_to_element**, které cílový element můžeme zadat:

::

    self.driver.send_keys_to_element(elm, u"kotě v botě")

Kromě textu se dají odesílat i speciální klávesy. Jejich seznam je v :ref:`keysapi`.

::

    self.driver.send_keys(Keys.ENTER)

Nastavení požadovaných prohlížečů pro jednotlivé testy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Seznam prohlížečů, na kterých chceme spustit testy, je možné přenastavit pro každou třídu testů (testcase):

::

    class homepage(TestCase):

        BROWSERS = [
            {
                "browserName": "internet explorer",
                "version": "8.0",
                "platform": "ANY"
            }
        ]

        def test_vyhledavani(self):
            ...

To je užitečné například v případě, že chceme napsat testy specifické pro jeden prohlížeč.

Stringy s českými znaky
~~~~~~~~~~~~~~~~~~~~~~~

Při práci s českými znaky v testech je potřeba string, který je obsahuje, označit jako unicode. To se dělá přidáním znaku "**u**" před string.

::

    self.driver.fill_form_and_submit(search_form, {"q": u"kotě v botě"})

.. toctree::
   :numbered:

   index
   instalace
   psani_testu
   api




