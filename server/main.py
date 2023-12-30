import os
import psycopg2
from flask import Flask
from flask import request

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

@app.route('/users/add_user/<user_id>/<user_name>',methods=['GET','POST'])
def add_user(user_id=1,user_name='noname'):
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
        
        return "USER IS ADD"
    else:
        print('error')
        return -1
    
@app.route('/users/<user_id>',methods = ['GET', 'POST'])
def get_user_info(user_id=3):
    if request.method=='POST':
        user_id=request.args.get('user_id')

    if request.method=='GET':
        cur=conn.cursor()
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
        print(rows,flush=True)
        return rows
    else:
        print("error")


@app.route('/meals/<meal_id>',methods = ['GET'])
def get_all_meals(meal_id='all'):
    if request.method=='POST':
        meal_id=request.args.get('meal_id')
    if request.method=='GET':
        cur=conn.cursor()
        rows1=[]
        if meal_id=='all':
            cur.execute(
                '''
                select meals_id,name_meals from meals
                '''
            )
        else:
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
            rows1 = cur.fetchall()
            cur.execute(
                f'''
                select * from meals
                where meals_id ={meal_id};
                '''
            )
        rows=cur.fetchall()
        rows+=rows1
        conn.commit()
        cur.close()
        print("GET Meal")
        return rows
    else:
        print("error")


@app.route('/users/<user_id>/add_meals/<meals_id>',methods = ['GET', 'POST'])
def add_meals_to_user(user_id,meals_id):
    if request.method=='POST':
        user_id=request.args.get('user_id')
        meals_id=request.args.get('meals_id')
    if request.method=='GET':
        cur=conn.cursor()
        cur.execute(
            f'''
            insert into journal (log_id,user_id,meals_id)
            values
	            (nextval('seq_journal'),{user_id},'{meals_id}')
            '''
            )
        
        conn.commit()
        cur.close()
        print("GET USER INFO")
        return "GET USER INFO"
    else:
        print("error")

@app.route('/users/<user_id>/remove_meals/<meals_id>',methods = ['GET', 'POST'])
def remove_meal_from_account(user_id,meals_id):
    if request.method=='POST':
        user_id=request.args.get('user_id')
        meals_id=request.args.get('meals_id')
    if request.method=='GET':
        cur=conn.cursor()
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
        print("GET USER INFO")
        return "GET USER INFO"
    else:
        print("error")

@app.route('/search/<product_id>',methods = ['GET', 'POST'])
def search_product(product_id):
    if request.method=='POST':
        product_id=request.args.get('product_id')
    if request.method=='GET':
        cur=conn.cursor()
        if product_id=='all':
            cur.execute(
                f'''
                select product_id, name from product
                '''
                )
        else:
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
        return rows
    else:
        print("error")


@app.route('/search_with_limit/<limit>',methods = ['GET', 'POST'])
def earch_with_limit(limit):
    if request.method=='POST':
        limit=request.args.get('limit')
    if request.method=='GET':
        cur=conn.cursor()
        
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
        return rows
    else:
        print("error")
    

@app.route('/users/<user_id>/delete_all_meals',methods = ['GET', 'POST'])
def delete_all_meals_from_account(user_id=3):
    if request.method=='POST':
        user_id=request.args.get('user_id')

    if request.method=='GET':
        cur=conn.cursor()
        cur.execute(
            f"delete                                    \
            from journal                                \
            where user_id = {user_id};"
            )
        
        conn.commit()
        cur.close()
    else:
        print("error")

@app.route('/users/get_meals_sum/<user_id>',methods = ['GET', 'POST'])
def sum_all_meals_by_user(user_id):
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
        conn.commit()
        cur.close()
        result={
            'calories'      :float(rows[0][0]),
            'squirrels'     :float(rows[0][1]),
            'fats'          :float(rows[0][2]),
            'carbohydrates' :float(rows[0][3])
        }
        print(result, flush=True)
        
        return result
    else:
        print("error")
app.run(debug=True,host=HOST,port=PORT)