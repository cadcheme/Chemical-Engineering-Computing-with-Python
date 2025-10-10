"""
Chemical Engineering Unit Converter (cheuc)
A comprehensive unit converter for chemical engineering applications.
Handles SI units with prefixes, dimensional analysis, and complex unit expressions.

Mohammad Rahmani
Chemical Engineering Department
Amirkabir University of Technology
Oct 10th, 2025


Created wuth the help from DeepSeek AI assistant.

https://chat.deepseek.com/share/rt7z9pcygouzx17nqi
"""

class ChemEngUnitConverter:
    """
    A comprehensive unit converter for chemical engineering applications.
    Handles SI units with prefixes and complex unit expressions.
    Uses only ASCII characters for compatibility.
    """
    
    # Base dimensions: length, mass, time, temperature, amount, current, luminous intensity
    DIMENSIONS = ['L', 'M', 'T', 'Θ', 'N', 'I', 'J']
    
    # Base SI units conversion factors (to SI base) with their dimensions
    BASE_UNITS = {
        # Length (base: meter) - dimension L
        'm': {'factor': 1.0, 'dimensions': {'L': 1}},
        'ft': {'factor': 0.3048, 'dimensions': {'L': 1}},
        'in': {'factor': 0.0254, 'dimensions': {'L': 1}},
        
        # Mass (base: kilogram) - dimension M
        'g': {'factor': 0.001, 'dimensions': {'M': 1}},
        'kg': {'factor': 1.0, 'dimensions': {'M': 1}},
        'lb': {'factor': 0.453592, 'dimensions': {'M': 1}},
        'lbm': {'factor': 0.453592, 'dimensions': {'M': 1}},
        
        # Time (base: second) - dimension T
        's': {'factor': 1.0, 'dimensions': {'T': 1}},
        'min': {'factor': 60.0, 'dimensions': {'T': 1}},
        'hr': {'factor': 3600.0, 'dimensions': {'T': 1}},
        'h': {'factor': 3600.0, 'dimensions': {'T': 1}},
        
        # Temperature (base: Kelvin) - dimension Θ
        'K': {'factor': 1.0, 'dimensions': {'Θ': 1}},
        
        # Current (base: Ampere) - dimension I
        'A': {'factor': 1.0, 'dimensions': {'I': 1}},
        
        # Amount of substance (base: mole) - dimension N
        'mol': {'factor': 1.0, 'dimensions': {'N': 1}},
        'gmol': {'factor': 1.0, 'dimensions': {'N': 1}},
        'lbmol': {'factor': 453.59237, 'dimensions': {'N': 1}},
        
        # Luminous intensity (base: candela) - dimension J
        'cd': {'factor': 1.0, 'dimensions': {'J': 1}},
    }
    
    # Derived units conversion factors (to SI equivalent) with their dimensions
    DERIVED_UNITS = {
        # Force (base: Newton) - M·L/T²
        'N': {'factor': 1.0, 'dimensions': {'M': 1, 'L': 1, 'T': -2}},
        'lbf': {'factor': 4.44822, 'dimensions': {'M': 1, 'L': 1, 'T': -2}},
        
        # Pressure (base: Pascal) - M/(L·T²)
        'Pa': {'factor': 1.0, 'dimensions': {'M': 1, 'L': -1, 'T': -2}},
        'bar': {'factor': 1e5, 'dimensions': {'M': 1, 'L': -1, 'T': -2}},
        'atm': {'factor': 101325.0, 'dimensions': {'M': 1, 'L': -1, 'T': -2}},
        'psi': {'factor': 6894.76, 'dimensions': {'M': 1, 'L': -1, 'T': -2}},
        'torr': {'factor': 133.322, 'dimensions': {'M': 1, 'L': -1, 'T': -2}},
        'mmHg': {'factor': 133.322, 'dimensions': {'M': 1, 'L': -1, 'T': -2}},
        
        # Energy (base: Joule) - M·L²/T²
        'J': {'factor': 1.0, 'dimensions': {'M': 1, 'L': 2, 'T': -2}},
        'cal': {'factor': 4.184, 'dimensions': {'M': 1, 'L': 2, 'T': -2}},
        'Btu': {'factor': 1055.06, 'dimensions': {'M': 1, 'L': 2, 'T': -2}},
        'kWh': {'factor': 3.6e6, 'dimensions': {'M': 1, 'L': 2, 'T': -2}},
        
        # Power (base: Watt) - M·L²/T³
        'W': {'factor': 1.0, 'dimensions': {'M': 1, 'L': 2, 'T': -3}},
        'hp': {'factor': 745.7, 'dimensions': {'M': 1, 'L': 2, 'T': -3}},
        
        # Volume (base: cubic meter) - L³
        'L': {'factor': 0.001, 'dimensions': {'L': 3}},
        'gal': {'factor': 0.00378541, 'dimensions': {'L': 3}},
        
        
        # Viscosity - M/(L·T)
         'cP': {'factor': 0.001, 'dimensions': {'M': 1, 'L': -1, 'T': -1}},
         'P': {'factor': 0.1, 'dimensions': {'M': 1, 'L': -1, 'T': -1}},        
    }
    
    # SI prefixes
    PREFIXES = {
        'Y': 1e24, 'Z': 1e21, 'E': 1e18, 'P': 1e15, 'T': 1e12, 'G': 1e9, 'M': 1e6,
        'k': 1e3, 'h': 1e2, 'da': 1e1, 'd': 1e-1, 'c': 1e-2, 'm': 1e-3,
        'mu': 1e-6, 'u': 1e-6, 'n': 1e-9, 'p': 1e-12, 'f': 1e-15, 'a': 1e-18,
        'z': 1e-21, 'y': 1e-24,
    }
    
    # Temperature conversion functions (special handling)
    TEMPERATURE_UNITS = {'K', 'degC', 'degF', 'degR'}
    
    def __init__(self):
        # Build comprehensive unit dictionary
        self.unit_dict = {}
        self.dimension_dict = {}
        self._build_unit_dictionary()
    
    def _build_unit_dictionary(self):
        """Build a comprehensive dictionary of all supported units with prefixes."""
        # Add base units
        for unit, data in self.BASE_UNITS.items():
            self.unit_dict[unit] = data['factor']
            self.dimension_dict[unit] = data['dimensions']
        
        # Add derived units
        for unit, data in self.DERIVED_UNITS.items():
            self.unit_dict[unit] = data['factor']
            self.dimension_dict[unit] = data['dimensions']
        
        # Generate prefixed units for base SI units
        base_si_units = ['m', 'g', 's', 'A', 'mol', 'gmol', 'cd', 'Pa', 'J', 'W', 'N', 'L']
        
        for base_unit in base_si_units:
            for prefix, factor in self.PREFIXES.items():
                # Skip invalid combinations
                if base_unit == 'kg' and prefix == 'k':  # kg already has kilo
                    continue
                if base_unit == 'L' and prefix in ['d', 'c']:  # dL, cL are common
                    pass
                if base_unit == 'gmol' and prefix == 'k':  # kgmol is uncommon
                    continue
                    
                prefixed_unit = prefix + base_unit
                
                # Calculate conversion factor and copy dimensions
                if base_unit in self.BASE_UNITS:
                    base_factor = self.BASE_UNITS[base_unit]['factor']
                    base_dimensions = self.BASE_UNITS[base_unit]['dimensions']
                elif base_unit in self.DERIVED_UNITS:
                    base_factor = self.DERIVED_UNITS[base_unit]['factor']
                    base_dimensions = self.DERIVED_UNITS[base_unit]['dimensions']
                else:
                    continue
                
                self.unit_dict[prefixed_unit] = base_factor * factor
                self.dimension_dict[prefixed_unit] = base_dimensions.copy()
    
    def convert(self, value, from_unit, to_unit):
        """
        Convert a value from one unit to another.
        Handles complex unit expressions and automatic prefix parsing.
        
        Args:
            value: Numerical value to convert
            from_unit: Source unit expression (e.g., 'kW/(m2.K)', 'mm', 'Btu/(h.ft2.degF)')
            to_unit: Target unit expression (e.g., 'W/(m2.K)', 'cm', 'kW/(m2.K)')
            
        Returns:
            Converted value
            
        Raises:
            ValueError: If units have incompatible dimensions
            
        Examples:
            >>> conv.convert(1, 'kW/(m2.K)', 'W/(m2.K)')  # 1000
            >>> conv.convert(100, 'cm', 'm')              # 1
            >>> conv.convert(1, 'lbmol', 'gmol')          # 453.59237
        """
        # Handle temperature units separately
        if from_unit in self.TEMPERATURE_UNITS and to_unit in self.TEMPERATURE_UNITS:
            return self._convert_temperature(value, from_unit, to_unit)
        
        # Parse and convert complex unit expressions
        from_factor, from_dims = self._parse_unit_expression_with_dims(from_unit)
        to_factor, to_dims = self._parse_unit_expression_with_dims(to_unit)
        
        # Check dimensional compatibility
        if not self._check_dimensional_compatibility(from_dims, to_dims):
            raise ValueError(f"Incompatible dimensions: {from_unit} has dimensions {from_dims}, "
                           f"but {to_unit} has dimensions {to_dims}")
        
        return value * (from_factor / to_factor)
    
    def _parse_unit_expression_with_dims(self, unit_expr):
        """
        Parse a unit expression and return its conversion factor and dimensions.
        
        Args:
            unit_expr: Unit expression string
            
        Returns:
            Tuple of (conversion_factor, dimensions_dict)
        """
        if not unit_expr or unit_expr == '1' or unit_expr == 'dimensionless':
            return 1.0, {}
        
        # Handle simple units (no division, no multiplication)
        if '/' not in unit_expr and '.' not in unit_expr:
            return self._parse_simple_unit_with_dims(unit_expr)
        
        # Handle division and multiplication in units
        parts = self._split_unit_expression(unit_expr)
        
        numerator_factor = 1.0
        denominator_factor = 1.0
        numerator_dims = {}
        denominator_dims = {}
        
        # Parse numerator parts
        for part in parts['numerator']:
            if '.' in part:
                # Handle multiplication in numerator
                subparts = part.split('.')
                subfactor = 1.0
                subdims = {}
                for subpart in subparts:
                    factor, dims = self._parse_simple_unit_with_dims(subpart)
                    subfactor *= factor
                    # Add dimensions for multiplication
                    for dim, exp in dims.items():
                        subdims[dim] = subdims.get(dim, 0) + exp
                numerator_factor *= subfactor
                for dim, exp in subdims.items():
                    numerator_dims[dim] = numerator_dims.get(dim, 0) + exp
            else:
                factor, dims = self._parse_simple_unit_with_dims(part)
                numerator_factor *= factor
                for dim, exp in dims.items():
                    numerator_dims[dim] = numerator_dims.get(dim, 0) + exp
            
        # Parse denominator parts
        for part in parts['denominator']:
            if '.' in part:
                # Handle multiplication in denominator
                subparts = part.split('.')
                subfactor = 1.0
                subdims = {}
                for subpart in subparts:
                    factor, dims = self._parse_simple_unit_with_dims(subpart)
                    subfactor *= factor
                    # Add dimensions for multiplication
                    for dim, exp in dims.items():
                        subdims[dim] = subdims.get(dim, 0) + exp
                denominator_factor *= subfactor
                for dim, exp in subdims.items():
                    denominator_dims[dim] = denominator_dims.get(dim, 0) + exp
            else:
                factor, dims = self._parse_simple_unit_with_dims(part)
                denominator_factor *= factor
                for dim, exp in dims.items():
                    denominator_dims[dim] = denominator_dims.get(dim, 0) + exp
        
        # For division, subtract denominator dimensions from numerator dimensions
        final_dims = numerator_dims.copy()
        for dim, exp in denominator_dims.items():
            final_dims[dim] = final_dims.get(dim, 0) - exp
        
        return numerator_factor / denominator_factor, final_dims
    
    def _parse_simple_unit_with_dims(self, unit_str):
        """
        Parse a simple unit and return its conversion factor and dimensions.
        
        Args:
            unit_str: Simple unit string
            
        Returns:
            Tuple of (conversion_factor, dimensions_dict)
        """
        if not unit_str or unit_str == '1':
            return 1.0, {}
        
        # Handle temperature units
        if unit_str in self.TEMPERATURE_UNITS:
            # For temperature differences, use scale factors
            if unit_str == 'K' or unit_str == 'degC':
                return 1.0, {'Θ': 1}
            elif unit_str == 'degF' or unit_str == 'degR':
                return 5/9, {'Θ': 1}
        
        # Handle units with powers
        power = 1
        base_unit = unit_str
        
        # Check for power suffix
        if unit_str[-1].isdigit():
            i = len(unit_str) - 1
            while i >= 0 and unit_str[i].isdigit():
                i -= 1
            i += 1
            power = int(unit_str[i:])
            base_unit = unit_str[:i]
        
        # Get conversion factor and dimensions for base unit
        base_factor = self._get_unit_factor(base_unit)
        base_dims = self._get_unit_dimensions(base_unit)
        
        # Apply power to dimensions
        final_dims = {dim: exp * power for dim, exp in base_dims.items()}
        
        return base_factor ** power, final_dims
    
    def _get_unit_dimensions(self, unit):
        """Get the dimensional representation of a unit."""
        if unit in self.dimension_dict:
            return self.dimension_dict[unit]
        
        # Try to find unit with prefixes
        for prefix in self.PREFIXES:
            if unit.startswith(prefix):
                base_unit = unit[len(prefix):]
                if base_unit in self.dimension_dict:
                    return self.dimension_dict[base_unit]
        
        if unit == 'kg':
            return {'M': 1}
        
        raise ValueError(f"Unknown unit: {unit}")
    
    def _get_unit_factor(self, unit):
        """Get conversion factor for a base unit."""
        if unit in self.unit_dict:
            return self.unit_dict[unit]
        
        for prefix, prefix_factor in self.PREFIXES.items():
            if unit.startswith(prefix):
                base_unit = unit[len(prefix):]
                if base_unit in self.unit_dict:
                    return self.unit_dict[base_unit] * prefix_factor
        
        if unit == 'kg':
            return 1.0
        
        raise ValueError(f"Unknown unit: {unit}")
    
    def _check_dimensional_compatibility(self, from_dims, to_dims):
        """Check if two dimensional representations are compatible."""
        # Normalize dimensions by filling missing dimensions with 0
        all_dims = set(from_dims.keys()) | set(to_dims.keys())
        
        for dim in all_dims:
            from_exp = from_dims.get(dim, 0)
            to_exp = to_dims.get(dim, 0)
            if from_exp != to_exp:
                return False
        return True
    
    def _split_unit_expression(self, unit_expr):
        """Split a unit expression into numerator and denominator parts."""
        # Remove spaces
        expr = unit_expr.replace(' ', '')
        
        # Check if the expression has division
        if '/' not in expr:
            return {'numerator': [expr], 'denominator': ['1']}
        
        # Split into numerator and denominator
        if '(' in expr and ')' in expr:
            parts = expr.split('/', 1)
            numerator = parts[0]
            denominator = parts[1]
            
            if denominator.startswith('(') and denominator.endswith(')'):
                denominator = denominator[1:-1]
            if numerator.startswith('(') and numerator.endswith(')'):
                numerator = numerator[1:-1]
                
            return {'numerator': [numerator], 'denominator': [denominator]}
        else:
            parts = expr.split('/')
            numerator = parts[0]
            denominator_parts = parts[1:] if len(parts) > 1 else ['1']
            return {'numerator': [numerator], 'denominator': denominator_parts}
    
    def _convert_temperature(self, value, from_unit, to_unit):
        """Convert temperature values."""
        if from_unit == 'K':
            temp_k = value
        elif from_unit == 'degC':
            temp_k = value + 273.15
        elif from_unit == 'degF':
            temp_k = (value - 32) * 5/9 + 273.15
        elif from_unit == 'degR':
            temp_k = value * 5/9
        else:
            raise ValueError(f"Unknown temperature unit: {from_unit}")
        
        if to_unit == 'K':
            return temp_k
        elif to_unit == 'degC':
            return temp_k - 273.15
        elif to_unit == 'degF':
            return (temp_k - 273.15) * 9/5 + 32
        elif to_unit == 'degR':
            return temp_k * 9/5
        else:
            raise ValueError(f"Unknown temperature unit: {to_unit}")