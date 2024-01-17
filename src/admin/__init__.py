from flask_admin import Admin

from src.admin.base import SecureIndexView, SecureModelView
from src.admin.user import UserView
from src.admin.book import BookView, MentorView, TeacherView
from src.admin.base import LogoutMenuLink



admin = Admin(
    index_view=SecureIndexView(),
    template_mode="bootstrap4"
    
)

admin.add_link(LogoutMenuLink(name="Logout", category="", url="/logout"))



