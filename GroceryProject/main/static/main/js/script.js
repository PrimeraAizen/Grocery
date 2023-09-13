let addButtons = document.querySelectorAll('#updateBtn');


for (btn of addButtons) {
    btn.addEventListener('click', function () {
        let productID = this.dataset.product;
        let action = this.dataset.action;
        if (user === 'AnonymousUser') {
            console.log('Not logged in');
        } else {
            console.log('User is logged in, sending data...');
            updateUserOrder(productID, action);
        }
    });
}


function updateUserOrder(productID, action){
    let url = '/update_cart/';
    
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productID': productID, 'action': action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        location.reload();
    });
}