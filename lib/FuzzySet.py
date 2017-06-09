class FuzzySet(object):
    """This class contains FuzzySet capability."""

    def __init__(self, name, left_interval, right_interval):
        """Set FuzzySet initial config."""
        super(FuzzySet, self).__init__()
        self.name = name
        self.left_interval = left_interval
        self.right_interval = right_interval