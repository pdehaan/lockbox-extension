/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

import openDataStore from "./datastore";
import initializeMessagePorts from "./message-ports";

// XXX: For now, initialize the datastore on startup and then hook up the
// button. Eventually, we'll have UX to create new datastores (and persist
// existing ones).\
openDataStore().then(async(ds) => {
  if (!ds.initialized) {
    await ds.initialize();
  }
  initializeMessagePorts();

  function openLockbox() {
    browser.tabs.create({url: browser.extension.getURL("manage/index.html")});
  }
  browser.browserAction.onClicked.addListener(openLockbox);
});
