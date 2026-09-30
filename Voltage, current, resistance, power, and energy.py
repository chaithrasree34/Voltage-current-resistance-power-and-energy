# Voltage-current-resistance-power-and-energy
# Electrical Calculations

print("Electrical Calculator")
print("1. Voltage")
print("2. Current")
print("3. Resistance")
print("4. Power")
print("5. Energy")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    I = float(input("Enter current (A): "))
    R = float(input("Enter resistance (Ohm): "))
    V = I * R
    print("Voltage =", V, "V")

elif choice == 2:
    V = float(input("Enter voltage (V): "))
    R = float(input("Enter resistance (Ohm): "))
    I = V / R
    print("Current =", I, "A")

elif choice == 3:
    V = float(input("Enter voltage (V): "))
    I = float(input("Enter current (A): "))
    R = V / I
    print("Resistance =", R, "Ohm")

elif choice == 4:
    V = float(input("Enter voltage (V): "))
    I = float(input("Enter current (A): "))
    P = V * I
    print("Power =", P, "W")

elif choice == 5:
    P = float(input("Enter power (W): "))
    t = float(input("Enter time (hours): "))
    E = P * t
    print("Energy =", E, "Wh")

else:
    print("Invalid choice")
