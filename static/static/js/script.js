function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue
}


document.addEventListener('DOMContentLoaded', function () {
    var select = document.getElementById('input-select');
    var array = []
    var button = document.getElementById('do-buton')
    var confirm_delete = document.getElementById('confirm')
    var delete_button = document.getElementById('delete-button')
    var all_delete_buttons = document.querySelectorAll('.delete-button')
    var delButton = document.getElementById('del-confirm')
    var selectedFiles = document.querySelectorAll('.del-files')
    var delFiles = []
    delButton.addEventListener('click',function (){

        selectedFiles.forEach(file=>{
            file.addEventListener('change',function (){
                          if (file.checked === true) {
                              delFiles.push(file.id)
                          }
                              if (file.checked === false){
                                  delFiles = delFiles.filter(item => item !== file.id)
                              }
            })
        })







    all_delete_buttons.forEach(value => {
        value.addEventListener('click', function () {
            confirm_delete.addEventListener('click', function () {
                fetch(`delete/${value.id}`).then(res=>{
                    location.reload()
                })

            })
        })
    })


    document.querySelectorAll("input[type='checkbox']").forEach(value => {
        value.addEventListener('change', function () {
            if (value.checked === true) {
                array.push(value.id)
            }

        })
    })


    delete_button.addEventListener('click', function () {
        for (i = 0; i < array.length; i++) {
            fetch(`delete-user/${array[i]}`).then(res => {
                location.reload()
            })
        }

    })

    button.addEventListener('click', function () {
        if (select.value === 'Bloklash') {
            for (i = 0; i < array.length; i++) {
                fetch(`block/${array[i]}`).then(res => {
                    location.reload()
                })
            }
        }
        if (select.value === 'Blokdan ochish') {
            for (i = 0; i < array.length; i++) {
                fetch(`unblock/${array[i]}`).then(res => {
                    location.reload()
                })
            }
        }
    })
})