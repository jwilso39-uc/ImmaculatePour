const showBtn = document.querySelectorAll('.show-dialog');
const dialog = document.getElementById("dialog");
const jsCloseBtn = dialog.querySelector("#js-close");

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

jsCloseBtn.addEventListener("click", (e) => {
  dialog.close();
});