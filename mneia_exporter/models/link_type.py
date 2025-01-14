from mneia_backend.models.link_type import LinkType as _LinkType

from mneia_exporter.mixins import Exportable


class LinkType(_LinkType, Exportable):
    class Meta:
        verbose_name_plural = "Link Types"
        proxy = True
