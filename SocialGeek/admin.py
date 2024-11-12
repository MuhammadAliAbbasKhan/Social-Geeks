from django.contrib import admin
from .models import Profile , Gweek

# Register your models here.


#  in order to remove the    group  in admin section as we login and we see
# we  can do the following steps 
from django.contrib.auth.models import Group 
#   UNREGISTER THE GROUPS
admin.site.unregister(Group) 


#  MIX PROFILE INFO  INTO USER  INFO SO WE CAN SEE ALL IN ONE TABLE IN ADMIN 

class ProfileInLine (admin.StackedInline)  : 
        model   =  Profile 



#  now to remoove the unnecessary user model first name and last name we see we remove those 
from django.contrib.auth.models import User 
# REOMOVE THE UNNECCESSARY THINGS 
class UserAdmin (admin.ModelAdmin)  : 
    model  = User 
    #  Just display username field on  Admin Page 
    fields  =  ["username"]
    inlines =  [ProfileInLine]
    
    
    
#   UNREGISTER  INTIAL USERS
admin.site.unregister(User)
#   REREGIISTER INITIAL USERS
admin.site.register(User , UserAdmin)
# admin.site.register(Profile)




admin.site.register(Gweek)




