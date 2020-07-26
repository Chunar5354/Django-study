from django.db import models

# Create your models here.
class Voltage_AB(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Voltage_AB'

class Voltage_BC(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Voltage_BC'

class Voltage_CA(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Voltage_CA'

class Current_A(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Current_A'

class Current_B(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Current_B'

class Current_C(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Current_C'

class Rev(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Rev'

class Temp_controller_env(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Temp_controller_env'

class Temp_fore_bearing(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Temp_fore_bearing'

class Temp_fore_winding_A(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Temp_fore_winding_A'

class Temp_fore_winding_B(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Temp_fore_winding_B'

class Temp_fore_winding_C(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Temp_fore_winding_C'

class Temp_rear_bearing(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Temp_rear_bearing'

class Temp_rotator(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Temp_rotator'

class Temp_water(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Temp_water'

class Vib_fore_bearing(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Vib_fore_bearing'

class Vib_rear_bearing(models.Model):
	create_time = models.DateTimeField()
	value = models.DecimalField(max_digits=6, decimal_places=2)

	# def __str__(self):
	# 	return self.value

	class Meta():
		verbose_name_plural = 'Vib_rear_bearing'

