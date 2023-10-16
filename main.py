def help_function_x(str_0, str_1, str_2, str_3, list_1):
    filling_field_x(str_0, str_1, str_2, str_3, list_1)


def filling_field_x(str_0, str_1, str_2, str_3, list_1):
    print(str_0, "\n", str_1, "\n", str_2, "\n", str_3)
    position = input(f"Введите индекс поля куда вы хотите поставить 'X' {list_1}:")

    if position in array:
        array.remove(position)
        if position == "00":
            change_string_1 = str_1[:2] + "X" + str_1[3:]
            result = check_result(str_0, change_string_1, str_2, str_3)
            if result == "Поздравляю, крестики победили":
                return result
            return help_function_o(str_0, change_string_1, str_2, str_3, list_1)

        elif position == "01":
            change_string_1 = str_1[:4] + "X" + str_1[5:]
            result = check_result(str_0, change_string_1, str_2, str_3)
            if result == "Поздравляю, крестики победили":
                return result
            return help_function_o(str_0, change_string_1, str_2, str_3, list_1)

        elif position == "02":
            change_string_1 = str_1[:6] + "X"
            result = check_result(str_0, change_string_1, str_2, str_3)
            if result == "Поздравляю, крестики победили":
                return result
            return help_function_o(str_0, change_string_1, str_2, str_3, list_1)

        elif position == "10":
            change_string_2 = str_2[:2] + "X" + str_2[3:]
            result = check_result(str_0, str_1, change_string_2, str_3)
            if result == "Поздравляю, крестики победили":
                return result
            return help_function_o(str_0, str_1, change_string_2, str_3, list_1)

        elif position == "11":
            change_string_2 = str_2[:4] + "X" + str_2[5:]
            result = check_result(str_0, str_1, change_string_2, str_3)
            if result == "Поздравляю, крестики победили":
                return result
            return help_function_o(str_0, str_1, change_string_2, str_3, list_1)

        elif position == "12":
            change_string_2 = str_2[:6] + "X"
            result = check_result(str_0, str_1, change_string_2, str_3)
            if result == "Поздравляю, крестики победили":
                return result
            return help_function_o(str_0, str_1, change_string_2, str_3, list_1)

        elif position == "20":
            change_string_3 = str_3[:2] + "X" + str_3[3:]
            result = check_result(str_0, str_1, str_2, change_string_3)
            if result == "Поздравляю, крестики победили":
                return result
            return help_function_o(str_0, str_1, str_2, change_string_3, list_1)

        elif position == "21":
            change_string_3 = str_3[:4] + "X" + str_3[5:]
            result = check_result(str_0, str_1, str_2, change_string_3)
            if result == "Поздравляю, крестики победили":
                return result
            return help_function_o(str_0, str_1, str_2, change_string_3, list_1)

        elif position == "22":
            change_string_3 = str_3[:6] + "X"
            result = check_result(str_0, str_1, str_2, change_string_3)
            if result == "Поздравляю, крестики победили":
                return result
            return help_function_o(str_0, str_1, str_2, change_string_3, list_1)
    else:
        print("Такой позиции нет на поле, попробуйте еще раз")
        filling_field_x(str_0, str_1, str_2, str_3, list_1)


def help_function_o(str_0, str_1, str_2, str_3, list_1):
    filling_field_o(str_0, str_1, str_2, str_3, list_1)


def filling_field_o(str_0, str_1, str_2, str_3, list_1):
    print(str_0, "\n", str_1, "\n", str_2, "\n", str_3)
    position = input(f"Введите индекс поля куда вы хотите поставить 'O' {list_1}:")

    if position in array:
        array.remove(position)
        if position == "00":
            change_string_1 = str_1[:2] + "O" + str_1[3:]
            result = check_result(str_0, change_string_1, str_2, str_3)
            if result == "Поздравляю, нолики победили":
                return result
            return help_function_x(str_0, change_string_1, str_2, str_3, list_1)

        elif position == "01":
            change_string_1 = str_1[:4] + "O" + str_1[5:]
            result = check_result(str_0, change_string_1, str_2, str_3)
            if result == "Поздравляю, нолики победили":
                return result
            return help_function_x(str_0, change_string_1, str_2, str_3, list_1)

        elif position == "02":
            change_string_1 = str_1[:6] + "O"
            result = check_result(str_0, change_string_1, str_2, str_3)
            if result == "Поздравляю, нолики победили":
                return result
            return help_function_x(str_0, change_string_1, str_2, str_3, list_1)

        elif position == "10":
            change_string_2 = str_2[:2] + "O" + str_2[3:]
            result = check_result(str_0, str_1, change_string_2, str_3)
            if result == "Поздравляю, нолики победили":
                return result
            return help_function_x(str_0, str_1, change_string_2, str_3, list_1)

        elif position == "11":
            change_string_2 = str_2[:4] + "O" + str_2[5:]
            result = check_result(str_0, str_1, change_string_2, str_3)
            if result == "Поздравляю, нолики победили":
                return result
            return help_function_x(str_0, str_1, change_string_2, str_3, list_1)

        elif position == "12":
            change_string_2 = str_2[:6] + "O"
            result = check_result(str_0, str_1, change_string_2, str_3)
            if result == "Поздравляю, нолики победили":
                return result
            return help_function_x(str_0, str_1, change_string_2, str_3, list_1)

        elif position == "20":
            change_string_3 = str_3[:2] + "O" + str_3[3:]
            result = check_result(str_0, str_1, str_2, change_string_3)
            if result == "Поздравляю, нолики победили":
                return result
            return help_function_x(str_0, str_1, str_2, change_string_3, list_1)

        elif position == "21":
            change_string_3 = str_3[:4] + "O" + str_3[5:]
            result = check_result(str_0, str_1, str_2, change_string_3)
            if result == "Поздравляю, нолики победили":
                return result
            return help_function_x(str_0, str_1, str_2, change_string_3, list_1)

        elif position == "22":
            change_string_3 = str_3[:6] + "O"
            result = check_result(str_0, str_1, str_2, change_string_3)
            if result == "Поздравляю, нолики победили":
                return result
            return filling_field_x(str_0, str_1, str_2, change_string_3, list_1)

    else:
        print("Такой позиции нет на поле, попробуйте еще раз")
        filling_field_o(str_0, str_1, str_2, str_3, list_1)


def check_result(str_0, str_1, str_2, str_3):
    if (str_1[2] == "X" and str_1[4] == "X" and str_1[6] == "X") or (
            str_2[2] == "X" and str_2[4] == "X" and str_2[6] == "X") or (
            str_3[2] == "X" and str_3[4] == "X" and str_3[6] == "X") or (
            str_1[2] == "X" and str_2[4] == "X" and str_3[6] == "X") or (
            str_1[2] == "X" and str_2[2] == "X" and str_3[2] == "X") or (
            str_1[4] == "X" and str_2[4] == "X" and str_3[4] == "X") or (
            str_1[6] == "X" and str_2[6] == "X" and str_3[6] == "X") or (
            str_1[6] == "X" and str_2[4] == "X" and str_3[2] == "X"):
        print(str_0 + "\n" + str_1 + "\n" + str_2 + "\n" + str_3, "\n")
        result = "Поздравляю, крестики победили"
        return result
    elif (str_1[2] == "O" and str_1[4] == "O" and str_1[6] == "O") or (
            str_2[2] == "O" and str_2[4] == "O" and str_2[6] == "O") or (
            str_3[2] == "O" and str_3[4] == "O" and str_3[6] == "O") or (
            str_1[2] == "O" and str_2[4] == "O" and str_3[6] == "O") or (
            str_1[2] == "O" and str_2[2] == "O" and str_3[2] == "O") or (
            str_1[4] == "O" and str_2[4] == "O" and str_3[4] == "O") or (
            str_1[6] == "O" and str_2[6] == "O" and str_3[6] == "O") or (
            str_1[6] == "O" and str_2[4] == "O" and str_3[2] == "O"):
        print(str_0 + "\n" + str_1 + "\n" + str_2 + "\n" + str_3, "\n")
        result = "Поздравляю, нолики победили"
        return result


string_0 = "   0 1 2"
string_1 = "0 - - -"
string_2 = "1 - - -"
string_3 = "2 - - -"
array = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]

figura = input('Выберите чем хотите играть: "X" или "O" ')
while len(array) > 0:
    if figura.lower() == "x":
        filling_field_x(string_0, string_1, string_2, string_3, array)
        print("Поздравляю, крестики победили")
        break
    elif figura.lower() == "o":
        filling_field_o(string_0, string_1, string_2, string_3, array)
        print("Поздравляю, нолики победили")
        break
    else:
        print(
            "Произошла ошибка, попробуйте выбрать букву 'O', "
            "если вы хотели играть ноликами! "
        )
        continue
