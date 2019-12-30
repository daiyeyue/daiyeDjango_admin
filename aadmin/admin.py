from django.contrib import admin
from aadmin.models import Student, ClassRoom, Teacher

class ClassRoomAdmin(admin.ModelAdmin): # 属于admin.ModelAdmin子类
    pass

@admin.register(Teacher)  # 使用装饰器注册
class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    list_display = ["name", "room", "curTime", "getRoomName"]
    search_fields = ["name"]

    #fields = ["name", "room"]

    fieldsets = (
        ("基本信息", {"fields":["name",]}),
        ("其他信息", {"fields":["room","course"]}),

    )

class StudentAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Student,admin_class=StudentAdmin)
admin.site.register(ClassRoom, admin_class=ClassRoomAdmin)
#admin.site.register(Teacher, admin_class=TeacherAdmin)

