window.onload=function(){
    var md = document.getElementById("open-delete-modal");
    md.addEventListener("click", open_modal);

    var md_close = document.getElementById("btn-close-modal");
    md_close.addEventListener("click", close_modal);

    var md_cancel = document.getElementById("btn-cancel-modal");
    md_cancel.addEventListener("click", close_modal);

    var md_validate = document.getElementById("btn_validate_modal");
    md_validate.addEventListener("click", close_modal);

    var md_ttt= document.getElementById("background_modal");
    md_ttt.addEventListener("click", close_modal);

};

function open_modal(){
    var modal = document.getElementById("delete-modal");
    var html = document.querySelector('html');
    modal.classList.add('is-active');
    html.classList.add('is-clipped');

}

function close_modal(){
    var modal = document.getElementById("delete-modal");
    var html = document.querySelector('html');
    modal.classList.remove('is-active');
    html.classList.remove('is-clipped');
}


/*
document.querySelector('a#open-delete-modal').addEventListener('click', function(event) {
  event.preventDefault();

  var modal = document.querySelector('.modal');  // assuming you have only 1
  var html = document.querySelector('html');
    console.log(modal);
    console.log(html);
    modal.classList.add('is-active');
  html.classList.add('is-clipped');

  modal.querySelector('.modal-background').addEventListener('click', function(e) {
    e.preventDefault();
    modal.classList.remove('is-active');
    html.classList.remove('is-clipped');
  });
});
*/
