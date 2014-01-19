# coding: utf-8

from flask import render_template, Blueprint, Markup


class Map(object):
    def __init__(self, identifier, lat, lng,
                 zoom=13, maptype="ROADMAP", drawingtype='point', markers=None,
                 varname='map',
                 style="height:300px;width:300px;margin:0;",
                 cls="map", strokecolor='#FF0000', strokeopacity=0.8, strokeweight=2, fillcolor='#FF0000', fillopacity=0.35):
        self.cls = cls
        self.style = style
        self.varname = varname
        self.center = (lat, lng)
        self.zoom = zoom
        self.maptype = maptype
        self.drawingtype = drawingtype
        self.strokecolor = strokecolor
        self.strokeopacity = strokeopacity
        self.strokeweight = strokeweight
        self.fillcolor = fillcolor
        self.fillopacity = fillopacity
        self.markers = markers or []
        self.identifier = identifier

    def __init__(self, point=None, zoom=13, maptype="SATELITE", varname="map",style="height:300px;width:300px;margin:0;", cls="map", markers=None, polygons=None):
        self.point = point,
        self.zoom = zoom,
        self.maptype = maptype,
        self.varname = varname,
        self.style = style,
        self.cls = cls,
        self.markers = markers,
        self.polygons = polygons

    def add_marker(self, identifier, latitude, longitude):
        self.markers.append(new Marker(identifier,new Point(latitude,longitude))

    def add_polygon(self, identifier, strokecolor, strokeopacity, strokeweight, fillcolor, fillopacity, markers): 
        self.polygons.append(new Polygon(identifier,stokecolor,strokeopacity,strokeweight,fillcolor,fillopacity,markers))

    #def add_marker(self, lat, lng):
    #    self.markers.append((lat, lng))

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
    def __init__(self, longitude, latitude, isDMS):
        self.longitude = longitude,
        self.latitude = latitude

class Point(object):
    def __init__(self, identifier, marker):
        self.identifier = identifier,
        self.marker = marker

class Polygon(object):
    def __init__(self, identifier, strokecolor, strokeopacity, strokeweight, fillcolor, fillopacity, markers):
        self.strokecolor = strokecolor,
        self.strokeopacity = stokeopacity,
        self.stokeweight = strokeweight,
        self.fillcolor = fillcolor,
        self.fillopacity = fillopacity,
        self.markers = self.markers

