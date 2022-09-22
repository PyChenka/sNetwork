from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()         # обращаемся к основной! модели User


class CreationForm(UserCreationForm):           # создаем свой класс для формы регистрации
    class Meta(UserCreationForm.Meta):          # наследуется класс Meta, вложенный в класс UserCreationForm
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')