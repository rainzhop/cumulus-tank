var tags = [];

function delTag(e) {
  var idx = tags.indexOf(e.target.innerText);
  tags.splice(idx, 1);
  renderTags();
}

function renderTags() {
  var tagsArea = document.getElementById('tags-area');
  tagsArea.innerText = "";
  for (var i = 0; i < tags.length; i++) {
    var d = document.createElement('div');
    d.setAttribute('class', 'list-item');
    d.innerText = tags[i];
    tagsArea.appendChild(d);
    d.onclick = delTag;
  }
}

function addTag(e) {
  if (tags.length == 10) {
    return;
  }
  var keycode = e.keyCode;
  if (keycode == 13 || keycode == 32 || keycode == 188 ||　keycode == 229) {
    var v = e.target.value.trim();
    e.target.value = "";
    if (tags.includes(v) || v == "") {
      return;
    }
    tags.push(v);
    renderTags();
  }
}

var hobbys = []

function renderHobbys() {
  var hobbysArea = document.getElementById('hobbys-area');
  hobbysArea.innerText = "";
  for (var i = 0; i < hobbys.length; i++) {
    var d = document.createElement('div');
    d.setAttribute('class', 'hobby-item');
    d.innerText = hobbys[i];
    hobbysArea.appendChild(d);
  }
}

function addHobby() {
  var s = document.getElementById('hobby-input').value;
  inputs = s.split(/[^\w$]+/);
  document.getElementById('hobby-input').value = "";
  for (var i = 0; i < inputs.length; i++) {
    if (hobbys.includes(inputs[i]) || inputs[i] == "") {
      continue;
    }
    hobbys.push(inputs[i]);
  }
  hobbys = hobbys.slice(-10);
  renderHobbys();
}

function init() {
  document.getElementById('tag-input-area').onkeydown = addTag;
  document.getElementById('confirm-hobby').onclick = addHobby;
}

init();
