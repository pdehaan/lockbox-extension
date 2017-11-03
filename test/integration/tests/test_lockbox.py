# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""Tests for lockbox extension."""


def test_login(login_page):
    """Log into Lockbox."""
    home_page = login_page.login('password')
    assert 'Welcome to Lockbox!' in home_page.lockie


def test_add_entry(home_page):
    """Add a new entry."""
    home_page.add_entry()
    assert len(home_page.entries) == 1
    assert home_page.entries[0].name == '(No Entry Name)'


def test_delete_entry(home_page):
    """Test Deleting an entry."""
    home_page.add_entry()
    home_page.delete_entry()
    assert len(home_page.entries) == 0
