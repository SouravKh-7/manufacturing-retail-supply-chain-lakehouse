"""Initial source contracts; no pipeline behavior is implemented here."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SourceContract:
    name: str
    grain: str
    business_keys: tuple[str, ...]
    event_time_column: str
    arrival_time_column: str
    change_mode: str

    def validate(self) -> None:
        if not self.name.strip():
            raise ValueError("source name is required")
        if not self.grain.strip():
            raise ValueError("source grain is required")
        if not self.business_keys:
            raise ValueError("at least one business key is required")

