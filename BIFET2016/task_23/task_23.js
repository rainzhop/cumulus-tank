function traverse() {
  var order = [];
  var makeOrder = function (node) {
    if (!node) {
      return;
    }
    order.push(node);
    for (var i = 0; i < node.children.length; i++) {
      makeOrder(node.children[i])
    }
  };
  var root = document.getElementsByClassName('root')[0];
  makeOrder(root);
  return order;
}

function highlight(order, i, w) {
  var node = order[i];
  node.classList.add('highlight');
  var s = node.childNodes[0].textContent.trim();
  if (w != '' && s.includes(w)) {
    node.classList.remove('highlight');
    node.classList.add('found');
  }
  setTimeout(function () {
    node.classList.remove('highlight');
    i++;
    if (i != order.length) {
      highlight(order, i, w);
    }
  }, 500);
}

function ontraverse() {
  var order = traverse();
  highlight(order, 0, '');
}

function onsearch() {
  var w = document.getElementById('word').value;
  var order = traverse();
  highlight(order, 0, w);
}

function init() {
  document.getElementById('traverse').onclick = ontraverse;
  document.getElementById('search').onclick = onsearch;
}

init();
