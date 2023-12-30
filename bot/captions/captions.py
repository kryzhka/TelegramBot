def get_meal_info(data):
    cap=(
    f"Информация о блюде:\n"
    f"Название блюда:\n"
    f"{data[0][1]}\n"
    f"Количество калорий:     {data[0][2]}\n"
    f"Количество белков:      {data[0][3]}\n"
    f"Количество жиров:       {data[0][4]}\n"
    f"Количество углеводов:   {data[0][5]}\n"
    f"Ингридиенты:\n"
    f"Продукт:        Количество:\n"
    )
    for i in range(1,len(data)):
        cap+=f"{data[i][0]}      {data[i][1]}\n"
    return cap
