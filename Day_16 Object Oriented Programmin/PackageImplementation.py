from prettytable import PrettyTable

table = PrettyTable()

# invoking the methods of the PrettyTable package
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
table.add_column( "Type", ["Electric", "Water", "Fire", "Grass"])

# adjusting the attributes that are associated with the Table() class and the table object
table.align = "r"
 
print(table)