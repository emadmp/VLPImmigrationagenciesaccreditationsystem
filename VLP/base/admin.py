from django.contrib import admin
from .models import *
# Register your models here.

class countryadmin(admin.ModelAdmin):
    list_display=('Ename','Pname','mini_name','telcode','flag_icon','flag_imge','Continent','wikilink','languge')
admin.site.register(country,countryadmin)

class gotypesadmin(admin.ModelAdmin):
    list_display=('name','wiki_link','icon')
admin.site.register(gotypes,gotypesadmin)

class websiteadmin(admin.ModelAdmin):
    list_display=('URL','alexa','agancy_id' , 'lastupdate')
admin.site.register(website,websiteadmin)

class owneradmin(admin.ModelAdmin):
    list_display=('Pname','Ename','wiki_link' , 'linkdin' , 'education','homecountry')
admin.site.register(owner,owneradmin)

class baseagancyadmin(admin.ModelAdmin):
    list_display=('Pname','Ename','country' , 'logo' , 'google_map','address','website' , 'owner')
admin.site.register(baseagancy,baseagancyadmin)

class agancyprofileadmin(admin.ModelAdmin):
    list_display=('baseagancy','companyvalid','companyvalid_link' , 'parvanevalid' , 'parvanevalid_link','iranold','globalold')
admin.site.register(agancyprofile,agancyprofileadmin)

class agancycontactadmin(admin.ModelAdmin):
    list_display=('baseagancy','instagram','telegram' , 'facebook' , 'twitter','linkdin','youtube','medium','virgool','email1','email2')
admin.site.register(agancycontact,agancycontactadmin)

class shobeadmin(admin.ModelAdmin):
    list_display=('country','agancy','googlemap' , 'adress' , 'tel1','tel2','tel3')
admin.site.register(shobe,shobeadmin)

class telsadmin(admin.ModelAdmin):
    list_display=('number','country','agancy' , 'shobe')
admin.site.register(tels,telsadmin)

class papersadmin(admin.ModelAdmin):
    list_display=('country','name' , 'icon','logo','officiallink','wikilink')
admin.site.register(papers,papersadmin)

class agVcuadmin(admin.ModelAdmin):
    list_display=('agancy','country','point')
admin.site.register(agVcu,agVcuadmin)

class agVgtadmin(admin.ModelAdmin):
    list_display=('agancy','gotype','point')
admin.site.register(agVgt,agVgtadmin)
