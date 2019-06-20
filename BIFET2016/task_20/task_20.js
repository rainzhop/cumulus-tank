var list = ['10', '3', '7', '12', '11', '30'];

function renderList(pos = []) {
  var listArea = document.getElementById('list-area');
  listArea.innerHTML = '';
  for (var i = 0; i < list.length; i++) {
    var d = document.createElement('div');
    d.setAttribute('class', 'list-item');
    d.innerText = list[i];
    listArea.appendChild(d);
  }
  for (var i = 0; i < pos.length; i++) {
    var d = listArea.children[pos[i]] ;
    d.setAttribute('class', 'list-item marked');
  }
}

function listLeftPush() {
  var s = document.getElementById('input-area').value;
  inputs = s.split(/[^\w$]+/);
  list = inputs.concat(list);
  renderList();
}

function listRightPush() {
  var s = document.getElementById('input-area').value;
  inputs = s.split(/[^\w$]+/);
  list = list.concat(inputs);
  renderList();
}

function listLeftPop() {
  list.reverse();
  list.pop();
  list.reverse();
  renderList();
}

function listRightPop() {
  list.pop();
  renderList();
}

function query() {
  var s = document.getElementById('input-area').value;
  var pos = [];
  for (var i = 0; i < list.length; i++) {
    if (list[i].indexOf(s) != -1) {
      pos.push(i);
    }
  }
  renderList(pos);
}

function init() {
  document.getElementById('lpush').onclick = listLeftPush;
  document.getElementById('rpush').onclick = listRightPush;
  document.getElementById('lpop').onclick = listLeftPop;
  document.getElementById('rpop').onclick = listRightPop;
  document.getElementById('query').onclick = query;
  renderList();
}

init();
