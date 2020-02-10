from django.test import TestCase




# Create your tests here.


##右键运行
import os
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo03.settings")
    import django
    django.setup()

    print('helllo')