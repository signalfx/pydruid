def build_granularity(granularity):
    if isinstance(granularity, Granularity):
        granularity = granularity.build()

    return granularity


class Granularity(object):

    granularity_type = None

    def build(self):
        if self.granularity_type:
            return {"type": self.granularity_type}
        else:
            return {}


class DurationGranularity(Granularity):

    granularity_type = "duration"

    def __init__(self, duration, origin=None):
        super(Granularity, self).__init__()
        self._duration = duration
        self._origin = origin

    def build(self):
        granularity = super(DurationGranularity, self).build()
        if self._duration:
            granularity["duration"] = self._duration

        if self._origin:
            granularity["origin"] = self._origin

        return granularity
