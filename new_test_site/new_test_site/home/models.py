from django.db import models,Field  
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import permalink

#temporary display until graphs and stuff can be added
class data(db.Model): 
	header = Field.db_column(db.Integer, primary_key=True)
	table = Field.db_tablespace(db.float, primary_key=True)  

	def __unicode__(self): 
		return '%s'%self.title 

	@permalink 
	def get_absolute_url(self): 
		return('view_data')

class display(models.Model): 
	title = models.CharField(max_length=20 
