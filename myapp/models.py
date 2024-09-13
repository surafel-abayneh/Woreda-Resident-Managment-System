from django.db import models
from datetime import timedelta
from django.forms import NumberInput


class PersonalInformation(models.Model):
    PI_ID = models.AutoField(primary_key=True)
    F_Name = models.CharField(max_length=15)
    M_Name = models.CharField(max_length=15)
    L_Name = models.CharField(max_length=15)
    Mother_Name = models.CharField(max_length=15)
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    Dob = models.DateField()
    Place_of_birth = models.CharField(max_length=15)
    Date_of_registration = models.DateTimeField(auto_now_add=True)
    Nationality = models.CharField(max_length=15)
    photograph = models.ImageField(upload_to='photos/', null=True, blank=True)
    Phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.F_Name} {self.M_Name} {self.L_Name}'

class House(models.Model):
    House_No = models.AutoField(primary_key=True)
    Woreda = models.CharField(max_length=15)
    Region = models.CharField(max_length=15)
    House_type = models.CharField(max_length=15)
    Family_size = models.CharField(max_length=15)
    Family_names = models.CharField(max_length=55)
    PI_ID = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE)

    def __str__(self):
        return self.House_No

class IDCard(models.Model):
    ID_No = models.AutoField(primary_key=True)
    Given_date = models.DateTimeField(auto_now_add=True)
    Expire_date = models.DateField()
    Emergency_cont_name = models.CharField(max_length=15)
    Emergency_cont_number = models.CharField(max_length=15)
    Blood_Type = models.CharField(max_length=2, default="", choices=[('A', 'A'), ('B', 'B'), ('B+', 'B+'), ('AB', 'AB'), ('O+', 'O+'), ('O-', 'O-')])
    House_No = models.ForeignKey(House, on_delete=models.CASCADE)
    PI_ID = models.ForeignKey(PersonalInformation, related_name='p_info', on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.Expire_date:
            self.Expire_date = (self.Given_date + timedelta(days=730)).date()  # 2 years = 730 days
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.Emergency_cont_name} {self.Emergency_cont_number} {self.Blood_Type}'

class Marriage(models.Model):
    MAR_ID = models.AutoField( primary_key=True)
    Given_date = models.DateTimeField(auto_now_add=True)
    witness_1 = models.CharField(max_length=15)
    witness_2 = models.CharField(max_length=15)
    H_ID_No = models.ForeignKey('PersonalInformation',related_name='Husband_info',default="", on_delete=models.CASCADE)
    W_ID_No = models.ForeignKey('PersonalInformation', on_delete=models.CASCADE)

class Request(models.Model):
    Req_ID = models.AutoField( primary_key=True)
    purpose = models.CharField(max_length=15)
    date = models.DateField()

class Comment(models.Model):
    Com_ID = models.AutoField( primary_key=True)
    purpose = models.CharField(max_length=15)
    date = models.DateField()

class BirthCertificate(models.Model):
    Certi_ID = models.AutoField(primary_key=True)
    PI_ID = models.ForeignKey(PersonalInformation, related_name='personal_info', on_delete=models.CASCADE)
    Father_id = models.ForeignKey(PersonalInformation, related_name='father_info', on_delete=models.CASCADE)
    Mother_id = models.ForeignKey(PersonalInformation, related_name='mother_info', on_delete=models.CASCADE)
    Given_date = models.DateField()
    House_No = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return f"Birth Certificate {self.Certi_ID}"









""" class UserAccount(models.Model):
    User_Id = models.AutoField( primary_key=True)
    position = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    PI_id = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE)
 """
""" class Clearance(models.Model):
    ID_No = models.ForeignKey(IDCard, on_delete=models.CASCADE)
    ReasonOfClearance = models.CharField(max_length=15)
    Date_of_taken = models.DateField()
   
 """
