"use strict"

class Notifier {
    successMsg(msg, time) {
        Materialize.toast(msg, time, "notifier-success");
    }
    errorMsg(msg, time) {
        Materialize.toast(msg, time, "notifier-error");
    }
    warningMsg(msg, time) {
        Materialize.toast(msg, time, "notifier-warning");
    }
}