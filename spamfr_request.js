//https://m.facebook.com/friends/center/requests/outgoing/#friends_center_main

var j = 0,
    cbt = document.getElementsByClassName("_54k8 _56bs _56bt"),
    sbt = document.getElementsByClassName("_54k8 _56bs _56bu");
setInterval(function () {
    for (var e = 0; e < cbt.length; e++) cbt[e].click();
    for (e = 0; e < sbt.length; e++) sbt[e].click();
    j++
}, 20000);
