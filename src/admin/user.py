from src.admin.base import SecureModelView
from wtforms import PasswordField
from werkzeug.security import generate_password_hash
from src.models import User


class UserView(SecureModelView):
    can_view_details = True
    can_create = True
    can_delete = True
    column_list = ["username", "role"]

    form_extra_fields = {
        'password': PasswordField('Password')
    }

    form_columns = ('username', 'password', 'email', 'role')

    
    
    def on_model_change(self, form, model, is_created):
        print(f"Form data: {form.data}")
        print(f"Model data: {model.__dict__}")
        
        if 'password' in form:
            new_password = form.password.data
            print(f"New password: {new_password}")
            if new_password:
                model.password = generate_password_hash(new_password)
        elif model.id:
            
            model.password = User.query.get(model.id).password

    


        

        





