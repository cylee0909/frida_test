Java.perform(function () {
    var Activity = Java.use("android.app.Activity");
    Activity.onResume.implementation = function () {
        send("onResume() " + this);
        this.onResume();
        
        Java.choose("android.view.View", {
            "onMatch": function(instance){
                send("findView () " + instance);
            },
            "onComplete":function() {
                send("completed!");
            }
        })
    };
});