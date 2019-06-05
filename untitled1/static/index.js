function getMoreContents() {
    var keyword = document.getElementById("keyword").value;
    if (keyword == "") {
        clearContent();
        return;
    } else {
        var ajax = new XMLHttpRequest();
        var url = "search?s=" + keyword;
        ajax.open("GET", url, true);
        ajax.send(null);
        ajax.onreadystatechange = function() {
            if (ajax.readyState == 4) {
                if (ajax.status == 200) {
                    var result = ajax.responseText;
                    insertContent(result);
                }
            }
        }
    }
}
function insertContent(content) {
    clearContent();
    setLocation();
    var json = JSON.parse(content);

    //console.log(json);
    var len = json.length;
    //console.log('长度为:'+len);

    for (var i = 0; i < len; i++) {
        var value = json[i];
        //console.log(value);
        var tr = document.createElement("tr");
        var td = document.createElement("td");
        td.setAttribute("bgcolor", "#FFFAFA");
        td.setAttribute("border", "0");
        td.onmouseover = function() {
            this.className = 'mouseOver';
        };
        td.onmouseout = function() {
            this.className = 'mouseOut';
        };
        //td.onclick = function() {
        //    document.getElementById("keyword").value=value;
        //    alert(value);
        //};
        var h = document.createElement('em');
        var text = document.createTextNode(value);
        //console.log(text);
        td.appendChild(text);
        tr.appendChild(td);
        document.getElementById("content_table_body").appendChild(tr);

    }
    $('td').click(function(){
        alert($(self.text()))

    })
}

function clearContent() {
    var popNode = document.getElementById("popDiv");
    popNode.style.border = "none";
    var contentNode = document.getElementById("content_table_body");
    var len = contentNode.childNodes.length;
    for (var i = len - 1; i >= 0; i--) {
        contentNode.removeChild(contentNode.childNodes[i]);
    }
}
function setLocation(){
    var inputNode = document.getElementById("keyword");
    var width = inputNode.offsetWidth;
    var left = inputNode["offsetLeft"];
    var top = inputNode.offsetHeight+inputNode["offsetTop"];
    var popNode = document.getElementById("popDiv");
    popNode.style.border = "gray 0.5px solid";
    popNode.style.width = width+"px";
    popNode.style.top = top+"px";
    popNode.style.left = left+"px";
    document.getElementById("content_table").style.width=width+"px";

}