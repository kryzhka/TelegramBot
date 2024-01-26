from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.filters.state import State,StatesGroup

#общие фильтры

class MainMenu(CallbackData,prefix='main menu'): #Переход в главное меню
    None

class GetMealInfo(CallbackData,prefix='get info about meal'): #Вывод подробной информации о блюде
    meal_id:int =None
    product_id:int=0
    limit:int=0
    menu:str=None
    name:str=' '

class AddMealToFavorites(CallbackData,prefix='add meal to favorites'):#Добавляет блюдо в избранное
    meal_id: int = None
    product_id:int=0
    limit:int=0
    menu:str=None
    name:str=' '

class MealsWithProduct(CallbackData,prefix='get products with select meal'): #Вывод блюд с выбранным ингридиентом
    list_of_product_ids: list = None
    product_name: str=' '
    menu:str=None


#Главное меню

class Favorites(CallbackData,prefix='favorites menu'):#Переход в избранное
    None
       
class Catalog(CallbackData,prefix='catalog'):#Переход в каталог
    None

class Search(CallbackData,prefix='search'):#Переход в меню поиска
    None


#Избранное
        
class DeleteAllFromFavorites(CallbackData,prefix='delete all meal from favorites'):#удаление всех блюд из избранных
    None

class DeleteFromFavorites(CallbackData,prefix='delete select meal from favorites'):#удаление выбранного блюда из избранных
    meal_id: int = None

class ModifyQuantity(CallbackData,prefix='modify quantity'):#Изменение количества ингридиентов
    None


#Каталог
class MealCatalog(CallbackData,prefix='meal catalog'):#Выводит все доступные блюда
    None

class ProductCatalog(CallbackData,prefix='product catalog'):
    None

class CatalogMealsWithProduct(CallbackData,prefix='get meals with selected product in catalog'):
    product_id:int=None

#Меню поиска
class ProductSearch(CallbackData,prefix='product search'):#Поиск по ингридиенту
    None

class CaloriesSearch(CallbackData,prefix='calories search'):#Поиск по калориям
    None

class MealNameSearch(CallbackData,prefix='search meal name'):#Поиск по названию блюда
    None


#Поиск по ингридиету

class InputMessegeProductName(StatesGroup):#Обработка сообщения с названием ингридиента
    message = State()
    data_callback= None


class ProductNameSearch(CallbackData,prefix='search product name'):
    None
#Поиск по калориям

class InputMessegeLimit(StatesGroup):#Обработка сообщения с верхним пределом калорий
    message = State()
    data_callback= None
    limit=None

class MealsWithCalories(CallbackData,prefix='back_to_meals_with_calories'):
    limit:int=None
#Поиск по названию блюда

class InputMessegeMealName(StatesGroup):
    message=State()
    data_callback=None
    name=None

class FoundedMeals(CallbackData,prefix='meals that find by input name'):
    name:str=None