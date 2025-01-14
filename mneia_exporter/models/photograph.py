from mneia_backend.models.photograph import Photograph as _Photograph

from mneia_exporter.mixins import Exportable


class Photograph(_Photograph, Exportable):
    class Meta:
        proxy = True
