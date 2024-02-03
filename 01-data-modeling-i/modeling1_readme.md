# Data Modeling 1

## tables

### Actors
|Attribute|Data Type|Note|
|:------------|:---------------:|:---------------:|
|id|int||
|login|text|username|
|url|text|link of the actor’s profile|

### Events
|Attribute|Data Type|Note|
|:------------|:---------------:|:---------------:|
|id|text||
|type|text|type of event|
|actor_id|int|(foreign key)|
|created_at|text|time event created|

### Repos
|Attribute|Data Type|Note|
|:------------|:---------------:|:---------------:|
|id|int||
|name|text||
|event_id|text|(foreign key)|

### Payloads
|Attribute|Data Type|Note|
|:------------|:---------------:|:---------------:|
|event_id|text|(foreign key)|
|size|int|size of payload|