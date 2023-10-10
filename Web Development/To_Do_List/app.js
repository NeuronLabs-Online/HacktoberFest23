var list = document.getElementById("list");

function add() {
  var val = document.getElementById("val");
  var li = document.createElement("li");
  var text = document.createTextNode(val.value);
  li.appendChild(text);

  var delbtn = document.createElement("button");
  var deltext = document.createTextNode("delete");
  delbtn.setAttribute("class", "parents");
  delbtn.setAttribute("onclick", "btnDelete(this)");
  delbtn.appendChild(deltext);
  li.appendChild(delbtn);

  var editbtn = document.createElement("button");
  var edittext = document.createTextNode("Edit");
  editbtn.setAttribute("class", "parents");
  editbtn.setAttribute("onclick", "btnEdit(this)");
  editbtn.appendChild(edittext);
  li.appendChild(editbtn);

  list.appendChild(li);
  val.value = "";
}

function btnDelete(e) {
  e.parentNode.remove();
}

function btnEdit(e) {
  var edit = prompt("Enter updated value", e.parentNode.firstChild.nodeValue);
  e.parentNode.firstChild.nodeValue = edit;
}

function deleteAll() {
  list.innerHTML = "";
}