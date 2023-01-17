

function move(from, to) {
    let fromNode = document.getElementById(from)
    let toNode = document.getElementById(to)
    toNode.insertBefore(fromNode.firstElementChild, toNode.firstElementChild)
}

function move12() {
    move("first", "second");
}

function move13() {
    move("first", "third");
}

function move21() {
    move("second", "first");
}

function move23() {
    move("second", "third");
}

function move31() {
    move("third", "first");
}

function move32() {
    move("third", "second");
}


