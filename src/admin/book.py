from src.admin.base import SecureModelView
from src.config import Config
from flask_admin.form.upload import ImageUploadField
from src.models import Teacher, Mentor


class MentorView(SecureModelView):
    can_view_details = True
    edit_modal = True
    create_modal = True
    column_list = ["fullname"]
    column_searchable_list = ["fullname"]
    column_labels = {"fullname": "მენტორის სახელი და გვარი"}
    column_default_sort = ("fullname", True)


class TeacherView(SecureModelView):
    can_view_details = True
    edit_modal = True
    create_modal = True
    column_list = ["fullname"]
    column_searchable_list = ["fullname"]
    column_labels = {"fullname": "მასწავლებლის სახელი და გვარი"}
    column_default_sort = ("fullname", True)



class BookView(SecureModelView):
    can_view_details = True
    edit_modal = True
    create_modal = True
    can_create = True
    can_edit = True
    can_export = True

    inline_models = (Mentor, Teacher)

    column_filters = ["project_name", "student_fullname", "school", "student_class"]

    column_default_sort = ("project_name", True)

    column_list = [
        "project_name",
        "student_fullname",
        "description",
        "school",
        "student_class",
        "project_link",
        "img",
    ]

    form_columns = [
        "project_name",
        "student_fullname",
        "description",
        "school",
        "student_class",
        "mentors",
        "teachers",
        "project_link",
        "img",
    ]

    form_overrides = {"img": ImageUploadField}

    form_args = {"img": {"base_path": Config.UPLOAD_PATH}}

    column_sortable_list = [
        "project_name",
        "student_fullname",
        "school",
        "school",
    ]

    column_searchable_list = [
        "project_name",
        "student_fullname",
        "school",
        "student_class",
        "school",
    ]

    column_labels = {
        "project_name": "სათაური",
        "student_fullname": "მოსწავლის სახელი და გვარი",
        "description": "აღწერა",
        "school": "სკოლა",
        "student_class": "კლასი",
        "mentors": "მენტორის სახელი და გვარი",
        "teachers": "მასწავლებლის სახელი და გვარი",
        "project_link": "ბმული  ინტერაქტიულ წიგნზე",
        "img": "მთავარი ვიზუალი",
    }
