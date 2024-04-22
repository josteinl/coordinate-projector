from pyproj import Transformer
from typing import Dict, Optional
from .projections import projections

_transformers: Dict[str, Transformer] = {}


class Projector:
    @staticmethod
    def get_supported_projections() -> Dict:
        return projections

    @staticmethod
    def _get_transformer(from_srid: int, to_srid: int, pipeline: str | None) -> Transformer:
        global _transformers

        if pipeline:
            transformer_key = f"{from_srid}-{pipeline}-{to_srid}"
        else:
            transformer_key = f"{from_srid}-{to_srid}"

        if transformer := _transformers.get(transformer_key):
            return transformer

        from_def_desc: Optional[Dict] = projections.get(str(from_srid))
        if not from_def_desc:
            raise Exception(f"SRID: {from_srid} is not supported")
        from_definition = from_def_desc["definition"]["data"]

        to_def_desc: Optional[Dict] = projections.get(str(to_srid))
        if not to_def_desc:
            raise Exception(f"SRID: {to_srid} is not supported")
        to_definition = to_def_desc["definition"]["data"]

        transformer = Transformer.from_crs(from_definition, to_definition)

        _transformers["transformer_key"] = transformer

        return transformer

    def transform(
        self, from_srid: int, to_srid: int, east: float, north: float, pipeline: str | None
    ) -> tuple[float, float]:
        transformer: Transformer = self._get_transformer(from_srid, to_srid)
        projected_east, projected_north = transformer.transform(east, north)
        return projected_east, projected_north
