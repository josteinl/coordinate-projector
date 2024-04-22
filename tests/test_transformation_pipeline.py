import pytest

from coordinate_projector import Projector

WGS84 = 4326


class TestTransformationPipeline:
    # fmt: off
    @pytest.mark.parametrize(
        "latitude, longitude, pipeline, to_srid, expected_northing, expected_easting",
        (
            (64.2661036327733, 5.2586365502776875, None, 3857, 9417662.27699099, 585388.743043809),
            (64.2661036327733, 5.2586365502776875, "urn:ogc:def:coordinateOperation:EPSG:1612", 3857, 9417662.27699099, 585388.743043809),
            (64.2661036327733, 5.2586365502776875, None, 23032, 7132208.08, 318903.87),
        ),
    )
    # fmt: on
    def test_tranformation_pipeline(self, latitude, longitude, pipeline, to_srid, expected_northing, expected_easting):

        # A) Y: Lat(64.2661036327733)  X: Lon(5.2586365502776875) EPSG:4326 is in degrees - 3D sphere
        # B) Y: Lat(9417662.27699099) X: Lon(585388.743043809) EPSG:3857 is in metres - 2D projection
        # C) X: 318903.87 Y: 7132208.08 metre EPSG:23032 ED50 / UTM zone 32N

        projector = Projector()
        easting, northing = projector.transform(from_srid=WGS84, to_srid=to_srid, east=longitude, north=latitude)
        assert easting == pytest.approx(expected_easting)
        assert northing == pytest.approx(expected_northing)
