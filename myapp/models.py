from django.db import models

# Create your models here.

class Project(models.Model):
 name = models.CharField(max_length=200)

class Task(models.Model):
 title = models.CharField(max_length=200)#texto no mayor a 200 letras
 description = models.TextField()#texto indefinido
 project = models.ForeignKey(Project,on_delete=models.CASCADE)#se le ordena que al eliminar un dato,debe eliminar todo lo relacionado

 #ejecuto  python  manage.py makemigrations para que  argue el modelo en la tabla migration
 #ejecuto  python  manage.py migrate para que pueda caragar en la base de datos
 #python manage.py shell-para sacar la consola de py
 #from myapp.models import Project-ates de almacenar datos
