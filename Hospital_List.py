# Hospital Ward Management List - Ordered collections for patient beds
# Ward 4A Patient Beds (Ordered by proximity to nurses' station)
ward_4a = ["Bed1: Robert", "Bed2: Fatima", "Bed3: James"]

# New admission
ward_4a.append("Bed4: Aisha")  # to append is to add
ward_4a.append("Bed5: Jojo")
print("Ward 4A:", ward_4a)  


# Discharge patient
discharged = []  # a list to store discharged patients

discharged.append(ward_4a.pop(1))  # removes "Fatima"
discharged.append(ward_4a.pop(2))  # now removes "Aisha"

print(f"Discharged: {discharged} → Remaining: {ward_4a}")

 