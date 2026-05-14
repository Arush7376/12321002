class BaseRepository:
    """Small repository base for model queries."""

    model = None

    def get_queryset(self):
        if self.model is None:
            raise NotImplementedError("Repository model must be defined.")
        return self.model.objects.all()
