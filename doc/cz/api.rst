API
===

Popis metod a vlastností objektů používaných při psaní testů.

.. automethod:: testcase.TestCase.log
.. automethod:: testcase.TestCase.take_screenshot

.. _webdriverapi:

WebDriver (driver)
~~~~~~~~~~~~~~~~~~

Instance Selenium Remote Webdriveru. Poskytuje metody pro ovládání prohlížeče a vyhledávání v DOMu. Metody se volají přes **self.driver.nazev_metody**.

.. automodule:: webdriver
   :members:
   :inherited-members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:

.. _webelementapi:

WebElement (webelement)
~~~~~~~~~~~~~~~~~~~~~~~

Metody pro práci s DOM elementem. Metody se volají přes **element.nazev_metody**.

.. automodule:: selenium.webdriver.remote.webelement
   :members:
   :inherited-members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:

.. _proxyapi:

Proxy (proxy)
~~~~~~~~~~~~~

Metody pro práci s proxy. Volají se přes **self.proxy.nazev_metody**.

.. automodule:: proxy
   :members:
   :inherited-members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:

.. _keysapi:

Akce (ActionChains)
~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.common.action_chains
   :members:
   :inherited-members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:

Keys (Keys)
~~~~~~~~~~~

.. automodule:: selenium.webdriver.common.keys
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:

Alerts (Alert)
~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.common.alert
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:

.. _assertmethods:

Metody pro testování výsledku testu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------+----------------------------+
| Název metody                 | Význam                     |
+==============================+============================+
| assertEqual(a, b)            | a == b                     |
+------------------------------+----------------------------+
| assertNotEqual(a, b)         | a != b                     |
+------------------------------+----------------------------+
| assertTrue(x)                | bool(x) is True            |
+------------------------------+----------------------------+
| assertFalse(x)               | bool(x) is False           |
+------------------------------+----------------------------+
| assertIs(a, b)               | a is b                     |
+------------------------------+----------------------------+
| assertIsNot(a, b)            | a is not b                 |
+------------------------------+----------------------------+
| assertIsNone(x)              | x is None                  |
+------------------------------+----------------------------+
| assertIsNotNone(x)           | x is not None              |
+------------------------------+----------------------------+
| assertIn(a, b)               | a in b                     |
+------------------------------+----------------------------+
| assertNotIn(a, b)            | a not in b                 |
+------------------------------+----------------------------+
| assertIsInstance(a, b)       | isinstance(a, b)           |
+------------------------------+----------------------------+
| assertNotIsInstance(a, b)    | not isinstance(a, b)       |
+------------------------------+----------------------------+
