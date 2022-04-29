row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? First digit is for horizontal, second digit is for vertical.")
#első szám --> vertikális
#második szám --y horizontális
horizontal_index = int(position[0]) -1
vertical_index = int(position[1]) -1

map[horizontal_index][vertical_index] = "X"
#if vertical_index and horizontal_index == 0 :
#   map[[0][0]] = "X"

print(f"{row1}\n{row2}\n{row3}")