Actor
-id
-login = user name
-url = link of the actor’s profile

Event
-id
-type = type of event
-actor_id (foriegn key)
-created_at = time event created

Repo
-id
-name 
-event_id (foriegn key)

Payload
-event_id
-size = size of payload