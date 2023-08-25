"""Output_

sunshine
princeZone
tesla
rapido
levis
"""

#using the continue statement

projects = ["sunshine", "princeZone", "tesla", "amul", "rapido", "levis"]

for project in projects:
    if project == "amul":
        continue
    print(project)