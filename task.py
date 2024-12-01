from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Names", ["Mudasir", "Sawera", "Gulshen,"])
table.add_column("Type", ["Student", "Student", "Housewife"])
table.align = "l"
print(table)
