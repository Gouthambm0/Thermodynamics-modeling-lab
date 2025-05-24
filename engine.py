#Toy Volume ramp 

State0 = {"p":1,"t":300,"v": 50}
State1 = {"p":1,"t":300,"v": 60}
State2 = {"p":1,"t":300,"v": 70}

k = 0.082    #in L,atm,mol,K units
# inside your derivative function

dT_dt = 5
dP_dt = 3
def dv(state, k,dT_dt, dP_dt):
    dT_dt = ...      # comes from first-law bookkeeping
    dP_dt = ...      # maybe controlled, maybe computed
    V      = state["v"]
    P      = state["p"]
    T      = state["t"]
    dV_dt = (k / P) * dT_dt - (V / P) * dP_dt
    return dV_dt

def main():
    dv()
    print (f"dV_dt")


main() 