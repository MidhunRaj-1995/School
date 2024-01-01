from django import forms
class Register(forms.Form):
    name        =   forms.CharField(max_length=250)
    dob         =   forms.DateField()
    age         =   forms.IntegerField()
    gender      =   forms.CharField(max_length=250)
    phone       =   forms.CharField(max_length=250)
    mail_id     =   forms.EmailField()
    department_choices = [
        ('commerce', 'Commerce'),
        ('science', 'Science'),
        # Add other department choices as needed
    ]

    course_choices = {
        'commerce': [
            ('BBA', 'BBA'),
            ('BCOM', 'BCOM'),
            ('BCA', 'BCA'),
            ('economics', 'Economics'),
        ],
        'science': [
            ('physics', 'Physics'),
            ('chemistry', 'Chemistry'),
            ('zoology', 'Zoology'),
            ('botany', 'Botany'),
        ],
        # Add other department-course mappings as needed
    }

    department = forms.ChoiceField(choices=department_choices)
    course = forms.ChoiceField(choices=[], required=False)







