//initialization function for the CodeMirror editor
//required for syntax highlighting
//more here: https://mr-coffee.net/blog/code-editor-django-admin
(function(){
    var $ = django.jQuery;
    $(document).ready(function(){
        $('textarea.python-editor').each(function(idx, el){
            CodeMirror.fromTextArea(el, {
                lineNumbers: true,
                mode: 'python',
                theme: 'monokai'
            });
        });
    });
})();