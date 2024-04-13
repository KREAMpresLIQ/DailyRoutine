from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["City name", "Area", "Population", "Zip Code"]
table.add_row(["Backa Topola", "Backa Topola", 11000, 24300])
table.add_row(["Tornjos", "Senta", 1100, 24500])
table.add_row(["Temerin", "Novi Sad", 31000, 24400])
table.add_row(["Becej", "Novi Sad", 18000, 24900])
table.add_row(["Bajsa", "Backa Topola", 2000, 24600])

table.add_column("Companies", ["Sat-Trakt", "Gebi", "Beba Kids", "John Deere", "Krivaj"])
table.add_column("Employes", [1295, 5905, 112, 1357, 2058])
table.add_column("Payment", [1158259, 1857594, 120900, 205556, 4336374])
table.add_column("Time", [600.5, 1146.4, 1714.7, 619.5, 1214.8])

print(table)

# table.field_names = ["City name", "Area", "Population", "Zip Code"]
# table.add_rows(
#     [
#         ["Backa Topola", "Backa Topola", 11000, 24300],
#         ["Tornjos", "Senta", 1100, 24500],
#         ["Temerin", "Novi Sad", 31000, 24400],
#         ["Becej", "Novi Sad", 18000, 24900],
#         ["Bajsa", "Backa Topola", 2000, 24600]
#     ]
# )
#
# print(table)

table2 = PrettyTable()

table2.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table2.add_column("Type", ["Electric", "Water", "Fire"])

table2.align = "l"

print(table2.align)
print(table2)
