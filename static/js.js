// update the class page
$(document).ready(function() {
    function check(num) {
        var real = document.getElementById("number").value;
        var str = "" + num;
        var name = document.getElementById("nombre").value;
        console.log(str);
        if (num == real)
        {
            document.getElementById("heading").style.color = "green";
            document.getElementById("heading").innerHTML = "Correct!";
            document.getElementById("message").style.color = "green";
            document.getElementById(str).className = "btn btn-success";
            document.getElementById("name").innerHTML = `<h4 color='green'>- ${name}</h4>`;
            document.getElementById("whole").style.display = "none";
            hold();
        }
        else
        {
            document.getElementById("heading").style.color = "red";
            document.getElementById("heading").innerHTML = "Incorrect";
            document.getElementById("message").innerHTML = "<h3>Try again!</h3>";
            document.getElementById("message").style.color = "red";
            document.getElementById(str).className = "btn btn-danger";
            setTimeout(clear, 1500);
        }
    }

    function hold() {
        document.getElementById("new").style.display = "none";
        document.getElementById("message").innerHTML = "<form><button class='btn btn-success'>New Quote</button></form><br>";
    }

    function clear() {
        document.getElementById("message").innerHTML = "";
    }
});
