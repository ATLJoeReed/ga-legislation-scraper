#### Step #1 - Get a list of sessions and extract the current sessionID. This ID is needed for several of the call below. You can get this sessionID from several places.

  - url: https://www.legis.ga.gov/committees/house
  - url: https://www.legis.ga.gov/committees/senate
  - url: https://www.legis.ga.gov/members/house
  - url: https://www.legis.ga.gov/members/senate

  - api call: /api/sessions
---
#### Step #2 - Get a list of committees. 

Note: You can call either url (house or senate) as the json response object contains all committees for both.
  - url: https://www.legis.ga.gov/committees/house
  - url: https://www.legis.ga.gov/committees/senate

  - api call: /api/committees/List/1029
---
#### Step #3a - Get a list of Representatives.
  - url: https://www.legis.ga.gov/members/house

  - api call: /api/members/list/1029?chamber=1
---
#### Step #3b - Get a list of Senators.
- url: https://www.legis.ga.gov/members/senate

- api call: /api/members/list/1029?chamber=2
---
#### Step #4 - Get a list of all Legislation.
\
**ToDo: Figure out a way to pull these faster...**

- url: https://www.legis.ga.gov/legislation/all

- api call: /api/Legislation/Search/20/0

This is the starting point. From here you will need to start building out the url(s) based on the number of bills found - resultCount.

*Data extracted: legislationId, caption, number, documentType, chamberType, status & statusDate*

Next call:
- url: https://www.legis.ga.gov/search?s=1029&p=2&rc=2100

- api call: /api/Legislation/Search/20/1
---
#### Step #5 - Get legislative details. You need the legislationId for each legislation.

  - url: https://www.legis.ga.gov/legislation/58786

  - api call: /api/legislation/detail/58916
  - api call: /api/legislation/html/20212022/195760

**ToDo: Build process to convert legistative HTML to txt...**
