from django import forms
class Register_modelform(forms.modelform):
	class Meta:
		model = Register
		fields = "__all__"