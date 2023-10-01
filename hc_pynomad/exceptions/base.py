class NomadAPIError(Exception):
    """Returned with Nomad responses with an HTTP 400"""
    pass


class NomadAgentError(Exception):
    """Returned when a Nomad Agent call fails."""
    pass


class Unauthenticated(Exception):
    """Raised when an API call fails where we receive a 403 status code."""
    pass


class UnknownResourceCalled(Exception):
    """Raised when an API call is made but the cluster doesn't support it."""
    pass
