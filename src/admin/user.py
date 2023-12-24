from src.admin.base import SecureModelView



class UserView(SecureModelView):
    can_create = True
    can_delete = True
    column_list = ["username", "role"]





