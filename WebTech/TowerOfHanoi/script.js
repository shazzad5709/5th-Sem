var top1 = 0;
var top2, top3 = 3;

function move12() {
    if(top1<4 || top2<4) {
        let l = document.getElementById('first');
    let node = document.getElementById('second');
    
    node.insertBefore(l.children[top1], node.children[top2]);
    l.insertBefore(node.children[top2], l.children[top1]);
    top1++;
    top2--;
    }
    
}