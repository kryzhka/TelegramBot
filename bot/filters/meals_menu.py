from aiogram.filters.callback_data import CallbackData
from aiogram.filters.state import State,StatesGroup

class AddMealToFavorites(CallbackData,prefix='add_meal_to_favorites'):
    meal_id: int = None

class MealInfo(CallbackData,prefix='get_info_about_meal'):
    meal_id: int = None