const toastLiveExample = document.getElementsByClassName('toast')
const navbar = document.getElementById("navbar")
const navbarToggler = document.getElementById("navbar-toggler")

function navbarTogglerOnClick() {
    if (navbarToggler.getAttribute("aria-expanded") === "true") {
        navbar.classList.remove("bg-transparent");
        navbar.classList.add("bg-light");
    } else {
        navbar.classList.remove("bg-light");
        navbar.classList.add("bg-transparent");
    }
}

document.addEventListener("DOMContentLoaded", function () {

    const triggerToast = (item) => {
        const toastBootstrap = bootstrap.Toast.getOrCreateInstance(item)
        toastBootstrap.show()
    }

    for (let toast of toastLiveExample) {
        triggerToast(toast)
    }


    const forms = document.querySelectorAll('.needs-validation')

    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })


    function updateProgress() {
        const progressBars = document.querySelectorAll(".dynamic-progress");

        progressBars.forEach((progress, index) => {
            const progressValue = progress.querySelector(".progress-value");
            const percentage = parseInt(progressValue.getAttribute("data-progress"));

            // Ensure that the percentage is within the valid range (0-100)
            const clampedPercentage = Math.min(Math.max(percentage, 0), 100);

            // Update the progress bar and value
            progress.style.setProperty('--progress-percentage', `${clampedPercentage}`);
            progressValue.innerText = `${clampedPercentage}%`;
        });
    }

// Call the function to update progress bars
    updateProgress();

})

