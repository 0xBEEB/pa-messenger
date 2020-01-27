import flask
from flask import url_for, redirect, render_template


def twiml(resp):
    resp = flask.Response(str(resp))
    resp.headers['Content-Type'] = 'text/xml'
    return resp


def view(view_name, form=None, params=None):
    if form is None and params is None:
        return render_template("{0}.html".format(view_name))
    elif form is None and params is not None:
        return render_template("{0}.html".format(view_name), params=params)
    elif form is not None and params is None:
        return render_template("{0}.html".format(view_name), form=form)
    else:
        return render_template("{0}.html".format(view_name), form=form, params=params)


def redirect_to(view_name, **options):
    if len(options) == 0:
        return redirect(url_for(view_name))
    return redirect(url_for(view_name, **options))
