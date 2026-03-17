def calculate_efficiency(output_power, copper_loss, iron_loss):
    total_input = output_power + copper_loss + iron_loss
    efficiency = (output_power / total_input) * 100
    return efficiency


print("---- Transformer Efficiency Calculator ----")

try:
    rated_power = float(input("Enter Rated Power (kW): "))
    load_percent = float(input("Enter Load Percentage (%): "))
    copper_loss_full = float(input("Enter Full Load Copper Loss (kW): "))
    iron_loss = float(input("Enter Iron Loss (kW): "))

    if load_percent < 0 or load_percent > 150:
        print("Load percentage should be between 0 and 150.")
    else:
        # Calculations
        copper_loss = copper_loss_full * (load_percent / 100) ** 2
        output_power = rated_power * (load_percent / 100)

        eff = calculate_efficiency(output_power, copper_loss, iron_loss)

       # Check for maximum efficiency condition
         if abs(copper_loss - iron_loss) < 0.01:
            print("\nTransformer is operating at maximum efficiency condition.")

        # Output results
        print(f"\nOutput Power = {output_power:.2f} kW")
        print(f"Copper Loss = {copper_loss:.2f} kW")
        print(f"Total Loss = {copper_loss + iron_loss:.2f} kW")
        print(f"Efficiency at {load_percent}% load = {eff:.2f}%")

except ValueError:
    print("Invalid input. Please enter numeric values.")
