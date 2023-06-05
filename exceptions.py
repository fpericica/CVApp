"""
exceptions.py

This module provides custom exception classes used in the application.

Exceptions:
- EmptyDataException: Exception raised when the data is empty or invalid.
- NotFoundException: Exception raised when a resource is not found.
"""
class EmptyDataException(Exception):
    pass


class NotFoundException(Exception):
    pass
