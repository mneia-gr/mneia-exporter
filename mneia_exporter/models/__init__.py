from django_musicbrainz_connector.models.area_type import AreaType as _MusicBrainzAreaType
from django_musicbrainz_connector.models.artist_type import ArtistType as _MusicBrainzArtistType
from django_musicbrainz_connector.models.gender import Gender as _MusicBrainzGender
from django_musicbrainz_connector.models.link_attribute_type import LinkAttributeType as _MusicBrainzLinkAttributeType
from django_musicbrainz_connector.models.work_type import WorkType as _MusicBrainzWorkType

from mneia_exporter.models.abstract import Exportable, SampleExportable


class MusicBrainzAreaType(_MusicBrainzAreaType, Exportable):
    class Meta:
        verbose_name_plural = "Area Types"
        proxy = True


class MusicBrainzWorkType(_MusicBrainzWorkType, Exportable):
    class Meta:
        verbose_name_plural = "Work Types"
        proxy = True


class MusicBrainzGender(_MusicBrainzGender, Exportable):
    class Meta:
        verbose_name_plural = "Genders"
        proxy = True


class MusicBrainzArtistType(_MusicBrainzArtistType, Exportable):
    class Meta:
        verbose_name_plural = "Artist Types"
        proxy = True


class MusicBrainzLinkAttributeType(_MusicBrainzLinkAttributeType, SampleExportable):
    class Meta:
        verbose_name_plural = "Link Attribute Types"
        proxy = True
