from prettytable import PrettyTable, MARKDOWN

table = PrettyTable()

table.set_style(MARKDOWN)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
