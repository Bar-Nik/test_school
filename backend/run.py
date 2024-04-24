# from werkzeug.security import generate_password_hash, check_password_hash
# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

import os
from app.Managers.ConfigManager import ConfigManager
from app.Managers.LogManager import LogManager
from app.Managers.DbManager import DbManager


DIR = os.path.abspath(os.path.dirname(__file__))

config_manager = ConfigManager(DIR)
log_manager = LogManager(config_manager)
db_manager = DbManager(config_manager, log_manager)




# app = Flask(__name__)







# надо сделать корневой роут /auth
# от него уже выстраивать
# auth/login
# auth/logout
# auth/register
# Еще нужны методы для востановления аккаунта
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     # уточнится, нужно ли в этой библиотеке открывать транзацкцию?
#     if request.method == 'POST':
#         try:
#             hash = generate_password_hash(request.form['password'])
#             # user = Users(**kwargs)
#             user = Users(email=request.form['email'], password=hash, first_name=request.form['first_name'], last_name=request.form['last_name'])
#             db.session.add(user)
#             db.session.commit()
#         except:
#             db.session.rollback()
#             # использовать LogManager
#             print("Ошибка добавления в БД")
#
#
#     return render_template('register.html', title='Регистрация')
#
# if __name__ == "__main__":
#     app.run(debug=True)
# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#         app.run(debug=True)