# -*- coding: utf-8 -*- 
from app import app
from flask import render_template, flash, redirect,url_for
from app.forms import SelectForm, TableForm, LoginForm
from flask_login import current_user, login_user
from app.models import User
from app.postgres_conn import postgr_req
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse


users=''
old_sort_column=None
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = SelectForm()
    form_table= TableForm()
    global users
    global old_sort_column
    if form.validate_on_submit():
        lisPress = [key[4:]  for (key, value) in (form_table.data).items() if value == True]
        if form_table.validate_on_submit() and len(lisPress)>0:
            sortable_colmn = lisPress[0]
            if old_sort_column and old_sort_column==sortable_colmn:
                users = sorted(users, key=lambda k: k[sortable_colmn],reverse=True)
                old_sort_column=None
            else:
                users = sorted(users, key=lambda k: k[sortable_colmn])
                old_sort_column=sortable_colmn
                
            #flash(' {}    sort: {}'.format(sortable_colmn, old_sort_column))
            return render_template('index.html', title='HoMe', form=form, form_table=form_table,users = users)
        #return redirect('/index')
        count_string,users = postgr_req(form.data)
        flash('Lines All {}'.format(count_string))
        old_sort_column=None
        return render_template('index.html', title='HoMe', form=form, form_table=form_table,users = users)
    else:
        if form_table.validate_on_submit():
            print('FORM2-2')
        return render_template('index.html', title='HoMe', form=form, form_table=form_table, users = users)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/yar', methods=['GET', 'POST'])
def yar():
    form = SelectForm()
    form_table= TableForm()
    global users
    global old_sort_column
    return render_template('yar.html', title='HoMe', form=form, form_table=form_table, users = users)

@app.route('/kostr', methods=['GET', 'POST'])
def kostr():
    form = SelectForm()
    form_table= TableForm()
    global users
    global old_sort_column
    return render_template('kostr.html', title='HoMe', form=form, form_table=form_table, users = users)
