
from django.db import models

class Course(models.Model):
    course = models.CharField(max_length=122,verbose_name = 'Курс')
    about_course = models.TextField(max_length=122,verbose_name = 'О курсе')
    title = models.TextField(max_length=122,verbose_name = 'Заголовок')
    upload_file = models.FileField(upload_to = 'upload_file')
    image = models.ImageField(upload_to = 'course/Y%/%m/%d',verbose_name = 'Фотка')
    def __str__(self) -> str:
        return self.course
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'



class Lesson_Material(models.Model):
    lesson = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lesson_material')
    lesson_theme =models.CharField(max_length=122,verbose_name ='Тема урока' )
    title = models.CharField(max_length=122,verbose_name ='Заголовок' )
    image = models.ImageField(upload_to='lesson_material/%Y/%m/%d/')
    context1 = models.TextField(max_length=122,verbose_name ='Текст' )
    context2 = models.TextField(max_length=122,verbose_name ='Текст2' )
    def __str__(self) -> str:
        return self.lesson
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'





























