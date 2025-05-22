const Applet = imports.ui.applet;
const GLib = imports.gi.GLib;
const Mainloop = imports.mainloop;
const ByteArray = imports.byteArray;

class MyApplet extends Applet.TextApplet {
    constructor(metadata, orientation, panelHeight, instanceId) {
        super(orientation, panelHeight, instanceId);

        global.log("Chinese Lunar Applet loaded");
        this.set_applet_label("Loading...");

        this.refresh();
    }

    refresh() {
        try {
            let [success, stdout, stderr, exit_status] = GLib.spawn_sync(
                null,
                ["/usr/bin/python3", "/home/n1/.local/share/cinnamon/applets/chinese-lunar@n1/chinese_lunar.py"],
                null,
                GLib.SpawnFlags.SEARCH_PATH,
                null
            );

            if (!success || exit_status !== 0) {
                global.log(`Chinese Lunar Applet: spawn_sync failed or exit_status=${exit_status}`);
                if (stderr.length > 0) {
                    global.log("stderr: " + ByteArray.toString(stderr));
                }
                this.set_applet_label("Script Error");
                return;
            }

            let output = ByteArray.toString(stdout).trim();
            global.log("Chinese Lunar Applet Output: " + output);

            this.set_applet_label(output.length > 0 ? output : "No Output");

        } catch (e) {
            global.log("Chinese Lunar Applet Exception: " + e.message);
            this.set_applet_label("JS Error");
        }

        // Refresh once per day (86400 seconds)
        Mainloop.timeout_add_seconds(86400, () => {
            this.refresh();
            return true;
        });
    }
}

function main(metadata, orientation, panelHeight, instanceId) {
    return new MyApplet(metadata, orientation, panelHeight, instanceId);
}

