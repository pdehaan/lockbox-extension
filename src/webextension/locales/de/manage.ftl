document
  .title = LOCKBOXEN Entries

toolbar-item-count =
  { $count ->
     [one]   1 Entryen
    *[other] { $count } Entriens
  }

toolbar-add-item = NEW Entryen
toolbar-go-home = HOMEN
toolbar-send-feedback = FEEDBACKEN

item-filter
  .placeholder = SEARCHEN for an entry

item-summary-new-item = NEWEN Entry
item-summary-no-title = (NOEN Entry Name)
item-summary-no-username3 = (NOEN Username)

homepage-no-passwords =
  WELCOMEN to Lockbox! I'm Lockie, and I'm here to help you lock
  up your passwords!
  
  TO get started, click { toolbar-add-item } above.

homepage-under-10-passwords =
  { $count ->
     [1]     DANKE there! It's your friend, Lockie!
           
             YOU'VE added { $count } entry. That's a great start!
    *[other] WELVEKOMEN there! It's your friend, Lockie!
           
             YOU'VEN added { $count } entries. That's a great start!
  }

homepage-under-50-passwords =
  HEYEN again! Just your pal Lockie checking in!
  
  YOU'VE added { $count } entries. Great job, keep it up!

homepage-over-50-passwords =
  WELCOMEN back! I hope you're having a great day!
  
  You've added { $count } entries. Wow, I'm really impressed!

item-details-heading-view = ENTRYEN Details
item-details-heading-new = CREATEN a New Entry
item-details-heading-edit = EDITEN Entry

item-details-title = ENTRYEN Name
item-details-origin = WEBSITEN Address
item-details-username = USERNAMEN
item-details-copy-username = COPYEN
  .title = COPYEN the username to the clipboard
item-details-password = PASSWORDEN
item-details-copy-password = COPYEN
  .title = COPYEN the password to the clipboard
item-details-notes = NOTESEN

item-details-edit = EDITEN Entry
item-details-delete = DELETEN Entry

item-details-save-new3 = SAVEN Entry
item-details-save-existing = SAVEN Changes
item-details-cancel = CANCELEN

[[dialogs]]

modal-cancel-editing = THISEN entry has unsaved changes. Are you sure you want to discard them?
  .confirmLabel = DISCARDEN Changes
  .cancelLabel = GOEN Back

modal-delete = AREN you sure you want to delete this entry?
  .confirmLabel = DELETEN Entry
  .cancelLabel = CANCELEN
