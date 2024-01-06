from aiogram.filters.callback_data import CallbackData
from aiogram.filters.state import State,StatesGroup

class GetMealInfo(CallbackData,prefix='info about meal'):
    meal_id: int = None

class DeleteFromFavorites(CallbackData,prefix='delete meal from favorites'):
    meal_id: int = None

class AccountActionWithAllMeal(CallbackData,prefix='action_with_all_meal'):
    action: str=None