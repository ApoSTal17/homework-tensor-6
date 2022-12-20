
# Задание 2

with open("input.txt", "r") as file_in, open("output.txt", "w") as file_out:
    numbers = file_in.readline().split()
    if numbers[0].isdigit() & numbers[1].isdigit() & numbers[2].isdigit():
        c, h, o = int(numbers[0]), int(numbers[1]), int(numbers[2])
        print(f'Считанные из файла числа: c = {c}, h = {h}, o = {o}')
        c_count = c // 2
        h_count = h // 6
        o_count = o // 1
        mol_count = min(c_count, h_count, o_count)
        print(f'Итого возможных молекул: {mol_count}')
        file_out.write(str(mol_count))
    else:
        print('Неверный формат чисел.')