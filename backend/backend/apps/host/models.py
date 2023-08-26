from django.db import models


class Host(models.Model):
    class Meta:
        db_table = 'ao_host'
        verbose_name = '主机'
    # def __str__(self):

    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(unique=True)
    operating_system = models.CharField(max_length=50)
    cpu_cores = models.PositiveIntegerField()
    memory_gb = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

