from src.admin.base import SecureModelView
from src.config import Config


class BookView(SecureModelView):
    edit_modal = True
    create_modal = True
    can_export = True
    column_filters = ["title", "author"]

    column_list = ["title", "author"]
