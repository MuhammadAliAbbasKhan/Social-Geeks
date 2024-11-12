from django.shortcuts import render ,redirect  ,get_object_or_404   
from .models  import Profile 
from django.contrib import messages
from .models import Gweek 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


from .forms import Gweek_Form ,SignUpForm ,ProfilePicForm
from .forms import SignUpForm , UserProfileChangeForm , ChangePasswordForm 

def home_page (request )  : 

     if request.user.is_authenticated : 
          form    =  Gweek_Form(request.POST or None )
          if request.method == "POST" : 
               if form.is_valid() : 
                    gweek  = form.save(commit= False)
                    gweek.user  =  request.user 
                    gweek.save() 
                    messages.success(request , ("You Gweek Has Been Posted ! "))
                    return redirect ('home_page')
          gweeks  =  Gweek.objects.all().order_by("-created_at")
          return render(request , "home_page.html",  {'gweeks': gweeks, 'form': form})
     
     else : 
          gweeks  =  Gweek.objects.all().order_by("-created_at")
          return render(request , "home_page.html",  {'gweeks': gweeks})
     
def profile_list (request)  : 
     
     # if  user is logged in 
     if request.user.is_authenticated : 
          #  display all the profiles but exclude my profile so i donot see mine 
          profiles  =   Profile.objects.exclude(user =  request.user)
          #  total gweek likes 
          total_gweek_likes  =  Gweek.objects.all().order_by("-created_at")

          return render(request , "profile_list.html",  {"profiles" : profiles, "total_gweek_likes": total_gweek_likes})
     
     else: 
          messages.error(request , ("Oops , You Must Be Logged in To See Others Profile "))
          return redirect ('home_page')
     

def profile (request , pk) : 
     
     #  is user id logged in 
     if  request.user.is_authenticated : 
          
          profile   =  Profile.objects.get(user_id=pk)
          #  follow and unfoolow concept 
          if request.method == "POST"  : 
               #  Get the Current User 
               current_user_profile =  request.user.profile 
               #  Get the form data 
               action =   request.POST["follow"]
               if action == "unfollow"  : 
                      current_user_profile.follow.remove(profile)
               elif action == "follow" : 
                      current_user_profile.follow.add(profile)
               else : 
                    pass
               #  SAVE THE PROFILE
               current_user_profile.save()
          
          gweeks  =   Gweek.objects.filter(user_id  = pk).order_by("-created_at") 
               
          return render( request , "profile.html",  {"profile" : profile , "gweeks":gweeks})
     
     else: 
          messages.error(request , ("Oops , You Must Be Logged in To See Others Profile "))
          return redirect ('home_page')


def followers (request , pk )  :  
      
     # if  user is logged in 
     if request.user.is_authenticated : 
          # only  a request.user can see his followers and not others followes 
          if request.user.id == pk : 
               #  display all the profiles but exclude my profile so i donot see mine 
               profiles  =   Profile.objects.get(id  = pk )
          #  total gweek likes 
               return render(request , "followers.html",  {"profiles" : profiles, })
               
          else: 
               messages.error(request , ("Oops , You Can Not See Others Geeks Following List "))
               return redirect ('home_page')
     
     
     else: 
          messages.error(request , ("Oops , You Must Be Logged in To Access This Page ! "))
          return redirect ('home_page')
           
    
    
def following (request , pk )  :  
      
     # if  user is logged in 
     if request.user.is_authenticated : 
          # only  a request.user can see his followers and not others followes 
          if request.user.id == pk : 
               #  display all the profiles but exclude my profile so i donot see mine 
               profiles  =   Profile.objects.get(id  = pk )
          #  total gweek likes 
               return render(request , "following.html",  {"profiles" : profiles, })
               
          else: 
               messages.error(request , ("Oops , You Can Not See Others Geeks Following List "))
               return redirect ('home_page')
     
     
     else: 
          messages.error(request , ("Oops , You Must Be Logged in To Access This Page ! "))
          return redirect ('home_page')
    
    
          
def login_user (request) : 

     if request.method == "POST"  : 
          username  =    request.POST["username"]
          userpassword = request.POST["userpassword"]
          
          user =  authenticate(request , username =  username , password = userpassword)
          if user is not None : 
               login(request , user)  
               messages.success(request , ("You Are Logged in Social Geek !"))
               return  redirect ("home_page")
          else : 
               messages.error(request , ("Oops, Wrong Credentials or  must be Signup !"))
               return  redirect ("login_user")
               
     return render( request , "login_user.html",  { })



def logout_user (request) : 


          logout(request)
          messages.success(request , ("You are Logged out . !"))
          return  redirect ("home_page")
     
     
def register_user (request)  : 
     
     # when they only visit the page
     form =  SignUpForm() 
     #  when they actually  register
     if request.method == "POST"  :
               form = SignUpForm(request.POST)
               if form.is_valid () : 
                    form.save()
                    # then clear the data 
                    username =           form.cleaned_data["username"]
                    email =              form.cleaned_data["email"]
                    first_name = form.cleaned_data["first_name"]
                    last_name = form.cleaned_data["last_name"]
                    password = form.cleaned_data["password1"]
                    # then login the user 
                    user = authenticate(username = username , password = password)
                    login(request , user )
                    messages.success(request , ("Welcome , You Now A Social Geek "))
                    return redirect ("home_page")
     
     return render (request , "register_user.html" , {"form": form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user=current_user)

        update_form = UserProfileChangeForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)

        if request.method == 'POST':  
            if update_form.is_valid() and profile_form.is_valid():
                update_form.save()
                profile_form.save()
                login(request, current_user)
                messages.success(request, "Your Geek Profile has been updated.")
                return redirect("home_page")
            else:
                print(update_form.errors)
                print(profile_form.errors)

        return render(request, "update_user.html", {'update_form': update_form, 'profile_form': profile_form})

    else:
        messages.error(request, "You must be logged in to access this page.")
        return redirect("home_page")

# def update_user(request):
#      if request.user.is_authenticated:
#           #  USE id when  there is a model 
#           current_user = User.objects.get(id=request.user.id)
#           #  USE user__id when  the  model  is assocciated with another model
#           profile_user = User.objects.get(   id = request.user.id)
#           #  Get THe Forms 
#           update_form = UserProfileChangeForm(request.POST or None, request.FILES or None , instance=current_user)
#           profile_form= ProfilePicForm(request.POST or None , request.FILES or None ,instance= profile_user)
          
#           if request.method == 'POST':  # Handle the form submission
          
#                if update_form.is_valid() and  profile_form.is_valid() :
#                     update_form.save()
#                     profile_form.save()
#                     # Log the user in again after updating their details
#                     login(request, current_user )
#                     messages.success(request, "Your Geek Profile has been updated.")
#                     return redirect("home_page")  # Redirect to the profile page after updating
#           else:
#                update_form = UserProfileChangeForm(instance=current_user)  # Load the form for GET request

#           return render(request, "update_user.html", {'update_form': update_form , "profile_form":profile_form})
          
#      else:
#           messages.error(request, "You must be logged in to access this page.")
#           return redirect("home_page")
     
     
          
def update_password(request)  : 
     
          if request.user.is_authenticated : 
                current_user = request.user 
                if request.method == 'POST' : 
                         update_password_form = ChangePasswordForm(current_user , request.POST)
                         #  Is the Form Valid 
                         if update_password_form.is_valid() :
                                update_password_form.save()
                                messages.success(request , ("You Password has been Changed ! "))
                              #   login (request , current_user)
                                return redirect ('home_page')
                         else : 
                                   for  error in  list(update_password_form.errors.values())   : 
                                             messages.error(request , error)
                                             return redirect ("update_password")
                else :
                    update_password_form  = ChangePasswordForm(current_user)
                    return render (request , "update_password.html" , {'update_password_form':update_password_form})
          else : 
                    messages.success(request , ("You Must Been Logged In To Access This Page!"))
                    return render (request , "register_user.html" , {})

               

          return render (request , "update_password.html" , {})
     
     


def gweek_like (request , pk ) : 
          
     if request.user.is_authenticated : 
          gweek =  get_object_or_404(Gweek , id = pk)
          # if already liked 
          if gweek.likes.filter(id = request.user.id) : 
               gweek.likes.remove(request.user)  
               
          else : 
               gweek.likes.add(request.user)    
          return redirect (request.META.get('HTTP_REFERER')) 
                                    
     else : 
          messages.error(request , ("You Must Been Logged In To Access This Page!"))
          return render (request , "register_user.html" , {})




def show_gweek (request , pk) :  
     
     gweek =  get_object_or_404 (Gweek , id = pk )
     
     if gweek : 
          return render (request , "show_gweek.html" ,  {"gweek": gweek}) 
     else : 
          messages.error(request , ("The Gweek Doesnot Exists !"))
          return redirect ("home_page") 




def unfollow (request , pk ) :  
     
     if request.user.is_authenticated : 
          #  get the profile to   unfollow 
          profile =   Profile.objects.get(id = pk)
          #  Unfollow The User  from our id  We are  request.user.id 
          request.user.profile.follow.remove(profile)
          #  save our profile 
          request.user.profile.save()
          
          messages.success(request , (f'You have unfollowed {profile.user.username}'))
          return redirect (request.META.get('HTTP_REFERER')) 
           
                                    
     else : 
          messages.error(request , ("You Must Been Logged In To Access This Page!"))
          return render (request , "register_user.html" , {})



def follow (request , pk ) :  
     
     if request.user.is_authenticated : 
          #  get the profile to   unfollow 
          profile =   Profile.objects.get(id = pk)
          #  Unfollow The User  from our id  We are  request.user.id 
          request.user.profile.follow.add(profile)
          #  save our profile 
          request.user.profile.save()
          
          messages.success(request , (f'You are now following {profile.user.username}'))
          return redirect (request.META.get('HTTP_REFERER')) 
           
                                    
     else : 
          messages.error(request , ("You Must Been Logged In To Access This Page!"))
          return render (request , "register_user.html" , {})






def delete_gweek(request, pk):
    if request.user.is_authenticated:
        gweek = get_object_or_404(Gweek, id=pk)
        if request.user.username == gweek.user.username:
            gweek.delete()
            messages.success(request, f'Your Gweek has been deleted {gweek.user.username}')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "You are trying to access someone else's Gweek!")
            return redirect("home_page")
    else:
        messages.error(request, "You must be logged in to perform this action!")
        return render(request, "register_user.html", {})
   
   
def search(request):
    if request.method == "POST":
        search_term = request.POST["searched"]
        searched_results = Gweek.objects.filter(body__contains=search_term)
        return render(request, "search.html", {"searched": searched_results})
    else:
        return render(request, "search.html", {})



def search_user(request):
    if request.method == "POST":
        # Get data from the form
        search_term = request.POST.get("searched", "")
        # Search it in the database
        searched_users = User.objects.filter(username__icontains=search_term)
        
        return render(request, "search_user.html", {"searched": searched_users, "search_term": search_term})
    else:
        return render(request, "search_user.html", {})
