from django import forms

#this is the normal function
def start_with_a(value):
    if value[0].lower()=='a': #if it starts with a then it cannot allow
        raise forms.ValidationError('it cannot start with a')
#This is the normal function
def len_with_g_4(value):
    if len(str(value))<4: #it thows an error if name having less then 4 characters
        raise forms.ValidationError('the length is highter')


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[start_with_a,len_with_g_4])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    #bot catcher is the element which is present in sorce code cannot display in th front-end


    def clean(self):   #it is automatically called after the calling validators
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        a=self.cleaned_data['age']
        if e!=r: #if re-ented email and email is not same it will raise an error
            raise forms.ValidationError('both or not same')
        if a<18: #if age less then 18 then it will raise an error
            raise forms.ValidationError('the age is grater')


    def clean_botcatcher(self):  #it will restrict the data which is accessed by the  the botcatcher(data enterd by hackers)
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('the data field is ')

