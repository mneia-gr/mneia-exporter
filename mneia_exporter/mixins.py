import json
from pathlib import Path
from typing import Dict

from django.db import models
from django.utils.text import slugify


class Exportable:
    @property
    def export_dir(self) -> Path:
        return Path.home() / "Mneia" / "mneia-data" / f"{slugify(self._meta.verbose_name_plural)}"

    @property
    def export_file(self) -> Path:
        return self.export_dir / f"{self.id}.json"

    def export(self) -> None:
        self.export_dir.mkdir(parents=True, exist_ok=True)
        self.export_file.write_text(json.dumps(self.as_json, indent=2, ensure_ascii=False, sort_keys=True))

    @property
    def as_json(self) -> Dict:
        _as_json = {}
        for field in self._meta.fields:
            if isinstance(field, models.UUIDField) or isinstance(field, models.DateTimeField):
                _as_json[field.name] = str(getattr(self, field.name))
            elif isinstance(field, models.ForeignKey):
                related_instance = getattr(self, field.name)
                _as_json[field.name] = str(related_instance.id) if related_instance is not None else None
            else:
                _as_json[field.name] = getattr(self, field.name)
        return _as_json
