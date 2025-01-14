from mneia_backend.models.person import Person as _Person

from mneia_exporter.mixins import Exportable


class Person(_Person, Exportable):
    class Meta:
        verbose_name_plural = "People"
        proxy = True
