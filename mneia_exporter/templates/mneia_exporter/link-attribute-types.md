Link Attribute Types
====================

Last checked on {{today}}, there are {{num_instances}} link attribute types in the MusicBrainz database. Here is a
sample of 20 of them:

| id              | parent              | root              | name              |  description             |
|-----------------|---------------------|-------------------|-------------------|--------------------------|{% for instance in instances %}
| {{instance.id}} | {{instance.parent}} | {{instance.root}} | {{instance.name}} | {{instance.description|linebreaks}} |{% endfor %}
