from mneia_backend.models.area_type import AreaType as _AreaType

from mneia_exporter.mixins import Exportable


class AreaType(_AreaType, Exportable):
    """
    Extends the AreaType model from `mneia-backend` to add export-specific functionality.
    """

    @property
    def as_json(self):
        _ = dict(self._as_json)  # create a copy
        _.update(
            {
                "mbid": self.mbid,
                "name": self.name,
                "parent": self.parent,
                "child_order": self.child_order,
                "description": self.description,
            }
        )
        return _

    class Meta:
        proxy = True
