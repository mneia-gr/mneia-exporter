from mneia_backend.models.links.person_photograph import LinkPersonPhotograph as _LinkPersonPhotograph

from mneia_exporter.mixins import Exportable


class LinkPersonPhotograph(_LinkPersonPhotograph, Exportable):
    class Meta:
        verbose_name_plural = "Links Person Photograph"
        proxy = True
