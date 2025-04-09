# define the function to calculate the drug dosage
# the function takes in the weight of the patient in kg and the drug dosage in mg/kg
# check the weight of the patient and the drug dosage
def calculate_dosage(weight, strength): 
    # Check if weight is a number and convert to float
    if weight<10 or weight>100:
        return "Error: Weight must be between 10 and 100 kg"
    
    # Check strength is valid and calculate dose
    if strength == "120 mg/5 ml":
        dose_mg = weight * 15  # 15 mg/kg
        volume_ml = (dose_mg / 120) * 5
        return round(volume_ml, 2)
    elif strength == "250 mg/5 ml":
        dose_mg = weight * 15  # 15 mg/kg
        volume_ml = (dose_mg / 250) * 5
        return round(volume_ml, 2)
    else:
        return "Error: Invalid strength. Must be '120 mg/5 ml' or '250 mg/5 ml'"

# Example usage
print("=== Drug Dosage Calculator Examples ===")
print("20 kg, 120 mg/5 ml:", calculate_dosage(20, "120 mg/5 ml"))
print("35 kg, 250 mg/5 ml:", calculate_dosage(35, "250 mg/5 ml"))
print("5 kg, 120 mg/5 ml:", calculate_dosage(5, "120 mg/5 ml"))  # Error case
print("50 kg, 500 mg/5 ml:", calculate_dosage(50, "500 mg/5 ml"))  # Error case




  

    