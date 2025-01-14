from mneia_backend.models.gender import Gender as _Gender

from mneia_exporter.mixins import Exportable


class Gender(_Gender, Exportable):
    class Meta:
        proxy = True
