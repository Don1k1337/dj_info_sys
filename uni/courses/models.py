from django.db import models
from django.db.models import options
from django.utils.translation import gettext_lazy as _
'''Кредиты, оценки, факультет, преподаватель, тайтл, ID, abbr, 
descript, postreq, prereq, program, 
elective or require, general edu, language'''

class Course(models.Model):
    description = models.CharField(max_length=60)
    course_id = models.AutoField(primary_key=True, **options)
    language = models.CharField(max_length=60)
    abbreviation = models.BooleanField(default=False)








    # post_req = models.CharField(max_length=60)
    # pre_req = models.CharField(max_length=60)
    # general_edu = models.CharField(max_length=60)
# class StudentProgram(models.Model):
#     class Faculty(models.TextChoices):
#         IT = 'IT', _('Informational Technology')
#         BA = 'BA', _('Business Administration')
#         LNG = 'LNG', _('Linguistics')
#         LAW = 'LAW', _('Jurisprudence')
#         IR = 'IR', _('International Relationship')
#         CHN = 'CHN', _('Chinese')
#
#         class YearInUni(models.TextChoices):
#             FRESHMAN = 'FR', _('Freshman')
#             SOPHOMORE = 'SO', _('Sophomore')
#             JUNIOR = 'JR', _('Junior')
#             SENIOR = 'SR', _('Senior')
#             GRADUATE = 'GR', _('Graduate')
#
#         year_in_uni = models.CharField(
#             max_length=2,
#             choices=YearInUni.choices,
#             default=YearInUni.FRESHMAN,
#         )
'''class CourseStudentsTransfer(models.Model):
    sid = models.ForeignKey(Student, on_delete=models.CASCADE)
    uni = models.ForeignKey()
    course_name_eng = models.CharField(max_length=60)
    course_name_rus = models.CharField(max_length=60)
    st_program = models.ForeignKey(Student, on_delete=models.CASCADE)
'''