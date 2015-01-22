from django.db import models
from django.forms import extras
from polymorphic import PolymorphicModel

# This isnt pep8 yet. also documentation
# These are the models for West KY Mentoring.  This will be all of the tables
# needed in the database.
# Let it be known that Django automatically creates a pk for our tables
# These will definitly need to have modules doe add them if you need them
STATE_CHOICES = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

class Address(models.Model):
    street_num = models.CharField(max_length=200)
    street_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2,choices=STATE_CHOICES)
    zip_code = models.CharField(max_length=15, blank=True)
    # country is currently excluded

class Individual(PolymorphicModel):
    ssn = models.TextField(null=True, max_length=9) # This can be null because our client deals with a lot of international students/people
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(null=True, max_length=200)
    last_name = models.CharField(max_length=200)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    drivers_lic = models.ImageField(null=True)
    address = models.ForeignKey(Address)
    
class Mentor(Individual):
    # Functional Area?
    education = models.TextField(null=True)
    job_exp = models.TextField('Job Experience', null=True)

    
class Mentee(Individual):
    interests = models.TextField(null=True)
    education = models.TextField(null=True)
    
class Intern(Individual):
    # catigories?
    education = models.TextField(null=True)
    job_exp = models.TextField('Job Experience', null=True)

class Volunteer(Individual):
    job_exp = models.TextField('Job Experience', null=True)
    
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=True) # True, in case of an all day event
    location = models.ForeignKey(Address)
    # event_budget
    
class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    Sponsor_type = models.CharField(max_length=200,choices=(('Personal','Personal'),('Company','Company')))
    
class Donation(models.Model):
    sponsor = models.ForeignKey(Event)
    amount = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    description = models.TextField(null=True)
    donation_type = models.CharField(max_length=200,choices=(('Currency','Currency'),('Equipment','Equipment'),('Food','Food'),('Toys','Toys'),('Ink Cartridges','Ink Cartridges')))
    
class Badge(models.Model):
    name = models.CharField(max_length=200)
    requirements = models.TextField(null=True)
    description = models.TextField(null=True)
    

class Event_Worker(models.Model): # This one might not be needed, djanog maks many2manys prety easy
    event = models.ForeignKey(Event)
    individual = models.ForeignKey(Individual)

    
