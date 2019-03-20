Java.perform(function () {
    var Activity = Java.use("android.app.Activity");
    Activity.onResume.implementation = function () {
        send("onResume() " + this);
        this.onResume();
        
        // dump view instance
        // Java.choose("android.view.View", {
        //     "onMatch": function(instance){
        //         send("findView () " + instance);
        //     },
        //     "onComplete":function() {
        //         send("completed!");
        //     }
        // })
    };

    var WebView = Java.use("android.webkit.WebView");
    WebView.loadUrl.overload("java.lang.String").implementation = function (s) {
        send(s.toString());
        this.loadUrl.overload("java.lang.String").call(this, s);
    };
});