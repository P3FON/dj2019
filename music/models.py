from django.db import models

# Create your models here.


"""
Create some model(s) in the <app>/models.py file
    typical fields:
        models.CharField(max_length=<n>)
        models.BooleanField(verbose_name=<verbose name>, 
		    		        choices=<choices_list>, 
		    		        default=<choice from choices_list>,
		    		        ...)
        models.DateField(null=True, blank=True)
        models.TimeField(null=True, blank=True,
		    		     default=datetime.time(hour=<int>, minute=<int>, second=<int>))
        models.ForeignKey(<AnotherModel>,
		                  on_delete=models.SET_NULL,	# CASCADE, SET_DEFAULT,…
		                  null=True, 
		                  blank=True)
        ...
	typical methods:
	    __str__()
        get_absolute_url()		# return reverse('<model>-detail', args=[str(self.id)])
        ...
Register each model in <app>.admin.py with a separate line like:
    admin.site.register(<Model>)
Run:
    manage.py@<project_site>  > makemigrations <app>
Run:
    manage.py@<project_site>  > migrate
in order to create those model tables in your database
Run another cycle of change models - makemigrations - migrate whenever you make changes to your model(s) / database
Run (optionally):
    manage.py@<project_site>  > sqlmigrate <app> <migration number> 
    (e.g., manage.py@polls_site  > sqlmigrate polls 0001) 
to see the SQL equivalent of a specific migration
"""


class Festival(models.Model):
    """The model class describing the concept of a festival.
    It includes a name, location and the start and end dates.
    """

    def __str__(self):
        pass

    def get_absolute_url(self):
        """Returns the URL to access a particular festival instance.
        Enables specific Festival pages in admin to include "View on site" button.
        """


class Performer(models.Model):
    """The model class describing the concept of performer.
    It is assumed that a performer is sufficiently described by their
    name and whether they are a solo performer or a band.
    """

    def __str__(self):
        pass

    def get_absolute_url(self):
        """Returns the URL to access a particular performer instance.
        Enables specific Performer pages in admin to include "View on site" button.
        """


