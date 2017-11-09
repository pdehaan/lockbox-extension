"""Representation of the Home page for lockbox."""

from pypom import Page, Region
from selenium.webdriver.common.by import By

import hashlib
import os
from functools import reduce

table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'

def munged_class_name(path, name):
    h = hashlib.md5((path + '+' + name).encode('utf-8')).digest()
    i = reduce(lambda x, y: x * 256 + y, reversed(h), 0)
    s = ''
    while i > 0:
        s = table[i % 64] + s
        i //= 64
 
    return (
        os.path.splitext(os.path.basename(path))[0] + '__' +
        name + '___' +
        s[:5]
    )

class Home(Page):
    """Contain the locators and actions relating to the home page."""

    _entries_locator = (By.CSS_SELECTOR,
                        'ul li div.{}'.format(munged_class_name('webextension/manage/components/item-summary.css', 'item-summary')))
    _lockie_locator = (By.CSS_SELECTOR,
                       munged_class_name('webextension/manage/components/homepage.css', 'homepage'))
    _delete_entry_locator = (By.CSS_SELECTOR,
                             'article div menu '
                             'button.{}'.format(munged_class_name('webextension/widgets/button.css', 'minimal')))
    _delete_entry_modal_locator = (By.CSS_SELECTOR,
                                   '.ReactModal__Content--after-open '
                                   'menu button.{}'.format(munged_class_name('webextension/widgets/button.css', 'button')))
    _new_entry_locator = (By.CSS_SELECTOR,
                          'section menu '
                          'button.{}:nth-child(3)'.format(munged_class_name('webextension/widgets/button.css', 'button')))
    _save_entry_locator = (By.CSS_SELECTOR, 'article div form menu '
                           'button.{}'.format(munged_class_name('webextension/widgets/button.css', 'button')))

    @property
    def lockie(self):
        """Lockie image locator."""
        return self.find_element(*self._lockie_locator).text

    def add_entry(self):
        """Add an entry into the lockbox."""
        current_entries = len(self.entries)
        self.find_element(*self._new_entry_locator).click()
        self.find_element(*self._save_entry_locator).click()
        self.wait.until(lambda _: len(self.entries) != current_entries)

    def delete_entry(self):
        """Delete an entry from lockbox."""
        self.find_element(*self._delete_entry_locator).click()
        self.find_element(*self._delete_entry_modal_locator).click()
        self.wait.until(lambda _: len(self.entries) == 0)

    @property
    def entries(self):
        """List of current entries."""
        els = self.find_elements(*self._entries_locator)
        return [Entry(self, el) for el in els]


class Entry(Region):
    """Entry specific locators and functions."""

    _name_locator = (By.CSS_SELECTOR, 'div.{}'.format(munged_class_name('webextension/manage/components/item-summary.css', 'title')))

    @property
    def name(self):
        """Return the name of the entry."""
        return self.find_element(*self._name_locator).text

    def click(self):
        """Click on the entry."""
        self.root.click()
        return self.EntryDetail(self)

    class EntryDetail(Region):
        """Entry detail locators and functions."""

        _delete_entry_locator = (By.CSS_SELECTOR,
                                 'article div menu '
                                 'button.{}'.format(munged_class_name('webextension/widgets/button.css', 'minimal')))
        _delete_entry_modal_locator = (By.CSS_SELECTOR,
                                       '.ReactModal__Content--after-open '
                                       'menu button.{}'.format(munged_class_name('webextension/widgets/button.css', 'button')))

        def delete(self):
            """Delete an entry from the lockbox."""
            self.find_element(*self._delete_entry_locator).click()
            self.find_element(*self._delete_entry_modal_locator).click()
