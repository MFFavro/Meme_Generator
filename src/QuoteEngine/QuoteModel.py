"""Make a quote model."""
class QuoteModel:
    """Representation for quotes."""

    def __init__(self, body, author):
        """Create a new quote model."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Representation of a quote model."""
        return f"{self.body} - {self.author}"
