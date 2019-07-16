from django.db import models
from django.conf import settings


class Simulation_report(models.Model):
    simulation_id = models.BigIntegerField(default=0)
    system_time = models.BigIntegerField(default=0)
    record_id = models.BigIntegerField(default=0)
    event = models.BigIntegerField(default=0)
    object = models.BigIntegerField(default=0)
    operation = models.BigIntegerField(default=0)
    int1 = models.BigIntegerField(default=0)
    int2 = models.BigIntegerField(default=0)
    double1 = models.FloatField(max_length=1000, default=0)
    double2 = models.FloatField(max_length=1000, default=0)
    comment = models.TextField(max_length=150, default="")

    class Meta:
        db_table = 'simulation_report'

    def __unicode__(self):
        return self.simulation_id


class User_model(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'user_model'

    def __unicode__(self):
        return "Модель: {0}".format(str(self.model_name))


class Computing_node(models.Model):
    model = models.ForeignKey('User_model', on_delete=models.CASCADE)
    cn_name = models.TextField()
    ncpu = models.IntegerField()
    cpu_speed = models.IntegerField()
    avr_data_value = models.IntegerField()

    class Meta:
        db_table = 'computing_node'

    def __unicode__(self):
        return "СN: {0}".format(str(self.cn_name))


class Data_generator(models.Model):
    model = models.ForeignKey('User_model', on_delete=models.CASCADE)
    dg_name = models.TextField()
    freq_data = models.IntegerField()
    data_value = models.IntegerField()

    class Meta:
        db_table = 'data_generator'

    def __unicode__(self):
        return "DG: {0}".format(str(self.dg_name))


class Disk_server(models.Model):
    model = models.ForeignKey('User_model', on_delete=models.CASCADE)
    disk_server_name = models.TextField(max_length=20)
    disk_pool_size = models.FloatField(max_length=50)

    class Meta:
        db_table = 'disk_server'

    def __unicode__(self):
        return "DS: {0}".format(str(self.disk_server_name))


class Switch(models.Model):
    model = models.ForeignKey('User_model', on_delete=models.CASCADE)
    switch_name = models.TextField()
    sw_capacity = models.FloatField()

    class Meta:
        db_table = 'switch'

    def __unicode__(self):
        return "Sw: {0}".format(str(self.switch_name))



