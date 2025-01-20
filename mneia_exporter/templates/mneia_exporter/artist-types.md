Artist Types
============

Last checked on {{today}}, there are {{num_instances}} artist types in the MusicBrainz database:

| id              | name              |  description             |
|-----------------|-------------------|--------------------------|{% for instance in instances %}
| {{instance.id}} | {{instance.name}} | {{instance.description}} |{% endfor %}
