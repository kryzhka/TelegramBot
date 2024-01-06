from aiogram.filters.callback_data import CallbackData
from aiogram.filters.state import State,StatesGroup





class MealsWithProduct(CallbackData,prefix='get_product'):
    action    : str =None
    product_id: int = None
    product_name: str=None

class MealsAction(CallbackData,prefix='action_with_meal_in_search'):
    action:  str = None
    meal_id: int = None

# class GetProductFromUser(,prefix='get_product_name_from_user'):
#     meal_name: str=None
class InputMessege(StatesGroup):
    message = State()
    data_callback= None

class InputMessegeLimit(StatesGroup):
    message = State()
    data_callback= None
    limit=None

class MealsActionCaloriesMenu(CallbackData,prefix='action_with_meal_in_calories_search'):
    action:  str = None
    meal_id: int = None
    limit: int=None

class MealsWithCalories(CallbackData,prefix='back_to_meals_with_calories'):
    limit:int=None