(function () {
    var sidebar = document.getElementById("appSidebar");
    var toggle = document.getElementById("sidebarToggle");
    var backdrop = document.getElementById("sidebarBackdrop");

    if (!sidebar || !toggle || !backdrop) {
        return;
    }

    function closeSidebar() {
        sidebar.classList.remove("open");
        backdrop.classList.remove("visible");
    }

    toggle.addEventListener("click", function () {
        sidebar.classList.toggle("open");
        backdrop.classList.toggle("visible");
    });

    backdrop.addEventListener("click", closeSidebar);

    window.addEventListener("resize", function () {
        if (window.innerWidth >= 992) {
            closeSidebar();
        }
    });
})();
