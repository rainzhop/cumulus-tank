function traverse() {
  var order = [];
  var makeOrder = function (node) {
    if (!node) {
      return;
    }
    order.push(node);
    makeOrder(node.children[0]);
    makeOrder(node.children[1]);
  };
  var root = document.getElementsByClassName('root')[0];
  makeOrder(root);
  highlight(order, 0);
}

function highlight(order, i) {
  var node = order[i];
  node.classList.add('highlight');
  setTimeout(function () {
    node.classList.remove('highlight');
    i++;
    if (i != order.length) {
      highlight(order, i);
    }
  }, 500);
}

function init() {
  document.getElementById('traverse').onclick = traverse;
}

init();
