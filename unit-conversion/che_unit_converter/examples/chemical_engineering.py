"""
Chemical Engineering Specific Examples

This file demonstrates unit conversions specific to chemical engineering processes.
Run this file to see advanced usage examples!
"""

from che_unit_converter import cheuc

print("=" * 70)
print("CHEMICAL ENGINEERING UNIT CONVERTER - ADVANCED EXAMPLES")
print("=" * 70)

print("\n1. GENERAL GAS CONSTANT CONVERSIONS")
print("-" * 40)
R_si = 8.314  # J/(mol·K)
print(f"  Universal gas constant R = {R_si} J/(mol·K)")

print("\n  R in different units:")
print(f"  {R_si} J/(mol·K) → cal/(mol·K): {cheuc(R_si, 'J/(mol.K)', 'cal/(mol.K)'):.4f} cal/(mol·K)")
print("    Explanation: Gas constant in calories per mole-Kelvin")

print(f"  {R_si} J/(mol·K) → Btu/(lbmol·°R): {cheuc(R_si, 'J/(mol.K)', 'Btu/(lbmol.degR)'):.6f} Btu/(lbmol·°R)")
print("    Explanation: Gas constant in BTU per pound-mole-Rankine")

print(f"  {R_si} J/(mol·K) → psia·ft³/(lbmol·°R): {cheuc(R_si, 'J/(mol.K)', 'psia.ft3/(lbmol.degR)'):.4f} psia·ft³/(lbmol·°R)")
print("    Explanation: Gas constant in psia-cubic feet per pound-mole-Rankine")

print(f"  {R_si} J/(mol·K) → atm·L/(mol·K): {cheuc(R_si, 'J/(mol.K)', 'atm.L/(mol.K)'):.6f} atm·L/(mol·K)")
print("    Explanation: Common unit for ideal gas law calculations")

print("\n2. HEAT TRANSFER AND THERMAL PROPERTIES")
print("-" * 40)

print("\n2.1 Heat Transfer Coefficient:")
h_si = 1000  # W/(m²·K)
print(f"  {h_si} W/(m²·K) → Btu/(h·ft²·°F): {cheuc(h_si, 'W/(m2.K)', 'Btu/(h.ft2.degF)'):.2f} Btu/(h·ft²·°F)")
print("    Explanation: Common conversion for heat exchanger calculations")

print("\n2.2 Thermal Conductivity:")
k_si = 50  # W/(m·K)
print(f"  {k_si} W/(m·K) → Btu/(h·ft·°F): {cheuc(k_si, 'W/(m.K)', 'Btu/(h.ft.degF)'):.2f} Btu/(h·ft·°F)")
print("    Explanation: Thermal conductivity of materials")

print("\n2.3 Heat Flux:")
q_si = 10000  # W/m²
print(f"  {q_si} W/m² → Btu/(h·ft²): {cheuc(q_si, 'W/m2', 'Btu/(h.ft2)'):.2f} Btu/(h·ft²)")
print("    Explanation: Heat flux in boiler and furnace calculations")

print("\n3. MOLAR QUANTITIES AND CONCENTRATIONS")
print("-" * 40)

print("\n3.1 Molar Flow Rates:")
print(f"  1 kmol/s → lbmol/h: {cheuc(1, 'kmol/s', 'lbmol/h'):.2f} lbmol/h")
print("    Explanation: Large-scale chemical process flow rates")
print(f"  100 gmol/s → lbmol/s: {cheuc(100, 'gmol/s', 'lbmol/s'):.4f} lbmol/s")
print("    Explanation: Gram-moles to pound-moles per second")

print("\n3.2 Concentrations:")
print(f"  1 mol/L → lbmol/ft³: {cheuc(1, 'mol/L', 'lbmol/ft3'):.6f} lbmol/ft³")
print("    Explanation: Molar concentration in different volume units")
print(f"  0.1 gmol/m³ → lbmol/gal: {cheuc(0.1, 'gmol/m3', 'lbmol/gal'):.8f} lbmol/gal")
print("    Explanation: Dilute solution concentrations")

print("\n4. FLUID PROPERTIES")
print("-" * 40)

print("\n4.1 Viscosity:")
print(f"  1 cP → Pa·s: {cheuc(1, 'cP', 'Pa.s'):.6f} Pa·s")
print("    Explanation: Centipoise to Pascal-seconds (SI units)")
print(f"  100 cP → lb/(ft·h): {cheuc(100, 'cP', 'lb/(ft.h)'):.1f} lb/(ft·h)")
print("    Explanation: Viscosity in engineering units")

print("\n4.2 Specific Heat:")
print(f"  1 J/(g·K) → Btu/(lb·°F): {cheuc(1, 'J/(g.K)', 'Btu/(lb.degF)'):.6f} Btu/(lb·°F)")
print("    Explanation: Specific heat capacity conversion")

print("\n5. DIMENSIONAL ANALYSIS PROTECTION")
print("-" * 40)
print("  The converter prevents physically meaningless conversions:")

try:
    result = cheuc(1, 'J/mol', 'Btu/ft')
    print("  ERROR: This should have failed!")
except ValueError as e:
    print("  ✓ Correctly rejected: J/mol → Btu/ft")
    print(f"    Reason: {e}")

try:
    result = cheuc(1, 'm', 'kg')
    print("  ERROR: This should have failed!")
except ValueError as e:
    print("  ✓ Correctly rejected: m → kg") 
    print(f"    Reason: {e}")

print("\n" + "=" * 70)
print("END OF CHEMICAL ENGINEERING EXAMPLES")
print("=" * 70)