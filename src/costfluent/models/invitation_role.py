from enum import StrEnum


class InvitationRole(StrEnum):
    EDITOR = "editor"
    INTEGRATIONOWNER = "integrationOwner"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
