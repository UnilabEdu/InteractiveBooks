from src.admin.base import SecureModelView
from flask_ckeditor import CKEditorField
from markupsafe import Markup
from src.config import Config
from flask_admin.form.upload import ImageUploadField
from src.models import Teacher, Mentor


class MentorView(SecureModelView):
    can_view_details = True
    edit_modal = True
    create_modal = True
    column_list = ["fullname","books"]
    column_searchable_list = ["fullname"]
    column_labels = {"fullname": "მენტორი",
                     "books":"წიგნი"}

    column_default_sort = ("fullname", True)


class TeacherView(SecureModelView):
    can_view_details = True
    edit_modal = True
    create_modal = True
    column_list = ["fullname","books"]
    column_searchable_list = ["fullname"]
    column_labels = {"fullname": "მასწავლებლი",
                     "books":"წიგნი"}
    column_default_sort = ("fullname", True)



class BookView(SecureModelView):
    can_view_details = True
    edit_modal = True
    create_modal = True
    can_create = True
    can_edit = True
    # can_export = True
    
    inline_models = (Mentor, Teacher)

    column_filters = ["project_name", "student_fullname", "school", "student_class"]

    column_default_sort = ("project_name", True)

    export_types = ["csv"]
    
    column_formatters = {
        "img": lambda v,c,m,n: Markup(f"<img src='/static/img/{m.img}' width='64px'>")
    }
    
    column_list = [
        "img",
        "project_name",
        "student_fullname",
        "description",
        "school",
        "student_class",
        "project_link",
        "teachers",
        "mentors",
        
    ]

    form_columns = [
        "project_name",
        "student_fullname",
        "description",
        "school",
        "student_class",
        "teachers",
        "mentors",
        "project_link",
        "img",
    ]
    form_extra_fields = {
        'description': CKEditorField('აღწერა')
    }

    form_overrides = {"img": ImageUploadField}

    form_args = {"img": {"base_path": Config.UPLOAD_PATH, "url_relative_path": "img/"}}

    column_sortable_list = [
        "project_name",
        "student_fullname",
        "school",
    ]

    column_searchable_list = [
        "project_name",
        "student_fullname",
        "school",
        "student_class",
    ]

    column_labels = {
        "project_name": "სათაური",
        "student_fullname": "მოსწავლე",
        "description": "აღწერა",
        "school": "სკოლა",
        "student_class": "კლასი",
        "teachers": "მასწავლებელი",
        "mentors": "მენტორი",
        "project_link": "ბმული  ინტერაქტიულ წიგნზე",
        "img": "მთავარი ვიზუალი",
    }
    column_details_list = [
        "img",
        "project_name",
        "description",
        "student_fullname",

        "school",
        "student_class",

        "project_link",
        "teachers",
        "mentors",
    ]
