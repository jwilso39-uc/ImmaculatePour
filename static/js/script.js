const showBtn = document.querySelectorAll('.show-dialog');
const dialog = document.getElementById("dialog");
const modalForm = dialog.querySelector("form");

let activeRow = null;
let activeCol = null;

showBtn.forEach((btn) => {
  btn.addEventListener("click", () => {
    activeRow = btn.getAttribute('data-row');
    activeCol = btn.getAttribute('data-col');

    document.getElementById('modal-row').value = activeRow;
    document.getElementById('modal-col').value = activeCol;

    dialog.showModal();
  });
});

modalForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const formData = new FormData(modalForm);

    const data = Object.fromEntries(formData.entries());

    fetch("/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        console.log("Success:", result);
        
        // Update the UI here (e.g., change button text to the beer name)
        if (result.is_correct) {
            updateCell(activeRow, activeCol, data.beer_name);
        }
        
        dialog.close(); // Close the modal
        modalForm.reset(); // Clear the text input
    })
    .catch((error) => {
        console.error("Error:", error);
    });
});

function updateCell(row, col, name) {
    showBtn.forEach((btn) => {
        activeRow = btn.getAttribute('data-row');
        activeCol = btn.getAttribute('data-col');

        if (activeCol == col && activeRow == row) {
          btn.parentElement.innerHTML = `<div>${name}</div>`;
        }
    });
    const btn = document.querySelector(`.show-dialog[data-row="${row}"][data-col="${col}"]`);

}