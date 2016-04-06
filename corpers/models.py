from time import time
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


def get_upload_file_name(filename):
    return 'uploaded_files/%s_%s' % (str(time()).replace('.', '_'), filename)


class Corper(models.Model):
    corper = models.ForeignKey(User)
    state_code = models.CharField(max_length=12)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    slug = models.SlugField(unique=True)
    sex = models.CharField(max_length=6)
    state_of_origin = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=10)
    about = models.TextField()
    phone_number = models.CharField(max_length=15)
    logo = models.FileField(upload_to=get_upload_file_name)

    @property
    def __str__(self):
        return self.state_code

    @models.permalink
    def get_absolute_url(self):
        return ('corper_details', (),
                {
                    'slug': self.slug, })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Corper, self).save(*args, **kwargs)
