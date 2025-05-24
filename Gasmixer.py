# Trying to find avg molar mass of gas mixture

# user inputs — assuming everything in SI
volume = float(input("Volume of gas (in m³)? "))
pressure = float(input("Pressure (in Pa)? "))
temperature = float(input("Temperature (in K)? "))
mass = float(input("Mass of gas (in grams)? "))

R = 8.314  # gas constant

# calculate number of moles from ideal gas law
def mole():
    x = pressure * volume 
    y = R * temperature
    z = x / y 
    print(f"Moles of gas mixture: {round(z, 2)}")
    return z

# get molar mass using total mass / moles
def mass_of_1_mole(z):
    gasx = int(input("Molar mass of CH4? "))
    gasy = int(input("Molar mass of C2H6? "))
    k = mass / z  
    return k, gasx, gasy

# figure out how much of CH4 is in the mix
def mole_frac(k, gasx, gasy):
    n = (k - gasy) / (gasx - gasy)
    print(f"Mole fraction of CH4: {round(n, 2)}")

def main():
    z = mole()
    k, gasx, gasy = mass_of_1_mole(z)
    mole_frac(k, gasx, gasy)

main()