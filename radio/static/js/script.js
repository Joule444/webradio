document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("a.ajax-link").forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();

            let url = this.getAttribute("href");

            fetch(url)
                .then(response => response.text())
                .then(data => {
                    document.getElementById("content").innerHTML = data;
                    window.history.pushState(null, "", url);
                })
                .catch(error => console.error("Erreur AJAX:", error));
        });
    });
});