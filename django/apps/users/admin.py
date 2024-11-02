from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

my_user = get_user_model()

# # Добавляем поле с биографией 
# # к стандартному набору полей (fieldsets) пользователя в админке.
# UserAdmin.fieldsets += (
#     # Добавляем кортеж, где первый элемент — это название раздела в админке,
#     # а второй элемент — словарь, где под ключом fields можно указать нужные поля.
#     ('Extra Fields', {'fields': ('bio',)}),
# )
# # Регистрируем модель в админке:

UserAdmin.fieldsets += (
    ('Extra Fields', {'fields': ('contact', 'is_top_manager')}),
)

admin.site.register(my_user, UserAdmin)
