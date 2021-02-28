from django.db import models

# Create your models here.
class country(models.Model):
    Ename = models.CharField(max_length=99 , default='notset')
    Pname = models.CharField(max_length=99 , default='notset')
    mini_name = models.CharField(max_length=99 , default='notset')
    telcode = models.CharField(max_length=9 , default='notset')
    flag_icon = models.ImageField(upload_to ="resourses/", blank=True , null= True ,help_text="size : 16*16")
    flag_imge = models.ImageField(upload_to ="resourses/", blank=False , null= True,help_text="size : 256*256")
    Continent = models.CharField(max_length=30 , default='notset' ,help_text="North America / South America / Asia / Europe / Africa / Oceania")
    wikilink = models.CharField(max_length=250 , default='notset')
    languge = models.CharField(max_length=99 , default='notset',help_text="from wikipedia page")

class gotypes(models.Model):
    name = models.CharField(max_length=90 , default='notset')
    wiki_link = models.CharField(max_length=250 , default='notset')
    icon = models.ImageField(upload_to ="resourses/", blank=True , null= True,help_text="flaticon 64*64")


class website(models.Model):
    URL = models.CharField(max_length=250 , default='notset')
    alexa = models.CharField(max_length=90 , default='notset')
    agancy_id = models.IntegerField(default=0)
    lastupdate = models.DateTimeField(auto_now=True)

class owner(models.Model):
    Pname = models.CharField(max_length=90 , default='notset')
    Ename = models.CharField(max_length=90 , default='notset')
    wiki_link = models.CharField(max_length=250 , default='notset')
    linkdin = models.CharField(max_length=250 , default='notset')
    education = models.CharField(max_length=200 , default='notset')
    homecountry = models.ForeignKey(country , on_delete=models.SET_NULL,null=True ,blank=True, related_name='ownercountry')

class baseagancy(models.Model):
    Pname = models.CharField(max_length=99 , default='notset')
    Ename = models.CharField(max_length=99 , default='notset')
    base_pname = models.CharField(max_length=30 , default = 'notset')
    base_ename = models.CharField(max_length = 30 , default = 'notset')
    country = models.ForeignKey(country , on_delete=models.CASCADE , related_name='country')
    logo = models.ImageField(upload_to = "resourses/",blank=True,null=True)
    google_map = models.CharField(max_length=250 , default='notset')
    address = models.CharField(max_length=250 , default = 'notset')
    website = models.ForeignKey(website , on_delete=models.SET_NULL,null=True ,blank=True , related_name='website')
    owner = models.ForeignKey(owner , on_delete=models.SET_NULL,null=True ,blank=True , related_name='owner')

class agancyprofile(models.Model):
    baseagancy = models.ForeignKey(baseagancy , on_delete=models.CASCADE , related_name='pagancy')
    companyvalid = models.BooleanField(default=False)
    companyvalid_link = models.CharField(max_length=250 , default='notset')
    parvanevalid = models.BooleanField(default=False)
    parvanevalid_link = models.CharField(max_length=250 , default='notset')
    iranold = models.IntegerField(default=-2)
    globalold = models.IntegerField(default=-2)

class agancycontact(models.Model):
    baseagancy = models.ForeignKey(baseagancy , on_delete=models.CASCADE , related_name='cagancy')
    instagram = models.CharField(max_length=250 , default='notset')
    telegram = models.CharField(max_length=250 , default='notset')
    facebook = models.CharField(max_length=250 , default='notset')
    twitter = models.CharField(max_length=250 , default='notset')
    linkdin = models.CharField(max_length=250 , default='notset')
    youtube = models.CharField(max_length=250 , default='notset')
    medium = models.CharField(max_length=250 , default='notset')
    virgool = models.CharField(max_length=250 , default='notset')
    email1 = models.CharField(max_length=250 , default='notset')
    email2 = models.CharField(max_length=250 , default='notset')


class shobe(models.Model):
    country = models.ForeignKey(country , on_delete=models.SET_NULL , null=True , related_name='shobecountry')
    agancy = models.ForeignKey(baseagancy , on_delete=models.SET_NULL , null=True , related_name='shobeagancy')
    googlemap = models.CharField(max_length=250 , default='notset')
    adress = models.CharField(max_length=200 , default='notset')
    tel1 = models.CharField(max_length=20 , default='notset')
    tel2 = models.CharField(max_length=20 , default='notset')
    tel3 = models.CharField(max_length=20 , default='notset')

class tels(models.Model):
    number = models.CharField(max_length=20 , default='notset')
    country = models.ForeignKey(country , on_delete=models.SET_NULL , null=True , related_name='telcountry')
    agancy = models.ForeignKey(baseagancy , on_delete=models.SET_NULL , null=True,related_name='telagancy')
    shobe = models.ForeignKey(shobe , on_delete=models.SET_NULL , null=True , related_name='telshobe')

class papers(models.Model):
    agancy = models.ManyToManyField(baseagancy , related_name='paperagancy' )
    country = models.ForeignKey(country , on_delete=models.SET_NULL , null=True)
    name = models.CharField(max_length=90 , default='notset')
    icon = models.ImageField(upload_to ="resourses/", blank=True , null= True)
    logo = models.ImageField(upload_to ="resourses/", blank=True , null= True)
    officiallink = models.CharField(max_length=250 , default='notset')
    wikilink = models.CharField(max_length=250 , default='notset')

class agVcu(models.Model):
    agancy = models.ForeignKey(baseagancy , on_delete=models.SET_NULL , null=True , related_name='agc')
    country = models.ForeignKey(country , on_delete=models.SET_NULL , null=True , related_name='cu')
    point = models.IntegerField( default= -1)

class agVgt(models.Model):
    agancy = models.ForeignKey(baseagancy , on_delete=models.SET_NULL , null=True , related_name='agg')
    gotype = models.ForeignKey(gotypes , on_delete=models.SET_NULL , null=True , related_name='gt')
    point = models.IntegerField( default= -1)


class point(models.Model):
    agancy = models.ForeignKey(baseagancy , on_delete=models.CASCADE , related_name='agancyofpoint')
    auth_point = models.CharField(max_length=7 , default='notset')
    old_point = models.CharField(max_length=7 , default='notset')
    destibute_point = models.CharField(max_length=7 , default='notset')
    manager_point = models.CharField(max_length=7 , default='notset')
    paper_point = models.CharField(max_length=7 , default='notset')
    country_point = models.CharField(max_length=7 , default='notset')
    total_point = models.CharField(max_length=7 , default='notset')
    updated_at = models.DateTimeField(auto_now=True)



