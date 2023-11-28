from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class University(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Universitet Nomi')

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        verbose_name = 'Univeristet'


class TTJ(BaseModel):
    title = models.CharField(max_length=255, verbose_name='TTJ nomi')
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='ttj_university',
    )

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        verbose_name = 'TTJ'


class Floor(BaseModel):
    floor = models.CharField(max_length=255, verbose_name='Hona')
    room = models.ForeignKey("self", on_delete=models.PROTECT, verbose_name="etaj", related_name='hona', null=True, blank=True)

    def __str__(self):
        return f'{self.floor}'

    class Meta:
        verbose_name = 'Honalar'


class Group(BaseModel):
    name = models.CharField(max_length=125, verbose_name='Guruh')

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        verbose_name = 'Guruhlar'


class Student(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name='To\'liq ismi')
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='student_group',
        verbose_name='Student Group'
    )
    ttj = models.ForeignKey(
        TTJ,
        on_delete=models.CASCADE,
        related_name='student_ttj',
        verbose_name='TTJ'
    )
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='attendance_university',
        verbose_name='Universitet'
    )
    floor = models.ForeignKey(
        Floor,
        on_delete=models.CASCADE,
        related_name='attendance_floor',
        null=True,
        blank=True,
        verbose_name='Hona'
    )
    phone = PhoneNumberField()

    def __str__(self):
        return f'{self.id} - {self.phone}'

    class Meta:
        verbose_name = 'Studentlar'


class Attendance(BaseModel):
    date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Sana')
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendace_student',
        verbose_name='Students',
    )
    on_ttj = models.BooleanField(default=False, verbose_name='yotoqhonada')

    class Meta:
        verbose_name = 'Yoqlama'



