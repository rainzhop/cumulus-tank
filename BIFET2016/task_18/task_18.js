var list = [10, 3, 7, 12, 11, 30];

function renderList() {
  var listArea = document.getElementById('list-area');
  listArea.innerHTML = '';
  for (var i = 0; i < list.length; i++) {
    var d = document.createElement('div');
    d.setAttribute('class', 'list-item');
    d.innerText = list[i];
    listArea.appendChild(d);
  }
}

function listLeftPush() {
  var n = document.getElementById('num');
  var num = parseInt(n.value);
  if (num) {
    list.reverse();
    list.push(num);
    list.reverse();
  }
  else {
    alert('请输入一个整数！');
  }
  renderList();
}

function listRightPush() {
  var n = document.getElementById('num');
  var num = parseInt(n.value);
  if (num) {
    list.push(num);
  }
  else {
    alert('请输入一个整数！');
  }
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

function init() {
  document.getElementById('lpush').onclick = listLeftPush;
  document.getElementById('rpush').onclick = listRightPush;
  document.getElementById('lpop').onclick = listLeftPop;
  document.getElementById('rpop').onclick = listRightPop;
  renderList();
}

init();
