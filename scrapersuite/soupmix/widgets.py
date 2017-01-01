from django import forms

class PythonEditor(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super(PythonEditor, self).__init__(*args, **kwargs)
        self.attrs['class'] = 'python-editor'

    class Media:
        css = {
            'all': (
                '/static/codemirror-5.9/codemirror.css',
                '/static/codemirror-5.9/theme/monokai.css',
                '/static/codemirror-5.9/theme/cm-custom.css',
            )
        }
        js = (
            '/static/codemirror-5.9/codemirror.js',
            '/static/codemirror-5.9/mode/python/python.js',
            '/static/codemirror-5.9/init.js'
        )