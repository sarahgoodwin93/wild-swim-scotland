document.addEventListener("DOMContentLoaded", function() {
    let joinButton = document.querySelectorAll(".join-swim-btn");

    joinButton.forEach(function(button) {
        button.addEventListener("click", function() {
            let swimId = button.getAttribute("id").split("-").pop();
            let joined = button.classList.contains("joined");

            if(!joined) {
                button.textContent = "Swim Joined";
                button.classList.add("joined");
                button.style.backgroundColor = "#337ab7"
            } else {
                button.textContent = "Join this swim";
                button.classList.remove("joined");
                button.style.backgroundColor = "";
            }
        });
    });
});