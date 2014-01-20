# coding: utf-8

from flask import render_template, Blueprint, Markup


class Map(object):

    def __init__(self, center, markers=None, polygons=None, zoom=13, maptype="SATELLITE", varname='map' ,style="height:300px;width:300px;margin:0;", cls="map"):
        self.center = center or Marker('47.12505','8.61546')
        self.markers = markers or []
        self.polygons = polygons or []
        self.zoom = zoom
        self.maptype = maptype
        self.varname = varname
        self.style = style
        self.cls = cls

    def add_marker(self, latitude, longitude):
        self.markers.append(Marker(latitude,longitude))

    def add_polygon(self, polygon):
        self.polygons.append(polygon)

    def render(self, *args, **kwargs):
        return render_template(*args, **kwargs)

    @property
    def js(self):
        return Markup(self.render('googlemaps/gmapjs.html', gmap=self))

    @property
    def html(self):
        return Markup(self.render('googlemaps/gmap.html', gmap=self))


def googlemap_obj(*args, **kwargs):
    map = Map(*args, **kwargs)
    return map


def googlemap(*args, **kwargs):
    map = googlemap_obj(*args, **kwargs)
    return Markup("".join((map.js, map.html)))


def googlemap_html(*args, **kwargs):
    return googlemap_obj(*args, **kwargs).html


def googlemap_js(*args, **kwargs):
    return googlemap_obj(*args, **kwargs).js


class GoogleMaps(object):
    def __init__(self, app=None, **kwargs):
        self.key = kwargs.get('key')
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.config['GOOGLEMAPS_KEY'] = self.key
        self.register_blueprint(app)
        app.add_template_filter(googlemap_html)
        app.add_template_filter(googlemap_js)
        app.add_template_global(googlemap_obj)
        app.add_template_filter(googlemap)
        app.add_template_global(googlemap)

    def register_blueprint(self, app):
        module = Blueprint("googlemaps", __name__,
                           template_folder="templates")
        app.register_blueprint(module)
        return module

class Marker(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class Polygon(object):
    def __init__(self, markers=None, strokecolor="#FF0000", strokeopacity=0.8, strokeweight=2, fillcolor="#FF0000", fillopacity=0.35):
        self.markers = markers or []
        self.strokecolor = strokecolor
        self.strokeopacity = strokeopacity
        self.strokeweight = strokeweight
        self.fillcolor = fillcolor
        self.fillopacity = fillopacity

    def add_marker(self, latitude, longitude):
        self.markers.append(Marker(latitude, longitude))


