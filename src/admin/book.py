from src.admin.base import SecureModelView
from src.config import Config
from flask_admin.form.upload import ImageUploadField


class BookView(SecureModelView):
    edit_modal = True
    create_modal = True
    can_export = True
    column_filters = ["project_name", "student_fullname"]

    column_list = [
        "project_name",
        "student_fullname",
        "description",
        "school",
        "student_class",
        "project_link",
        "img",
    ]

    form_overrides = {"img": ImageUploadField}

    form_args = {"img": {"base_path": Config.UPLOAD_PATH}}
