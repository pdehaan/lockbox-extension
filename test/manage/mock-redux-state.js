/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

// Keep these in sync with <src/webextension/manage/reducers.js>.

export const initialState = {
  cache: {
    items: [],
    currentItem: null,
    pendingAdd: null,
  },
  ui: {
    newItem: false,
  },
};

export const filledState = {
  cache: {
    items: [
      {id: "0", title: "title 0"},
      {id: "1", title: "title 1"},
      {id: "2", title: "title 2"},
    ],
    currentItem: {
      id: "1",
      title: "title 1",
      entry: {
        kind: "login",
        username: "username 1",
        password: "password 1",
      },
    },
    pendingAdd: null,
  },
  ui: {
    newItem: false,
  },
};
