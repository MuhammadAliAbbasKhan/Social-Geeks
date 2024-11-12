from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# --------______________--------------______USER PROFILE MODEL_________---------------_______

class Profile (models.Model)  : 
    
    user =          models.OneToOneField(User , on_delete= models.CASCADE)
    follow =        models.ManyToManyField(
                                "self" , 
                                related_name="followed_by",     #"A query help to searcg nu later on "
                                symmetrical= False ,            #"if i  follow someone not necessart they follow me too"   
                                blank= True ,                   # it is not neccsary that i have to follow any body                                         
                                           
                                           ) 
    #   when was the last user modified his  profile
    date_modified  =  models.DateTimeField(  auto_now= True)    
    #    user profile image upload
    profile_image =  models.ImageField( null= True , blank= True , upload_to = "images/" )
    profile_bio=          models.CharField(max_length= 500  , null= True , blank= True)
    home_page_link     =  models.CharField(max_length= 100  , null= True , blank= True)
    facebook_link     =   models.CharField(max_length= 100  , null= True , blank= True)
    instagram_link    =   models.CharField(max_length= 100 , null= True , blank= True)
    linkedin_link    =    models.CharField(max_length= 100 , null= True , blank= True)
                                 
                                       
    def __str__(self):
        return self.user.username

            


# --------______________--------------______AUTOMATIC PROFILE MODEL_________---------------_______

# CREATE AN AUTOMATIC PROFILE WHEN USERS SIGNS UP

def Create_Profile (sender , instance , created , **kwargs)  : 
    if created  :  # Means If A User New Is Created
        user_profile =       Profile(user = instance)
        user_profile.save() 
        # have yourself automatically followed when a user is  created 
        user_profile.follow.add(user_profile)
        user_profile.save() 
        

post_save.connect(Create_Profile , sender= User  )



# --------______________--------------______GWEEK  MODEL_________---------------_______

class Gweek (models.Model)  : 
    
    
    user     =    models.ForeignKey(User , related_name="gweeks" ,on_delete= models.DO_NOTHING)
    body     =    models.CharField(max_length= 500 )
    created_at=   models.DateTimeField(auto_now_add=True )
    #  as a user keep track of likes 
    likes  =              models.ManyToManyField(User, blank= True , related_name="gweek_like")  
           
    #  keep track of count of likes
    def number_of_like (self) : 
        
        return self.likes.count()
        
        
    def __str__(self):
       
         return f'{self.user} ({self.created_at:%Y-%m-%d %H:%M}) : {self.body} ...'
   
       
        
        



