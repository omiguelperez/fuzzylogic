class Variable(object):
    """This class contains Variable capability."""

    def __init__(self, name, fuzzy_sets=[]):
        """Set Initial Variable config."""
        super(Variable, self).__init__()
        self.name = name
        self.fuzzy_sets = fuzzy_sets
