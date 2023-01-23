let stackA = [1, 2, 3, 4];
let stackB = [];
let stackC = [];

// Shuffle the elements in stackA
stackA = shuffle(stackA);

// Display the initial state of the stacks
displayStacks();

// Add event listeners for clicking on the stacks
// let stacks = document.querySelectorAll("#stackA, #stackB, #stackC");
// stacks.forEach(stack => stack.addEventListener("click", moveBox));

// Add event listener for reset button
document.querySelector("#reset").addEventListener("click", reset);

function moveAtoB() {
    if (stackA.length > 0) {
      let box = stackA.pop();
      stackB.push(box);
      displayStacks();
    }
  }
  
  // Move box from stackA to stackC function
  function moveAtoC() {
    if (stackA.length > 0) {
      let box = stackA.pop();
      stackC.push(box);
      displayStacks();
    }
  }
  
  // Move box from stackB to stackA function
  function moveBtoA() {
    if (stackB.length > 0) {
      let box = stackB.pop();
      stackA.push(box);
      displayStacks();
    }
  }
  
  // Move box from stackB to stackC function
  function moveBtoC() {
    if (stackB.length > 0) {
      let box = stackB.pop();
      stackC.push(box);
      displayStacks();
    }
  }
  
  // Move box from stackC to stackA function
  function moveCtoA() {
    if (stackC.length > 0) {
      let box = stackC.pop();
      stackA.push(box);
      displayStacks();
    }
  }
  
  // Move box from stackC to stackB function
  function moveCtoB() {
    if (stackC.length > 0) {
      let box = stackC.pop();
      stackB.push(box);
      displayStacks();
    }
  }

function displayStacks() {
    let stackADiv = document.querySelector("#stackA");
    let stackBDiv = document.querySelector("#stackB");
    let stackCDiv = document.querySelector("#stackC");
    stackADiv.innerHTML = "";
    stackBDiv.innerHTML = "";
    stackCDiv.innerHTML = "";
    for (let i = stackA.length - 1; i >= 0; i--) {
        let box = document.createElement("div");
        box.classList.add("box");
        box.classList.add("row");
        box.innerHTML = stackA[i];
        stackADiv.appendChild(box);
    }
    for (let i = stackB.length - 1; i >= 0; i--) {
        let box = document.createElement("div");
        box.classList.add("box");
        box.classList.add("row");
        box.innerHTML = stackB[i];
        stackBDiv.appendChild(box);
    }
    for (let i = stackC.length - 1; i >= 0; i--) {
        let box = document.createElement("div");
        box.classList.add("box");
        box.classList.add("row");
        box.innerHTML = stackC[i];
        stackCDiv.appendChild(box);
    }
}

function checkWin() {
    if ((stackB.length === 4 && stackB.join("") === "4321") 
        || (stackC.length === 4 && stackC.join("") === "4321")) {
        alert("You won!");
        reset();
    }
}

function reset() {
    stackA = [1, 2, 3, 4];
    stackB = [];
    stackC = [];
    stackA = shuffle(stackA);
    displayStacks();
}

function shuffle(array) {
    let currentIndex = array.length, temporaryValue, randomIndex;
    while (0 !== currentIndex) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }
    return array;
}
