from pathlib import Path
from unittest import mock

import pytest

from mneia_exporter.models.area_type import AreaType


@mock.patch.object(Path, "home")
def test_area_type_export_dir(mock_path_home):
    mock_path_home.return_value = Path("/foo/bar/")

    area_type = AreaType(id="0c543ef3-942c-4a8f-8809-2c96b9ecef2d")
    assert area_type.export_dir == Path("/foo/bar/Mneia/mneia-data/area-types/")


@mock.patch.object(Path, "home")
def test_area_type_export_file(mock_path_home):
    mock_path_home.return_value = Path("/foo/bar/")

    area_type = AreaType(id="0c543ef3-942c-4a8f-8809-2c96b9ecef2d")
    assert area_type.export_file == Path(
        "/foo/bar/Mneia/mneia-data/area-types/0c543ef3-942c-4a8f-8809-2c96b9ecef2d.json"
    )


@pytest.mark.django_db
def test_area_type_as_json():
    area_type = AreaType.objects.get(id="06dd0ae4-8c74-30bb-b43d-95dcedf961de")  # from fixture
    assert area_type.as_json == {
        "id": "06dd0ae4-8c74-30bb-b43d-95dcedf961de",
        "mbid": 1,
        "name": "Country",
        "parent": None,
        "child_order": 1,
        "description": "Country is used for areas included (or previously included) in ISO 3166-1, e.g. United States.",
        "created_in_mneia": "2025-01-10 13:42:00+00:00",
        "updated_in_mneia": "2025-01-10 13:42:00+00:00",
    }
