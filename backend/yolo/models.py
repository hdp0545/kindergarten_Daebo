from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.crypto import get_random_string

make_stream_key = partial(get_random_string, 20)

class Stream(models.Model):

    key = models.CharField(max_length=20, default=make_stream_key, unique=True)
    started_at = models.DateTimeField(null=True, blank=True)

    @property
    def is_live(self):
        return self.started_at is not None

    @property
    def hls_url(self):
        return reverse("hls-url", )

    @receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid="create_stream_for_user")
    def create_stream_for_user(sender, instance=None, created=False, **kwargs):
        """ Create a stream for new users.
        """
        if created:
            Stream.objects.create(user=instance)
# Create your models here.
