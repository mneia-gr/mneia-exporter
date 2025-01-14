from mneia_backend.models.area_type import AreaType as _AreaType

from mneia_exporter.mixins import Exportable


class AreaType(_AreaType, Exportable):
    class Meta:
        proxy = True
