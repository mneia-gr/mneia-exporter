from mneia_backend.models.area import Area as _Area

from mneia_exporter.mixins import Exportable


class Area(_Area, Exportable):
    @property
    def as_json(self):
        _ = dict(self._as_json)  # create a copy
        _.update(
            {
                "mbid": self.mbid,
                "name": self.name,
                "type": str(self.type.id),
                "edits_pending": self.edits_pending,
                "last_updated": str(self.last_updated),
                "begin_date_year": self.begin_date_year,
                "begin_date_month": self.begin_date_month,
                "begin_date_day": self.begin_date_day,
                "end_date_year": self.end_date_year,
                "end_date_month": self.end_date_month,
                "end_date_day": self.end_date_day,
                "ended": self.ended,
                "comment": self.comment,
            }
        )
        return _

    class Meta:
        proxy = True
