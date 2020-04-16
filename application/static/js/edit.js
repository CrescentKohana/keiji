function show_edit(id, clips_index) {
  const e = document.getElementById(`edit-${id}`);
  const eClasses = document.getElementsByClassName(`edit`);

  if (e.style.display === "none") {
      for (const eClass of eClasses) {
          eClass.style.display = "none";
      }

      document.getElementById(`edit-button-${id}`).style.display = 'Block';
      document.getElementById(`edit-button-${id}`).innerText = 'Cancel';

      e.style.display = "block";

      document.getElementById(`edit-${id}`).scrollIntoView();
  } else {
      document.getElementById(`edit-button-${id}`).innerText = 'Edit / Delete';
      e.style.display = "none";
      document.body.innerHTML +=
          `<form id="cancel-edit" action="${clips_index}" method="post"><input class="button" type="hidden"></form>`;
      document.getElementById("cancel-edit").submit();
  }
}