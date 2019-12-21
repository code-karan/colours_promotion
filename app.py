from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
#from flask_googlemaps import GoogleMaps
from datetime import datetime

# create app
app = Flask(__name__)

# map
#app.config['GOOGLEMAPS_KEY'] = "8JZ7i18MjFuM35dJHq70n3Hx4"
#GoogleMaps(app)

# mail
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = '', # your username
    MAIL_PASSWORD = ''  # your password
)
mail = Mail(app)

'''
# database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/colorspromodb'
db = SQLAlchemy(app)

# database table(Contacts) and fields(sno, name, etc;)
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(600), nullable=False)
    date = db.Column(db.String(120), nullable=False)

'''
    


# url route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/clients')
def clients():
    return render_template('clients.html')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # assign fields to input values in form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        date = datetime.now()

        # make an entry for database
        #entry = Contacts(name=name, email=email, message=message, date=date)

        # add entry to database
        #db.session.add(entry)
        #db.session.commit()

        # send mail
        mail.send_message('[ColorsPromotion]-New message from {}'.format(name),
                            sender = email, 
                            recipients = ['ksinghasane14@gmail.com', 'avats765@gmail.com'],
                            body = message + '\n' + email
                            )

        return render_template('contact.html', msg = 'Email sent!')

    else:
        return render_template('contact.html')

app.run(debug=True)