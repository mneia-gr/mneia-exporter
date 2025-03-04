# Mneia Exporter #

A Django app that exports data to flat files:

1.  Data from the [mneia-backend](https://github.com/mneia-gr/mneia-backend) database exported to JSON files in
    [mneia-data](https://github.com/mneia-gr/mneia-data).
2.  Data from the MusicBrainz database exported to the Sphinx documentation in
    [django-musicbrainz-connector](https://github.com/mneia-gr/django-musicbrainz-connector).
3.  Data from the [mneia-backend](https://github.com/mneia-gr/mneia-backend) database, plus text content from
    [mneia-data](https://github.com/mneia-gr/mneia-data), exported to Markdown files with YAML front matter, for
    processing by Jekyll in [mneia-gr.github.io](https://github.com/mneia-gr/mneia-gr.github.io).
