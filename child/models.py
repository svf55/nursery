from django.db import models


class Child(models.Model):
    """
    Ребенок
    """
    MAN = 'M'
    FEMALE = 'F'

    SEX_CHOICES = (
        (MAN, 'Мужской'),
        (FEMALE, 'Женский'),
    )

    name = models.CharField('Имя', max_length=256)
    image = models.ImageField('Фото', upload_to='images/',
                              blank=True, null=True
                              )
    sex = models.CharField('Пол', max_length=1, choices=SEX_CHOICES)
    birth_date = models.DateField('Дата рождения', db_index=True,
                                  null=True, blank=True)
    nursery_class = models.CharField('Класс', max_length=10, blank=True)
    is_studying = models.BooleanField('Учится/нет', default=False, db_index=True)

    def __str__(self):
        return self.name

