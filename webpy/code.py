##code.py

import web,os
from web import form

render = web.template.render("E:\Private Doc\code\webpy\\templates")

urls = (
    '/', 'index',

)
app = web.application(urls, globals())
login = form.Form(
    form.Textbox('username'),
    form.Password('password'),
    form.Password('password_again'),


    form.Button('Login'),
    form.Checkbox('YES'),
    form.Checkbox('NO'),
    form.Textarea('moe'),
    form.Dropdown('SEX', ['man','woman']),
    form.Radio('time', ['2012-01-01', '20120101']),
    validators = [form.Validator("Password didn't match.",lambda i:i.password == i.password_again)]

)


class index:

    def GET(self):
        f=login()
        return render.formtest(f)
    def POST(self):
        f=login()
        if not f.validates():
            return render.formtest(f)

        else:
            return "HAHA!"

if __name__ == "__main__":
    web.internalerror = web.debugerror

    app.run()
