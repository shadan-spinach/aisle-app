"""
Custom exceptions for the application.
"""

class AisleAppException(Exception):
    """Base class for application exceptions."""
    pass

class InvalidInputError(AisleAppException):
    """Raised when input is invalid."""
    pass

class CalculationError(AisleAppException):
    """Raised for errors during tax calculation."""
    pass
