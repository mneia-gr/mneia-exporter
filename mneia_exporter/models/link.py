from mneia_backend.models.link import Link as _Link

from mneia_exporter.mixins import Exportable


class Link(_Link, Exportable):
    class Meta:
        proxy = True
