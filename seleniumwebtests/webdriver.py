# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from seleniumwebtests import swt
from forms import Form, FormElement

class WebDriver(webdriver.Remote):
    """
    Extends selenium Remote webdriver
    """

    def get(self, url):
        """
        Method for navigation browser to the desired URL
        If the URL passed as argument does not begins with "http"
        it is considered as relative and will be prefixed with
        testcase.BASE_URL string

        :param url: Destination URL
        """
        if not url.startswith("http"):
            url = swt.config.BASE_URL + url
        super(WebDriver, self).get(url)

    def wait(self, timeout):
        """
        :param timeout: Number of seconds to wait
        """
        time.sleep(timeout)

    def fill_form(self, elm, data={}):
        """
        Fill form with given data

        :param elm: Form element
        :param data: Dictionary of data for the form. \
                Keys in the dictionary represent name \
                attributes of the form elements
        """
        form = Form(elm)
        form.fill_out(data)

    def fill_form_and_submit(self, elm, data={}):
        """
        Fill form with given data, then submit

        :param elm: Form element
        :param data: Dictionary of data for the form. \
                Keys in the dictionary represent name \
                attributes of the form elements
        """
        form = Form(elm)
        form.fill_out_and_submit(data)

    def fill_element(self, elm, value):
        """
        Fill element with given value

        :param elm: element
        :param value: value
        """
        formElm = FormElement(elm.parent, None)
        formElm.set_elm(elm)
        formElm.fill_out(value)
