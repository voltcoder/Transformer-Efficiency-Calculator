# Transformer Efficiency Calculator (With Load)

def calculate_efficiency(output_power, copper_loss, iron_loss):
    total_input = output_power + copper_loss + iron_loss
    efficiency = (output_power / total_input) * 100
    return efficiency

print("---- Transformer Efficiency Calculator ----")

rated_power = float(input("Enter Rated Power (kW): "))
load_percent = float(input("Enter Load Percentage (%): "))
copper_loss_full = float(input("Enter Full Load Copper Loss (kW): "))
iron_loss = float(input("Enter Iron Loss (kW): "))

# Copper loss varies with square of load
copper_loss = copper_loss_full * (load_percent/100)**2
output_power = rated_power * (load_percent/100)

eff = calculate_efficiency(output_power, copper_loss, iron_loss)

print(f"\nEfficiency at {load_percent}% load = {eff:.2f}%")
