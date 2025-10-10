"""
Chemical Engineering Unit Converter (cheuc)

A comprehensive unit converter package for chemical engineering applications.
Handles SI units with prefixes, dimensional analysis, and complex unit expressions.

Key Features:
- Single conversion function for all unit types
- Automatic prefix parsing (kilo, milli, micro, etc.)
- Dimensional analysis to prevent invalid conversions
- Support for complex unit expressions (W/(m2.K), Btu/(h.ft2.degF), etc.)
- Chemical engineering specific units (lbmol, psia, Btu, etc.)

Usage:
    >>> from che_unit_converter import cheuc
    >>> cheuc(1, 'kW/(m2.K)', 'W/(m2.K)')  # 1000.0
    >>> cheuc(100, 'cm', 'm')              # 1.0
    >>> cheuc(1, 'lbmol', 'gmol')          # 453.59237

The cheuc function is the main interface for unit conversions.
"""

from .che_unit_converter import ChemEngUnitConverter

# Create a singleton instance
_converter = ChemEngUnitConverter()

def convert(value, from_unit, to_unit):
    """
    Convert a value from one unit to another.
    
    This is the main conversion function that handles all unit conversions
    with dimensional analysis and automatic prefix parsing.
    
    Args:
        value: Numerical value to convert
        from_unit: Source unit expression (e.g., 'kW/(m2.K)', 'mm', 'Btu/(h.ft2.degF)')
        to_unit: Target unit expression (e.g., 'W/(m2.K)', 'cm', 'kW/(m2.K)')
        
    Returns:
        Converted value
        
    Raises:
        ValueError: If units have incompatible dimensions or unknown units
        
    Examples:
        >>> convert(1, 'kW/(m2.K)', 'W/(m2.K)')  # 1000.0
        >>> convert(100, 'cm', 'm')              # 1.0
        >>> convert(1, 'lbmol', 'gmol')          # 453.59237
        >>> convert(100, 'degC', 'degF')         # 212.0
    """
    return _converter.convert(value, from_unit, to_unit)

# Create alias
cheuc = convert

# Version
__version__ = "1.0.0"
__author__ = "Chemical Engineering Tools"
__description__ = "Chemical Engineering Unit Converter with dimensional analysis"

# Only export the convert function and its alias
__all__ = ['convert', 'cheuc']