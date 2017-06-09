class Rule(object):
    """This class contains the Rule capability."""

    def __init__(self, inputs, outputs):
        """Set Rule initial config."""
        super(Rule, self).__init__()
        self.inputs = inputs
        self.outputs = outputs
        