class RequestSchema:
    required_fields: set[str] = set()
    optional_fields: set[str] = set()

    @classmethod
    def validate(cls, payload: dict):
        missing = cls.required_fields - payload.keys()
        if missing:
            raise ValueError(f"Missing fields: {missing}")
