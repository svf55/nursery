from django.db import models
from django.utils import timezone
from child.models import Child


class Journal(models.Model):
    """
    Журнал
    """
    FATHER = 'F'
    MOTHER = 'M'

    PARENT_CHOICES = (
        (FATHER, 'Отец'),
        (MOTHER, 'Мать'),
    )

    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    led_at = models.DateTimeField('Время прихода', null=True, blank=True)
    led_parent = models.CharField('Родитель привел', max_length=1,
                                  choices=PARENT_CHOICES, null=True, blank=True)
    took_at = models.DateTimeField('Время ухода', null=True, blank=True)
    took_parent = models.CharField('Родитель забрал', max_length=1,
                                   choices=PARENT_CHOICES, null=True, blank=True)
    ts = models.DateTimeField('Дата записи', default=timezone.now)

    def __str__(self):
        return "{} {}".format(self.child.name, self.ts.date())

