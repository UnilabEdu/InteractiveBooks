from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose
from flask import url_for, redirect
from flask_admin.menu import MenuLink
from flask_login import current_user



class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("auth.login"))


class SecureIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("auth.login"))
    
    def is_visible(self):
        return False



class LogoutMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated
    
class LoginMenuLink(MenuLink):
    def is_accessible(self):
        return not current_user.is_authenticated 
    