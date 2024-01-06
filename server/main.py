import os
import psycopg2
from flask import Flask
from flask import request
import psycopg2.extras
from psycopg2 import Error


HOST=os.getenv('HOST')
PORT=os.getenv('PORT')
app = Flask(__name__)

conn = psycopg2.connect(
    database = os.getenv('DB_NAME'),
    user     = os.getenv('DB_USER'),
    host     = os.getenv('DB_HOST'),
    password = os.getenv('DB_PASS'),
    port     = os.getenv('DB_PORT')
    )

@app.route('/')
def test():
    return 'Hello noname'

@app.route('/users/add_user/<user_id>/<user_name>',methods=['GET','POST'])# добавление нового пользователя в базу данных
def add_user(user_id=1,user_name='noname'):
    try:
        if request.method=='POST':
            user_id=request.args.get('user_id')
            user_name=request.args.get('user_name')
        if request.method=='GET':
        
            cur=conn.cursor()
            cur.execute(
                f'''
                insert into users (user_id,username)
                values
                    ({user_id},'{user_name}')
                ON CONFLICT (user_id) DO NOTHING;
                '''
            )
            print("USER IS ADD",flush=True)

            conn.commit()
            cur.close()
            return [True]
    except(Exception, Error) as error:
        print('ERR: USER IS NOT ADD\n',error,flush=True)
        return [False]

@app.route('/users/<user_id>/add_meals/<meal_id>',methods = ['GET', 'POST'])#Добавление блюда в личный кабинет
def add_meals_to_user(user_id,meal_id):
    try:
        if request.method=='POST':
            user_id=request.args.get('user_id')
            meal_id=request.args.get('meal_id')
        if request.method=='GET':
            cur=conn.cursor()
            cur.execute(
                f'''
                insert into journal (log_id,user_id,meals_id)
                values
                    (nextval('seq_journal'),{user_id},'{meal_id}')
                '''
                )
            conn.commit()
            cur.close()
            print("MEAL ADDED",flush=True)
            return [True]
    except(Exception, Error) as error:
            print("ERR: meal not added\n",error,flush=True)
            return [False]

@app.route('/users/<user_id>/remove_meals/<meals_id>',methods = ['GET', 'POST'])#Удаление одного или всех блюд из личного кабинета пользователя
def remove_meal_from_account(user_id,meals_id):
    try:
        if request.method=='POST':
            user_id=request.args.get('user_id')
            meals_id=request.args.get('meals_id')
        if request.method=='GET':
            cur=conn.cursor()
            if(meals_id=='all'):
                cur.execute(
                f"delete                                    \
                from journal                                \
                where user_id = {user_id};"
                )
            
            else:
                cur.execute(
                f'''
                delete from journal
                where 
                user_id = {user_id}
                and
                meals_id={meals_id}
                '''
                )
            
            conn.commit()
            cur.close()
            print("MEALS REMOVED",flush=True)
            return [True]
    except(Exception, Error) as error:
        print("ERR: meals are not removed\n",error,flush=True)
        return [False]


@app.route('/users/<user_id>',methods = ['GET', 'POST'])#Вывод id и названий всех блюд, добавленных пользователем в личный кабинет  
def get_user_info(user_id=3):
    try:
        if request.method=='POST':
            user_id=request.args.get('user_id')

        if request.method=='GET':
            cur=conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
            cur.execute(
                f"select distinct                           \
                meals_id, \
                (select name_meals from meals     \
                where meals.meals_id = journal.meals_id     \
                )                                           \
                as meal                                     \
                from journal                                \
                where user_id = {user_id}"
                )
            rows = cur.fetchall()
            conn.commit()
            cur.close()
            print('GET USER MEALS',flush=True)
            return rows
    except(Exception, Error) as error:
        print("ERR:info about user meals\n",error,flush=True)
        return [False]

@app.route('/meals_with_limit/<limit>',methods = ['GET', 'POST'])#поиск с верхней границей по количеству калорий
def meals_with_limit(limit):
    try:
        if request.method=='POST':
            limit=request.args.get('limit')
        if request.method=='GET':
            cur=conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)

            cur.execute(
                    f'''
                    select meals_id,name_meals
                    from meals
                    where number_of_calories <= {limit};
                    '''
                    )

            rows=cur.fetchall()
            conn.commit()
            cur.close()
            print("MEALS FOUND with calories limit",flush=True)
            return rows
    except(Exception, Error) as error:
        print("ERR:search with calories limit\n",error,flush=True)
        return [False]
    

@app.route('/meals',methods = ['GET'])
def get_all_meals():# Вывод всех блюд
    try:
        if request.method=='GET':
            cur=conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
            cur.execute(
            '''
            select meals_id,name_meals from meals
            '''
            )

            rows=cur.fetchall()
            conn.commit()
            cur.close()
            print("GET ALL MEALS",flush=True)
            return rows
    except(Exception, Error) as error:
        print("ERR: meals are not get\n",error,flush=True)
        return [False]

@app.route('/meals/<meal_id>',methods = ['GET','POST'])
def select_meal(meal_id):#Выводит подробную информацию о выбранном блюде
    try:
        if request.method=='POST':
            meal_id=request.args.get('meal_id')
        if request.method=='GET':

            cur=conn.cursor()
            cur.execute(
            f'''
            select * from meals
                where meals_id ={meal_id};
            '''
            )
            meal_info=cur.fetchall()
            result={}
            for i in range(len(cur.description)):
                result[str(cur.description[i].name)]=meal_info[0][i]
            
            conn.commit()
            cur.close()
            print('GET MEAL INFO',flush=True)
            return result
    except(Exception, Error) as error:
        print('ERR: meal info are not get\n',error,flush=True)
        return [False]

@app.route('/meals/<meal_id>/quantity',methods = ['GET','POST'])
def get_quantity_of_products(meal_id):#return product_name, quantity
    try:
        if request.method=='POST':
            meal_id=request.args.get('meal_id')
        if request.method=='GET':
            cur=conn.cursor()
        cur.execute(
            f'''
            select 
            (
                select name from product
                    where product.product_id = product_meals.product_id
            )
            as product,
            quantity 
            from product_meals
                where meals_id ={meal_id};
            '''
            )
        quantity = cur.fetchall()
        conn.commit()
        cur.close()

        print('GET MEAL QUANTITY INFO',flush=True)           
        return quantity
    except(Exception, Error) as error:
        print('ERR: meal quantity are not get\n',error,flush=True)
        return [False]


@app.route('/products',methods = ['GET'])#Вывод всех возможных продуктов
def get_all_products():#return product_id,product_name
    try:
        if request.method=='GET':
            cur=conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
            cur.execute(
            f'''
            select product_id, name from product
            '''
            )
            rows=cur.fetchall()
            conn.commit()
            cur.close()
            print('GET ALL PRODUCTS',flush=True)
            return rows
    except(Exception, Error) as error:
        print("ERR: list of products are not get\n",error,flush=True)
        return [False]

@app.route('/products/<product_id>',methods = ['GET', 'POST'])#Вывод всех возможных блюд с выбранным продуктом
def select_product(product_id): #return meal_id,meal_nae
    try:
        if request.method=='POST':
            product_id=request.args.get('product_id')
        if request.method=='GET':
            cur=conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)

            cur.execute(
            f'''
            select meals_id, 
            (
                select name_meals 
                from meals
                where meals.meals_id = product_meals.meals_id
            )
            as meal_name
            from product_meals
                where product_id = {product_id}
            '''
            )
            rows=cur.fetchall()
            conn.commit()
            cur.close()
            print('MEALS WITH PRODUCT ARE GET',flush=True)
            return rows
    except(Exception, Error) as error:
        print('ERR: meals with product are not get\n',error,flush=True)
        return [False]


@app.route('/users/sum_of_user_PFC/<user_id>',methods = ['GET', 'POST'])#подсчет общего количества калорий, белков, жиров и углеводов всех блюд, добавленных в личный кабинет
def sum_of_user_PFC(user_id):
    try:
        if request.method=='POST':
            user_id=request.args.get('product_id')
        if request.method=='GET':
            cur=conn.cursor()

            cur.execute(
                    f'''
                    SELECT SUM(number_of_calories) as calories, 
                    SUM(number_of_squirrels) as squirrels, 
                    SUM(number_of_fats) as fats, 
                    SUM(number_of_carbohydrates) as carbohydrates
                    from users natural join journal 
                    natural join meals
                    WHERE user_id = {user_id};
                    '''
            )
            rows=cur.fetchall()
            result={}
            for i in range(len(cur.description)):
                result[str(cur.description[i].name)]=rows[0][i]
            conn.commit()
            cur.close()
            print("SUM OF USER MEALS INFO ARE GET", flush=True)
            return result
    except(Exception, Error) as error:
        print("ERR: sum of user meals info are not get\n",error,flush=True)
        return [False]



app.run(debug=True,host=HOST,port=PORT)