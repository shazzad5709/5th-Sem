let btnlist = ['1', '2', '3', '4'];
shuffle(btnlist);
const start = document.getElementById("first");

function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
    while (currentIndex != 0) {

        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        [array[currentIndex], array[randomIndex]] = [
            array[randomIndex], array[currentIndex]];
    }
  
    return array;
  }

function startNewGame() {
    for(let i=0; i<4; i++) {
        start.insertAdjacentHTML("afterend", '<button type="button" class="btn btn-light cb">' + btnlist[i] +'</button>');
    }
}

function move(from, to) {
    let fromNode = document.getElementById(from);
    let toNode = document.getElementById(to);
    toNode.insertBefore(fromNode.firstElementChild, toNode.firstElementChild);
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



