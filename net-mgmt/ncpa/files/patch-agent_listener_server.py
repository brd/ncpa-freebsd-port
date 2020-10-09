--- agent/listener/server.py.orig	2020-09-09 15:50:23 UTC
+++ agent/listener/server.py
@@ -28,8 +28,8 @@ __STARTED__ = datetime.datetime.now()
 __INTERNAL__ = False
 
 base_dir = os.path.dirname(sys.path[0])
+base_dir = base_dir + '/ncpa'
 
-
 # The following if statement is a workaround that is allowing us to run this
 # in debug mode, rather than a hard coded location.
 
@@ -948,7 +948,7 @@ def api(accessor=''):
         value = node.walk(**sane_args)
 
     # Generate page and add cross-domain loading
-    json_data = json.dumps(dict(value), ensure_ascii=False, indent=None if request.is_xhr else 4)
+    json_data = json.dumps(dict(value), ensure_ascii=False, indent=None if request.accept_mimetypes.accept_json else 4)
     response = Response(json_data, mimetype='application/json')
     response.headers['Access-Control-Allow-Origin'] = '*'
     return response
