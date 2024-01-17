from src.admin.base import SecureModelView
from wtforms import PasswordField
from werkzeug.security import generate_password_hash



class UserView(SecureModelView):
    can_view_details = True
    can_create = True
    can_delete = True
    column_list = ["username", "role"]

    form_overrides = dict(password=PasswordField)
    form_extra_fields = {
        
        'password': PasswordField('Password')
    }

    form_columns = ('username', 'email', 'role', 'password',)

    
    

    def on_model_change(self, form, model, is_created):
        
        new_password = form.password.data

        if is_created:
            # If it's a new model (e.g., user creation), set the password directly
            model.password = new_password
        else:
            print("Password not updated.")



    


        

        





