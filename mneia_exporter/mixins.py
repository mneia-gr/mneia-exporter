from pathlib import Path
from typing import Dict

from django.utils.text import slugify


class Exportable:
    @property
    def export_path(self) -> Path:
        return Path.home() / "Mneia" / "mneia-data" / f"{slugify(self._meta.verbose_name_plural)}" / f"{self.id}.json"

    @property
    def _as_json(self) -> Dict:
        return {
            "id": str(self.id),
            "created_in_mneia": str(self.created_in_mneia),
            "updated_in_mneia": str(self.updated_in_mneia),
        }
