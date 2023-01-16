// let l = document.getElementById('list');
// let node = document.getElementById('list').lastElementChild;

// l.removeChild(l.lastElementChild);

// l.insertBefore(node, null);

let para1 = document.getElementById('p1');
let classname = para1.getAttribute('class');
let para2 = document.getElementById('p2');
para2.setAttribute('class', classname);