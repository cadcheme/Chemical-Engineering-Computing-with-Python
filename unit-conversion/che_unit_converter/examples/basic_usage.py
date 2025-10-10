"""
Basic Usage Examples for Chemical Engineering Unit Converter

This file demonstrates common unit conversions with clear explanations.
Run this file to see the converter in action!
"""

from che_unit_converter import cheuc

print("=" * 70)
print("CHEMICAL ENGINEERING UNIT CONVERTER - BASIC EXAMPLES")
print("=" * 70)

print("\n1. LENGTH CONVERSIONS")
print("-" * 40)
print("  10 km → m: {cheuc(10, 'km', 'm'):.1f} m")
print("    Explanation: 10 kilometers = 10,000 meters")
print("  100 cm → m: {cheuc(100, 'cm', 'm'):.1f} m") 
print("    Explanation: 100 centimeters = 1 meter")
print(f"  1 ft → m: {cheuc(1, 'ft', 'm'):.6f} m")
print("    Explanation: 1 foot = 0.3048 meters")

print("\n2. PRESSURE CONVERSIONS")
print("-" * 40)
print(f"  1 atm → Pa: {cheuc(1, 'atm', 'Pa'):.0f} Pa")
print("    Explanation: Standard atmosphere to Pascals")
print(f"  1 bar → kPa: {cheuc(1, 'bar', 'kPa'):.1f} kPa")
print("    Explanation: 1 bar = 100 kPa")
print(f"  14.7 psi → atm: {cheuc(14.7, 'psi', 'atm'):.3f} atm")
print("    Explanation: Common pressure conversion")

print("\n3. TEMPERATURE CONVERSIONS")
print("-" * 40)
print(f"  100 °C → °F: {cheuc(100, 'degC', 'degF'):.1f} °F")
print("    Explanation: Water boiling point (100°C = 212°F)")
print(f"  32 °F → °C: {cheuc(32, 'degF', 'degC'):.1f} °C")
print("    Explanation: Water freezing point (32°F = 0°C)")
print(f"  300 K → °C: {cheuc(300, 'K', 'degC'):.1f} °C")
print("    Explanation: Room temperature approximation")

print("\n4. ENERGY CONVERSIONS")
print("-" * 40)
print(f"  1 Btu → J: {cheuc(1, 'Btu', 'J'):.1f} J")
print("    Explanation: British thermal unit to Joules")
print(f"  1 cal → J: {cheuc(1, 'cal', 'J'):.3f} J")
print("    Explanation: Calorie to Joules")
print(f"  1 kW·h → MJ: {cheuc(1, 'kW-h', 'MJ'):.3f} MJ")
print("    Explanation: Kilowatt-hour to Megajoules")

print("\n" + "=" * 70)
print("END OF BASIC EXAMPLES")
print("=" * 70)