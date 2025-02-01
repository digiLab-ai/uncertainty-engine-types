import json

from pydantic import BaseModel


class SensorDesigner(BaseModel):
    bed: dict

    def load_sensor_designer(self):

        from twinlab_bed.BED import BED

        bed = BED.from_json(json.dumps(self.bed))

        return bed


def save_sensor_designer(bed) -> SensorDesigner:
    return SensorDesigner(bed=json.loads(bed.to_json()))
