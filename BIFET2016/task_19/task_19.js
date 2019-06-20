var list = [10, 3, 7, 12, 11, 30];

function renderList() {
  var listArea = document.getElementById('list-area');
  listArea.innerHTML = '';
  for (var i = 0; i < list.length; i++) {
    var d = document.createElement('div');
    d.setAttribute('class', 'list-item');
    d.setAttribute('title', list[i]);
    d.setAttribute('style', 'height: ' + list[i] * 10 + 'px');
    // d.innerText = list[i];
    listArea.appendChild(d);
  }
}

function listLeftPush() {
  if (list.length >= 60) {
    alert('队列元素个数达到最大值60');
    return;
  }
  var n = document.getElementById('num');
  var num = parseInt(n.value);
  if (num) {
    if (num < 10 || num > 100) {
      alert('请输入10到100间的数字');
      return;
    }
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
  if (list.length >= 60) {
    alert('队列元素个数达到最大值60');
    return;
  }
  var n = document.getElementById('num');
  var num = parseInt(n.value);
  if (num) {
    if (num < 10 || num > 100) {
      alert('请输入10到100间的数字');
      return;
    }
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

function listSort() {
  for (var j = list.length - 1; j > 0; j--) {
    for (var i = 0; i < j; i++) {
      if (list[i] > list[i + 1]) {
        var t = list[i];
        list[i] = list[i + 1];
        list[i + 1] = t;
      }
      renderList();
      alert('请点击继续');
    }
  }
}

function init() {
  document.getElementById('lpush').onclick = listLeftPush;
  document.getElementById('rpush').onclick = listRightPush;
  document.getElementById('lpop').onclick = listLeftPop;
  document.getElementById('rpop').onclick = listRightPop;
  document.getElementById('sort').onclick = listSort;
  renderList();
}

init();
