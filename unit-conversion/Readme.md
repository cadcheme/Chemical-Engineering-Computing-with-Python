# Chemical Engineering Unit Converter (cheuc)

A comprehensive Python unit converter package specifically designed for chemical engineering applications. Handles SI units with prefixes, dimensional analysis, and complex unit expressions with a simple, intuitive interface.

## Features

- **Single Function Interface**: One function `cheuc()` handles all conversions
- **Dimensional Analysis**: Prevents physically meaningless conversions
- **Automatic Prefix Parsing**: Handles kilo, milli, micro, and all SI prefixes
- **Complex Unit Expressions**: Supports `W/(m2.K)`, `Btu/(h.ft2.degF)`, etc.
- **Chemical Engineering Focus**: Includes lbmol, psia, Btu, and other engineering units
- **ASCII Only**: No Unicode characters for maximum compatibility

## Installation

### Option 1: Copy the package
```bash
# Copy the che_unit_converter folder to your project
cp -r che_unit_converter/ your-project/
```

### Option 2: Install as editable package (for development)
```bash
pip install -e /path/to/che_unit_converter
```

## Quick Start

```python
from che_unit_converter import cheuc

# Simple conversions
print(cheuc(100, 'cm', 'm'))           # 1.0
print(cheuc(1, 'atm', 'kPa'))          # 101.325
print(cheuc(100, 'degC', 'degF'))      # 212.0

# Chemical engineering units
print(cheuc(1, 'lbmol', 'gmol'))       # 453.59237
print(cheuc(1, 'Btu', 'kJ'))           # 1.05506
```

## API Reference

### `cheuc(value, from_unit, to_unit)`

Convert a value from one unit to another.

**Parameters:**
- `value` (float): Numerical value to convert
- `from_unit` (str): Source unit expression
- `to_unit` (str): Target unit expression

**Returns:**
- `float`: Converted value

**Raises:**
- `ValueError`: If units have incompatible dimensions or unknown units

**Examples:**
```python
cheuc(1, 'kW/(m2.K)', 'W/(m2.K)')     # 1000.0
cheuc(100, 'cm', 'm')                 # 1.0
cheuc(1, 'lbmol', 'gmol')             # 453.59237
```

## Supported Units

### Basic SI Units
- **Length**: m, cm, mm, km, ft, in
- **Mass**: kg, g, mg, lb, lbm
- **Time**: s, min, h, hr
- **Temperature**: K, degC, degF, degR
- **Amount**: mol, gmol, lbmol

### Derived Units
- **Force**: N, lbf
- **Pressure**: Pa, kPa, MPa, bar, atm, psi, psia, psig, torr, mmHg
- **Energy**: J, kJ, MJ, cal, kcal, Btu, kW-h
- **Power**: W, kW, MW, hp
- **Volume**: m3, L, mL, gal, ft3

### Chemical Engineering Units
- **Thermal Conductivity**: W/(m.K), Btu/(h.ft.degF)
- **Heat Transfer Coefficient**: W/(m2.K), Btu/(h.ft2.degF)
- **Viscosity**: Pa.s, cP, P
- **Specific Heat**: J/(kg.K), Btu/(lb.degF)
- **Gas Constant**: J/(mol.K), cal/(mol.K), Btu/(lbmol.degR), psia.ft3/(lbmol.degR), atm.L/(mol.K)

### SI Prefixes
All standard SI prefixes are supported: Y, Z, E, P, T, G, M, k, h, da, d, c, m, mu, u, n, p, f, a, z, y

## Examples

### Basic Usage
```python
from che_unit_converter import cheuc

# Length and distance
print(f"10 km to m: {cheuc(10, 'km', 'm')}")      # 10000.0
print(f"1 ft to cm: {cheuc(1, 'ft', 'cm')}")      # 30.48

# Pressure conversions
print(f"1 atm to psi: {cheuc(1, 'atm', 'psi')}")  # 14.6959
print(f"1 bar to kPa: {cheuc(1, 'bar', 'kPa')}")  # 100.0

# Temperature
print(f"100°C to °F: {cheuc(100, 'degC', 'degF')}")  # 212.0
print(f"32°F to °C: {cheuc(32, 'degF', 'degC')}")    # 0.0
```

### Chemical Engineering Examples
```python
from che_unit_converter import cheuc

# Gas constant conversions
R = 8.314  # J/(mol·K)
print(f"R in Btu/(lbmol·°R): {cheuc(R, 'J/(mol.K)', 'Btu/(lbmol.degR)')}")  # 1.98588

# Heat transfer
print(f"1000 W/(m²·K) to Btu/(h·ft²·°F): {cheuc(1000, 'W/(m2.K)', 'Btu/(h.ft2.degF)')}")  # 176.11

# Molar flow rates
print(f"1 kmol/s to lbmol/h: {cheuc(1, 'kmol/s', 'lbmol/h')}")  # 7936.64

# Viscosity
print(f"1 cP to Pa·s: {cheuc(1, 'cP', 'Pa.s')}")  # 0.001
```

### Complex Unit Expressions
```python
from che_unit_converter import cheuc

# Thermal conductivity
print(f"50 W/(m·K) to Btu/(h·ft·°F): {cheuc(50, 'W/(m.K)', 'Btu/(h.ft.degF)')}")

# Specific heat capacity
print(f"1 J/(g·K) to Btu/(lb·°F): {cheuc(1, 'J/(g.K)', 'Btu/(lb.degF)')}")

# Gas constant in different forms
print(f"R in atm·L/(mol·K): {cheuc(8.314, 'J/(mol.K)', 'atm.L/(mol.K)')}")
```

## Dimensional Analysis

The converter includes built-in dimensional analysis to prevent physically meaningless conversions:

```python
from che_unit_converter import cheuc

# These will raise ValueError due to incompatible dimensions
try:
    cheuc(1, 'J/mol', 'Btu/ft')  # Energy/amount vs Energy/length
except ValueError as e:
    print(f"Correctly rejected: {e}")

try:
    cheuc(1, 'm', 'kg')  # Length vs Mass
except ValueError as e:
    print(f"Correctly rejected: {e}")

try:
    cheuc(1, 'Pa', 'J')  # Pressure vs Energy
except ValueError as e:
    print(f"Correctly rejected: {e}")
```

## Running Examples

The package includes comprehensive example files:

```bash
# Run basic examples
python examples/basic_usage.py

# Run chemical engineering examples  
python examples/chemical_engineering.py
```

## File Structure

```
che_unit_converter/
├── __init__.py                 # Main package interface
├── che_unit_converter.py       # Core converter implementation
└── examples/
    ├── basic_usage.py          # Basic conversion examples
    └── chemical_engineering.py # Advanced chemical engineering examples
```

## Error Handling

The converter provides clear error messages:

- **Unknown unit**: `ValueError: Unknown unit: unknown_unit`
- **Incompatible dimensions**: `ValueError: Incompatible dimensions: from_unit has dimensions {...}, but to_unit has dimensions {...}`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new units
4. Ensure all examples work
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this converter in your research, please cite:

```bibtex
@software{che_unit_converter,
  title = {Chemical Engineering Unit Converter},
  author = {Mohammad Rahmani},
  year = {2025},
  url = {https://github.com/yourusername/che-unit-converter}
}
```

## Support

For bugs, feature requests, or questions:
- Open an issue on GitHub
- Check the examples for usage patterns
- Verify unit compatibility using dimensional analysis

---

**Note**: This converter uses ASCII characters only (e.g., `degC`, `degF`, `degR`) for maximum compatibility across different systems and environments.