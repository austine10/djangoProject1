from django.db import models


class my_notes(models.Model):
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.subject

    def __str__(self):
        return '{}'.format(self.subject, self.description)

    class meta:
        verbose_name_plural = 'My notes'
        verbose_name_plural_desc = 'descriptions'
