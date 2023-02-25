function toggleDiv() {
    const div1 = document.getElementById("div1");
    
    div1.remove();

    let outerDiv = document.createElement("div");
    outerDiv.className = "container";
    
    let childDiv1 = document.createElement("div");
    childDiv1.className = "box";
    childDiv1.textContent = "<?php echo (\"<p>Name<p>\"); ?>";

    let childDiv2 = document.createElement("div");
    childDiv2.className = "box";
    childDiv2.textContent = "<?php echo (\"<p>$fname $lname<p>\"); ?>";

    let childDiv3 = document.createElement("div");
    childDiv3.className = "box picture";
    childDiv3.textContent = "<?php echo ('<img src= \"' . $target_file . '\" id=\"upload-img\">'); ?>";

    let childDiv4 = document.createElement("div");
    childDiv4.className = "box";
    childDiv4.textContent = "<?php echo (\"<p>Email<p>\"); ?>";

    let childDiv5 = document.createElement("div");
    childDiv5.className = "box";
    childDiv5.textContent = "<?php echo (\"<p>\" . $email . \"<p>\"); ?>";

    let childDiv6 = document.createElement("div");
    childDiv6.className = "box";
    childDiv6.textContent = "<?php echo (\"<p>Address<p>\"); ?>";

    let childDiv7 = document.createElement("div");
    childDiv7.className = "box";
    childDiv7.textContent = "<?php echo (\"<p>\" . $address . \"<p>\"); ?>";

    outerDiv.appendChild(childDiv1);
    outerDiv.appendChild(childDiv2);
    outerDiv.appendChild(childDiv3);
    outerDiv.appendChild(childDiv4);
    outerDiv.appendChild(childDiv5);
    outerDiv.appendChild(childDiv6);
    outerDiv.appendChild(childDiv7);

    document.body.appendChild(outerDiv);

}