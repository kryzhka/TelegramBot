from flask import request
import psycopg2

conn = psycopg2.connect(
    database = os.getenv('DB_NAME'),
    user     = os.getenv('DB_USER'),
    host     = os.getenv('DB_HOST'),
    password = os.getenv('DB_PASS'),
    port     = os.getenv('DB_PORT')
    )

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
    except:
        print('ERR: USER IS NOT ADD',flush=True)
        return [False]