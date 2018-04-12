function open_modal() {
    var modal = document.getElementById("delete-modal");
    var html = document.querySelector('html');
    modal.classList.add('is-active');
    html.classList.add('is-clipped');

}

function close_modal() {
    var modal = document.getElementById("delete-modal");
    var html = document.querySelector('html');
    modal.classList.remove('is-active');
    html.classList.remove('is-clipped');
}