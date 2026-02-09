#Task 1.1: Variable containing inital strings
sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

#Task 1.2: Analyzing Samples with iterations
for sample in sample_bay:
    print(f"Transmitting Data for: {sample}")


#Task 1.3: Creating a new list 
new_findings = []

i = 3
while i:
    i = i - 1
    rock_type = str(input("Enter a rock type: "))
    new_findings.append(f"{rock_type}")

for findings in new_findings:
    print(f"New rock type findings: {findings}")