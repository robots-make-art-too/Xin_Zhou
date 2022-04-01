function post(){
    var newli = document.createElement("li");
    var ul = document.getElementById("postul");
    ul.insertBefore(newli,ul.firstChild);

    var newdiv = document.createElement("div");
    newli.appendChild(newdiv);

    var hi = document.createElement("h1");
    newli.appendChild(hi);

    var name = document.getElementById("title");
    hi.innerText = name.value;

    var newp = document.createElement("p");
    newli.appendChild(newp);

    var ban = document.getElementById("sec");
    var cont = document.getElementById("content");
    newp.innerText = ban.value + ": " + cont.value;

    var span = document.createElement("span");
    newp.appendChild(span);

    span.style.marginLeft = "400px";
}