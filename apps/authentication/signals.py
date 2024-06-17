from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from apps.user.models.information import UserInformationModel


@receiver(post_save, sender=User)
def _post_save_user(sender, instance, **kwargs):
    if not instance.password.startswith('pbkdf2'):
        instance.password = make_password(instance.password)
        instance.save()
    if not hasattr(instance, 'information'):
        UserInformationModel.objects.create(user=instance)


# # Create default user admin
# @receiver(post_migrate)
# def created_user_admin(sender, **kwargs):
#     users_db = User.objects
#     user_admin= {
#                 'username': 'admin',
#                 'email': 'admin@yopmail.com',
#                 'password': '1234'
#                 }
    
#     if not users_db.filter(username=user_admin['username']).exists():
#         users_db.create_superuser(**user_admin)

@receiver(post_migrate)
def create_default_users(sender, **kwargs):
    users_db = User.objects
    information_db = UserInformationModel.objects

    try:
        # Crea el usuario administrador predeterminado
        if not users_db.filter(username='admin'):
            admin_user = users_db.create_superuser('admin', 'admin@yopmail.com', '1234')

            admin_information = {
                'user': admin_user,
                'identification': 'admin_id',
                'user_type': 0
            }

            # information_db.create(**admin_information)
            existing_information = UserInformationModel.objects.filter(user=admin_user).first()
            if existing_information:
                existing_information.delete()
                information_instance = information_db.create(user=admin_user, identification=admin_information['identification'], user_type=admin_information['user_type'])
            else:
                print(f'Información para el usuario {username} ya existe.')
                print('🥳 ¡Usuario administrador creado!')
    except Exception as e:
        print(f'Error al crear el usuario administrador: {e}')

    # Lista de usuarios a crear
    users_to_create = [
        {
            'username': 'vicerrector@yopmail.com',
            'email': 'vicerrector@yopmail.com',
            'first_name': 'Diego',
            'last_name': 'Pedrozo',
            'password': '1234',
            'information': {
                "identification": "1151898",
                "user_type": 6
            }
        },
        {
            'username': 'biblioteca@yopmail.com',
            'email': 'biblioteca@yopmail.com',
            'first_name': 'Kenn',
            'last_name': 'Marcucci',
            'password': '1234',
            'information': {
                "identification": "1151891",
                "user_type": 5
            }
        },
        {
            'username': 'decanoingenieria@yopmail.com',
            'email': 'decanoingenieria@yopmail.com',
            'first_name': 'Sebastian',
            'last_name': 'Bermon',
            'password': '1234',
            'information': {
                "identification": "1151909",
                "user_type": 4
            }
        },
        {
            'username': 'estudiosingsistemas@yopmail.com',
            'email': 'estudiosingsistemas@yopmail.com',
            'first_name': 'Andres',
            'last_name': 'Camperos',
            'password': '1234',
            'information': {
                "identification": "1151900",
                "user_type": 2
            }
        }
        ,
        {
            'username': 'departamentoingsistemas@yopmail.com',
            'email': 'departamentoingsistemas@yopmail.com',
            'first_name': 'Juan',
            'last_name': 'Nieto',
            'password': '1234',
            'information': {
                "identification": "1151234",
                "user_type": 3
            }
        }
    ]

    for user_data in users_to_create:
        information_data = user_data['information']
        username = user_data['username']
        email = user_data['email']
        password = user_data['password']
        
        user_instance, created = users_db.get_or_create(username=username, email=email, defaults={'password': password})
        existing_information = UserInformationModel.objects.filter(user=user_instance).first()

        if existing_information:
            existing_information.delete()
            information_instance = information_db.create(user=user_instance, identification=information_data['identification'], user_type=information_data['user_type'])
        else:
            print(f'Información para el usuario {username} ya existe.')
