from flask import request
from flask_login import login_user,logout_user,current_user,login_required
from models import User

def register_routes(app,db,bcrypt):

    @app.route('/',methods=['GET', 'POST'])
    def index():
        if current_user.is_authenticated:
            return str(current_user.username)
        else:
            return 'no user is logged in'
        
    @app.route('/signup', methods=['POST'])
    def signup():
        if request.method == 'GET':
            return "hello"
        elif request.method == 'POST':
             username=request.form.get('username')
             password=request.form.get('password')
             hashed_password=bcrypt.generate_password_hash(password)
         
        user=User(username=username, password=hashed_password)
        
        db.session.add(user)
        db.session.commit()
        return user


    @app.route('/login', methods=['GET','POST'])
    def login():
        if request.method == 'GET':
            return "hello"
        elif request.method == 'POST':
             username=request.form.get('username')
             password=request.form.get('password')
             hashed_password=bcrypt.generate_password_hash(password)

             user=User.query.filter(User.username==username).first()
             if bcrypt.check_password_hash(user.password,password):
                 login_user(user)
             else:
                 return 'Failed'

    @app.route('/logout')
    def logout():
        logout_user()
        return 'success'
