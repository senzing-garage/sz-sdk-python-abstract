#! /usr/bin/env python3

"""
szabstractfactory_abstract.py is the abstract class for all implementations of szabstractfactory.
"""


from abc import ABC, abstractmethod

from senzing_abstract import (
    SzConfigAbstract,
    SzConfigManagerAbstract,
    SzDiagnosticAbstract,
    SzEngineAbstract,
    SzProductAbstract,
)

# Metadata

__all__ = ["SzAbstractFactoryAbstract"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2024-09-23"
__updated__ = "2024-09-23"

# -----------------------------------------------------------------------------
# SzAbstractFactoryAbstract
# -----------------------------------------------------------------------------


class SzAbstractFactoryAbstract(ABC):
    """
    SzAbstractFactoryAbstract is the definition of the Senzing Python API
    SzAbstractFactory implementations.
    """

    # -------------------------------------------------------------------------
    # Interface definition
    # -------------------------------------------------------------------------

    @abstractmethod
    def create_sz_config(self) -> SzConfigAbstract:
        """
        The `create_sz_config` method creates a new implementation of an `SzConfigAbstract` object.

        Args:

        Returns:
            SzConfigAbstract: A new implementation.

        Raises:

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szabstractfactory/create_sz_config.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szabstractfactory/create_sz_config.txt
                :linenos:
                :language: json
        """

    @abstractmethod
    def create_sz_configmanager(self) -> SzConfigManagerAbstract:
        """
        The `create_sz_configmanager` method creates a new implementation of an `SzConfigManagerAbstract` object.

        Args:

        Returns:
            SzConfigManagerAbstract: A new implementation.

        Raises:

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szabstractfactory/create_sz_configmanager.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szabstractfactory/create_sz_configmanger.txt
                :linenos:
                :language: json
        """

    @abstractmethod
    def create_sz_diagnostic(self) -> SzDiagnosticAbstract:
        """
        The `create_sz_diagnostic` method creates a new implementation of an `SzDiagnosticAbstract` object.

        Args:

        Returns:
            SzDiagnosticAbstract: A new implementation.

        Raises:

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szabstractfactory/create_sz_diagnostic.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szabstractfactory/create_sz_diagnostic.txt
                :linenos:
                :language: json
        """

    @abstractmethod
    def create_sz_engine(self) -> SzEngineAbstract:
        """
        The `create_sz_engine` method creates a new implementation of an `SzEngineAbstract` object.

        Args:

        Returns:
            SzEngineAbstract: A new implementation.

        Raises:

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szabstractfactory/create_sz_engine.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szabstractfactory/create_sz_engine.txt
                :linenos:
                :language: json
        """

    @abstractmethod
    def create_sz_product(self) -> SzProductAbstract:
        """
        The `create_sz_product` method creates a new implementation of an `SzProductAbstract` object.

        Args:

        Returns:
            SzProductAbstract: A new implementation.

        Raises:

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szabstractfactory/create_sz_product.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szabstractfactory/create_sz_product.txt
                :linenos:
                :language: json
        """