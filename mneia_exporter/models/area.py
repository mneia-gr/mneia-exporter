from mneia_backend.models.area import Area as _Area

from mneia_exporter.mixins import Exportable


class Area(_Area, Exportable):
    class Meta:
        proxy = True
