def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"first_name": "Santiago", "last_name": "Ahumada"}

    super_list = [
        {"first_name": "Santiago", "last_name": "Ahumada"},
        {"first_name": "Natalia", "last_name": "Angel"},
        {"first_name": "Miguel", "last_name": "Cortes"},
        {"first_name": "Camilo", "last_name": "Lopez"},
        {"first_name": "Laura", "last_name": "Herrera"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "float_nums": [1.1, 4.5, 6.43, 3.14]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    print("\n")
    for dict in super_list:
        current_name = "first_name"
        current_lastname = "last_name"
        print(current_name, "-", dict[current_name])
        print(current_lastname, "-", dict[current_lastname])
        print("\n")
if __name__ == '__main__':
    run()