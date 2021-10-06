class ProtectedString(str):
    def __str__(self):
        return "*" * len(self)

    def __repr__(self):
        return "*" * len(self)
