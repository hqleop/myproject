      const sidebar = document.getElementById("sidebar");
      const toggleButton = document.getElementById("toggleButton");

      toggleButton.addEventListener("click", () => {
        sidebar.classList.toggle("collapsed");
      });

      function toggleMenu(element) {
        element.classList.toggle("open");
      }