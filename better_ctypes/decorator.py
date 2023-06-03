import functools


def typed_structure(cls):
    @functools.wraps(cls)
    def wrapper():
        annotations = {
            attr_name: attr_hint
            for attr_name, attr_hint in cls.__annotations__.items()
            if not attr_name.startswith("_")
        }

        struct = type(cls.__name__, (*cls.__bases__, cls), {})

        fields = getattr(cls, "fields") or []

        for attr_name, attr_hint in annotations.items():
            fields.append((attr_name, attr_hint))

        struct._fields_ = fields

        return struct

    return wrapper
