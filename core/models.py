from django.db import models
COUNTY_CHOICES = (
    ('Baringo', 'Baringo'),
    ('Bomet', 'Bomet'),
    ('Bungoma', 'Bungoma'),
    ('Busia', 'Busia'),
    ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'),
    ('Embu', 'Embu'),
    ('Garissa', 'Garissa'),
    ('Homa Bay', 'Homa Bay'),
    ('Isiolo', 'Isiolo'),
    ('Kajiado', 'Kajiado'),
    ('Kakamega', 'Kakamega'),
    ('Kericho', 'Kericho'),
    ('Kiambu', 'Kiambu'),
    ('Kilifi', 'Kilifi'),
    ('Kirinyaga', 'Kirinyaga'),
    ('Kisii', 'Kisii'),
    ('Kisumu', 'Kisumu'),
    ('Kitui', 'Kitui'),
    ('Kwale', 'Kwale'),
    ('Laikipia', 'Laikipia'),
    ('Lamu', 'Lamu'),
    ('Machakos', 'Machakos'),
    ('Makueni', 'Makueni'),
    ('Mandera', 'Mandera'),
    ('Marsabit', 'Marsabit'),
    ('Meru', 'Meru'),
    ('Migori', 'Migori'),
    ('Mombasa', 'Mombasa'),
    ('Murang’a', 'Murang’a'),
    ('Nairobi', 'Nairobi'),
    ('Nakuru', 'Nakuru'),
    ('Nandi', 'Nandi'),
    ('Narok', 'Narok'),
    ('Nyamira', 'Nyamira'),
    ('Nyandarua', 'Nyandarua'),
    ('Nyeri', 'Nyeri'),
    ('Samburu', 'Samburu'),
    ('Siaya', 'Siaya'),
    ('Taita-Taveta', 'Taita-Taveta'),
    ('Tana River', 'Tana River'),
    ('Tharaka-Nithi', 'Tharaka-Nithi'),
    ('Trans-Nzoia', 'Trans-Nzoia'),
    ('Turkana', 'Turkana'),
    ('Uasin Gishu', 'Uasin Gishu'),
    ('Vihiga', 'Vihiga'),
    ('Wajir', 'Wajir'),
    ('West Pokot', 'West Pokot'),
)

# Create your models here.
class Members(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    phonenumber=models.IntegerField()
    county=models.TextField(choices=COUNTY_CHOICES,default="")

