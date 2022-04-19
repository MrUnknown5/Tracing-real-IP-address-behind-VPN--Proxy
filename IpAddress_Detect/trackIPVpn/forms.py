from ipaddress import ip_address
from django import forms

# creating a form
class GeeksForm(forms.Form):
	IP_Address = forms.GenericIPAddressField( )
