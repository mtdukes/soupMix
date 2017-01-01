from django.contrib import admin
from django import forms
from .models import *
from soupmix.widgets import PythonEditor
import ast

#activation for syntax highlighting
class ScraperAdminForm(forms.ModelForm):
    model = Scraper
    run_schedule = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        choices=Scraper.day_choices
    )
    #use super to retrieve and set display values of day choices
    def __init__(self, *args,**kwargs):
        super(ScraperAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            #if run schedule is None, you're just adding a scraper, so pass
            if self.instance.run_schedule is not None:
                day_values = tuple(ast.literal_eval(self.instance.run_schedule))
                self.initial['run_schedule'] = day_values

    class Meta:
        fields = '__all__'
        widgets = {
            'code_block': PythonEditor(attrs={'style': 'width: 90%; height: 100%;'}),
        }

class ScraperAdmin(admin.ModelAdmin):
    form = ScraperAdminForm
    list_display = ['name','slug','last_run', 'next_run','active']
    search_fields = ['name', 'slug']
    list_filter = ['last_run','next_run','active']
    readonly_fields = ('next_run','last_run','date_created',)

admin.site.register(Scraper,ScraperAdmin)
admin.site.register(DataFile)
