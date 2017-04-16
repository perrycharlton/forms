# # from flask_wtf import FlaskForm
# # from wtforms import BooleanField, StringField, PasswordField
# # from wtforms.validators import InputRequired, Length, Email, Regexp, EqualTo
#
#
# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
#     password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=20)])
#     remember = BooleanField('Remember Me', default=False)
#
#
# class SignupForm(FlaskForm):
#     first_name = StringField('First Name', validators=[InputRequired()])
#     last_name = StringField('Last Name', validators=[InputRequired()])
#     email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
#     username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15),
#                                                    Regexp("^[a-zA-Z0-9]*$",
#                                                           message="Username can only contain letters and numbers")
#                                                    ])
#     password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=20)])
#
#     confirm = PasswordField('Repeat Password', validators=[InputRequired(), EqualTo('password',
#                                                                                     message='Password must match')
#                                                            ])
#
#
# class ContactsForm(FlaskForm):
#     first_name = StringField('First Name')
#     last_name = StringField('Last Name')
#     email = StringField('Email', validators=[Email(message='Invalid email'), Length(max=50)])
#     username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15),
#                                                    Regexp("^[a-zA-Z0-9]*$",
#                                                           message="Username can only contain letters and numbers")
#                                                    ])
#
#
# class AdminForm(FlaskForm):
#     first_name = StringField('First Name')
#     last_name = StringField('Last Name')
#     email = StringField('Email')
#     username = StringField('Username')