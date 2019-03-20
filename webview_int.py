import frida, sys
# package_name = "com.fenbi.android.solar"
package_name = 12234

def get_messages_from_js(message, data):
    print(message)


def hook_log_on_resume():

    if (len(sys.argv) > 1):
        file_object = open(sys.argv[1], 'r')
        try:
            all_the_text = file_object.read()
            return all_the_text
        finally:
            file_object.close()
    
    hook_code = """
    
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

    """
    return hook_code


def main():
    process = frida.get_device_manager().enumerate_devices()[-1].attach(package_name)
    script = process.create_script(hook_log_on_resume())
    script.on('message', get_messages_from_js)
    script.load()
    sys.stdin.read()


if __name__ == '__main__':
    main()