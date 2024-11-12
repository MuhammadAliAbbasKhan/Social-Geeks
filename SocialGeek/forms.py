from django import forms
from .models import Gweek 
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm ,SetPasswordForm
from django.contrib.auth.models import User

from .models import Profile

# --------__________---------------GWEEK FORM----------__________-------------_________--------
class Gweek_Form (forms.ModelForm)  :  
    
    body =  forms.CharField(required= True  , widget=   forms.widgets.Textarea(attrs={"placeholder": "Write Your Gweeks Here !" , "class":"form-control" ,}) ,label=""   )

    class  Meta :
        model  = Gweek 
        exclude = ("user" , "likes" ,"profile_bio","home_page_link","facebook_link","instagram_link","linkedin_link", )  # this line is neccessary else the code gives an  error  it emoves gthe likes
        
        
        
# --------__________-------------SIGNUP FORM----------__________-------------_________--------
        


class SignUpForm(UserCreationForm):
    
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'



# --------______________--------------______PROFILE EXTRA FORM MODEL_________---------------_______

class ProfilePicForm (forms.ModelForm) : 
    
		profile_image = forms.ImageField(label = "Profile Picture")
		profile_bio = forms.CharField(label="", max_length=500, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tell Other Geeks About Yourself'}))
		home_page_link= forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Link to Home'}))
		facebook_link = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Facebook Profile Link'}))
		instagram_link = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Instagram Profile Link'}))
		linkedin_link = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Linkedin Profile Link'}))

		class Meta : 

			model = Profile
			fields = ("profile_image","profile_bio","home_page_link","facebook_link","instagram_link","linkedin_link",)
				
    
# --------______________--------------______USER PROFILE CHANGE FORM MODEL_________---------------_______
				
    
class  UserProfileChangeForm(UserChangeForm) : 

#  in user change form  password cannot  be changed   we have to that concept in another form
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	#  hide password stuff 
	password = None
 
	class Meta:
		model = User
		fields = ('username' , 'first_name' , 'last_name' , 'email' )

	def __init__(self, *args, **kwargs):
		super(UserProfileChangeForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
    
    
# --------______________--------------______Change Password FORM MODEL_________---------------_______
    
    
class  ChangePasswordForm(SetPasswordForm)   : 
	class Meta:
		model = User
		fields = ['new_password1' , 'new_password1'  ]

	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)


		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


    