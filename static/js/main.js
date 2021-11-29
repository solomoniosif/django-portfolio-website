document.addEventListener('DOMContentLoaded', () => {
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {
        // Add a click event on each of them
        $navbarBurgers.forEach(el => {
            el.addEventListener('click', () => {
                // Get the target from the "data-target" attribute
                const target = el.dataset.target;
                const $target = document.getElementById(target);
                // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');
            });
        });
    }
});

// Close notification
document.addEventListener('DOMContentLoaded', () => {
    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
        const $notification = $delete.parentNode;

        $delete.addEventListener('click', () => {
            $notification.parentNode.removeChild($notification);
        });
    });
});

// Close notification modal
// const modal = document.querySelector("#notification-modal");
// const closeModalBtn = document.querySelector("#closeModalBtn");
// closeModalBtn.addEventListener("click", function (event) {
//         modal.classList.remove('is-active');
//     }
// );

// Photo Formset Management
const imageForms = document.getElementsByClassName("image-form");
const mainForm = document.querySelector("#inline-form");
const addImageFormBtn = document.querySelector("#add-image-form");
const endOfForm = document.querySelector("#form-end-hidden")
const totalForms = document.querySelector("#id_post_images-TOTAL_FORMS");

let formCount = imageForms.length - 1;

function updateForms() {

    let count = 0;
    for (let form of imageForms) {
        const formRegex = RegExp(`post_images-(\\d){1}-`, 'g');
        form.innerHTML = form.innerHTML.replace(formRegex, `post_images-${count++}-`)
    }
}

addImageFormBtn.addEventListener("click", function (event) {
    event.preventDefault();

    const newImageForm = imageForms[0].cloneNode(true);
    const formRegex = RegExp(`post_images-(\\d){1}-`, 'g');

    formCount++;

    newImageForm.innerHTML = newImageForm.innerHTML.replace(formRegex, `post_images-${formCount}-`);
    mainForm.insertBefore(newImageForm, endOfForm);
    totalForms.setAttribute('value', `${formCount + 1}`);
});

mainForm.addEventListener("click", function (event) {
    if (event.target.classList.contains("delete-image-form")) {
        event.preventDefault();
        event.target.parentElement.remove();
        formCount--;
        updateForms();
        totalForms.setAttribute('value', `${formCount + 1}`);
    }
});
