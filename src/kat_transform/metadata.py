import typing

T = typing.TypeVar("T", bound="Metadata")


class Metadata:
    def __init__(self) -> None:
        self.entries: tuple[Metadata, ...] = (self,)

    def get_metadata(self, metadata_type: type[T], exact: bool = False) -> T | None:
        for entry in self.entries:
            if type(entry) is metadata_type:
                return entry

            if not exact and isinstance(entry, metadata_type):
                return entry

        return None

    def __or__(self, other: "Metadata") -> "CombinedMetadata":
        return CombinedMetadata(*self.entries, *other.entries)


class CombinedMetadata(Metadata):
    def __init__(self, *entries: Metadata):
        super().__init__()
        self.entries: tuple[Metadata, ...] = entries


class FieldMetadata(Metadata):
    """
    Field metadata that can be used by other tools (like json schema generation)

    This is fully customisable and up to you, how to and for what use it
    """


class SchemaMetadata(Metadata):
    """
    Schema metadata that can be used by other tools (like json schema generation)

    This is fully customisable and up to you, how to and for what use it
    """
