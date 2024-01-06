def get_meal_info(info,quantity):
    cap=(
    f"Информация о блюде:\n"
    f"Название блюда:\n"
    f"{info['name_meals']}\n"
    f"Количество калорий:     {info['number_of_calories']}\n"
    f"Количество белков:      {info['number_of_squirrels']}\n"
    f"Количество жиров:       {info['number_of_fats']}\n"
    f"Количество углеводов:   {info['number_of_carbohydrates']}\n"
    f"Ингридиенты:\n"
    f"Продукт:        Количество:\n"
    )
    for i in quantity:
        cap+=f"{i[0]}      {i[1]}\n"
    return cap
