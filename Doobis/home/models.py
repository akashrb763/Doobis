
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
   country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True) 
   city = models.ForeignKey('cities_light.City', on_delete=models.SET_NULL, null=True, blank=True)

    

class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        if not phone_number:
            raise ValueError('The Phone Number must be set')

        user = self.model(
            username=username,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_user(self, email, password=None, **extra_fields):
    #     if not email:
    #         raise ValueError(_('The Email must be set'))
        
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, username, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # account_type= models.ForeignKey(Account_Type,on_delete=models.CASCADE)
    ACCOUNT_TYPE = (
        ("Bussiness Buyer","Bussiness Buyer"),
        ("Bussiness Invester","Bussiness Invester"),
        ("Doobiz Franchaise","Doobiz Franchaise")
    )

    # uid = models.IntegerField(unique=True, null=False, blank=False)
    account_type = models.CharField(max_length = 20,choices = ACCOUNT_TYPE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=150, unique=True)
    # age = models.IntegerField(blank=True, null=True)
    phone_number = models.IntegerField( blank=True,null=True)
    email = models.EmailField(unique=True)
    official_email = models.EmailField(blank=True,null=True)
    status = models.CharField(max_length=50,blank=True, null=True)
    verified = models.BooleanField(default=False)
    
    registered_date = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    terms_and_conditions = models.BooleanField(default=False,blank=True, null=True)
    # verify_paid=models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    cover_picture = models.ImageField(upload_to='cover_pictures', blank=True, null=True)
    # bio = models.TextField(blank=True)
    # work = models.CharField(max_length=255, blank=True)
    # education = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True,null=True)
    address = models.CharField(max_length=120, blank=True,null=True)
    postcode = models.CharField(max_length=10,blank=True,null=True)
    # country = models.CharField(max_length=30, blank=True,null=True)
    
    country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True) 
    state = models.ForeignKey('cities_light.Region', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey('cities_light.City', on_delete=models.SET_NULL, null=True, blank=True)

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    # def save(self, *args, **kwargs):
    #     if not self.uid:
    #         last_uid = CustomUser.objects.aggregate(models.Max('uid'))['uid__max'] or 99999
    #         self.uid = last_uid + 1
    #     super().save(*args, **kwargs)

    class Meta:
       permissions = [
            ('can_view_customuser', 'Can view custom users'),
            ('can_change_customuser', 'Can change custom users'),
            ('can_delete_customuser', 'Can delete custom users'),
        ]

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_permissions',
        related_query_name='customuser_permission',
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_groups',
        related_query_name='customuser_group',
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )


# class UserPropose(models.Model):
#     party_a=models.CharField(max_length=150)
#     party_b=models.CharField(max_length=150)
#     propose_id=models.CharField(max_length=150, unique=True)
#     accepte=models.BooleanField(null=True)
#     propose_date=models.DateTimeField(default=timezone.now)
#     sing_1=models.ImageField(upload_to='sing_1', blank=True, null=True)
#     sing_2=models.ImageField(upload_to='sing_2', blank=True, null=True)
#     re_props=models.IntegerField(blank=True, null=True,default=0)
    
    