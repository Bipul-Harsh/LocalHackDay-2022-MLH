function increase_border(){
    var elem = document.getElementById("button");
    var value = elem.style.border;
    var update_value = "";
    console.log(parseInt(value.substring(0, value.indexOf("p"))));
    if (value == "")
        update_value = "1px solid black";
    else
        update_value = (parseInt(value.substring(0, value.indexOf("p"))) + 5) + "px solid black";
    elem.style.border = update_value;
}