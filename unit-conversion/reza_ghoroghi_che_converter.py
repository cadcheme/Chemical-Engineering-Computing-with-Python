"""
Pytest test suite for che_unit_converter validation.

This test suite verifies that the converted values are within the specified tolerance and ensures that the
unit converter correctly raises a "ValueError" when encountering dimensionally inconsistent conversions.

The units tested in the default code are selected for typical chemical engineering applications — e.g.,
fluidized bed simulation, heat transfer, reaction kinetics, etc.

References for validation:
    - Unit Converter Pro, Version 3.0 (2000–2006), Elkens Software.
    - Perry’s Chemical Engineers’ Handbook, 9th Edition.

Steps:
    1. Install pytest by running "pip install pytest" in the command prompt.
    2. Add this file to the folder containing che_unit_converter.py and __init__.py.
    3. Define your acceptable tolerance.
    4. Add your test cases to the 'test_cases' and 'non_consistent_test_cases' dictionaries.
    5. Run the tests by typing "pytest -v" in your IDE terminal.
"""

import pytest
from che_unit_converter import cheuc

tolerance = 1e-3
test_cases = [
    {"value": 1e-2, "from_unit": "m/s", "to_unit": "ft/min", "expected": 1.968503937},
    {"value": 1e2, "from_unit": "mm", "to_unit": "in", "expected": 3.937007874},
    {"value": 1, "from_unit": "kg/m3", "to_unit": "g/L", "expected": 1},
    {"value": 1e2, "from_unit": "kg/m3", "to_unit": "lb/ft3", "expected": 6.242796058},
    {"value": 1e-2, "from_unit": "kg/m2.s", "to_unit": "lb/ft2.hr", "expected": 7.373381094},
    {"value": 1e-4, "from_unit": "m3/s", "to_unit": "L/min", "expected": 6},
    {"value": 1e-3, "from_unit": "m3/s", "to_unit": "ft3/hr", "expected": 1.271328002e2},
    {"value": 1, "from_unit": "mol/s", "to_unit": "kmol/hr", "expected": 3.6},
    {"value": 1, "from_unit": "mol/s", "to_unit": "lbmol/hr", "expected": 7.936633914824},
    {"value": 1, "from_unit": "mol/m3.s", "to_unit": "kmol/m3.hr", "expected": 3.6},
    {"value": 1e2, "from_unit": "mol/m3.s", "to_unit": "mol/L.min", "expected": 6},
    {"value": 1, "from_unit": "W/m3", "to_unit": "kJ/m3.hr", "expected": 3.6},
    {"value": 1e4, "from_unit": "W/m3", "to_unit": "kcal/m3.s", "expected": 2.390057361},
    {"value": 1e1, "from_unit": "W/m2.K", "to_unit": "kcal/m2.hr.degC", "expected": 8.60437847},
    {"value": 1e1, "from_unit": "W/m2.K", "to_unit": "Btu/ft2.hr.degF", "expected": 1.761101819},
    {"value": 1e-4, "from_unit": "m2/s", "to_unit": "cm2/s", "expected": 1},
    {"value": 1e-4, "from_unit": "m2/s", "to_unit": "ft2/hr", "expected": 3.8750077512},
    {"value": 1e4, "from_unit": "cP", "to_unit": "lb/ft.s", "expected": 6.719689751},
    {"value": 1e4, "from_unit": "J/kg.K", "to_unit": "cal/g.degC", "expected": 2.39010513},
    {"value": 1e4, "from_unit": "J/kg.K", "to_unit": "Btu/lb.degF", "expected": 2.388458966},
    {"value": 1e5, "from_unit": "Pa/m", "to_unit": "psi/ft", "expected": 4.420750245},
    {"value": 1e-7, "from_unit": "m3/mol.s", "to_unit": "ft3/lbmol.hr", "expected": 5.766646815},
]

non_consistent_test_cases = [
    {"value": 1.0, "from_unit": "J", "to_unit": "W"},
    {"value": 10.0, "from_unit": "kg", "to_unit": "Pa"},
    {"value": 0.5, "from_unit": "mol/s", "to_unit": "kg/hr"},
    {"value": 3.0, "from_unit": "W/m2.K", "to_unit": "cal/m.s.degF"},
]

@pytest.mark.parametrize("case", test_cases)
def test_unit_conversions(case):
    """
    Automatically runs each test case from the list above.
    """
    result = cheuc(case["value"], case["from_unit"], case["to_unit"])
    assert abs(result - case["expected"]) <= tolerance, (
        f"\nConversion failed:\n"
        f"  {case['value']} {case['from_unit']} -> {case['to_unit']}\n"
        f"  Expected: {case['expected']}, Got: {result}"
    )


@pytest.mark.parametrize("non_consistent_case", non_consistent_test_cases )
def test_inconsistent_dimensions(non_consistent_case):
    """
    Ensures that conversions between physically inconsistent dimensions
    raise a ValueError (as your convert() implementation does).
    """
    with pytest.raises(ValueError):
        cheuc(non_consistent_case["value"], non_consistent_case["from_unit"], non_consistent_case["to_unit"])
