var updateBtns = document.getElementsByClassName('update-cart')

for (var i=0; i<updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        //console.log('productId:', productId, 'action:', action)

        //console.log('User:', user)
        if (user == 'AnonymousUser') {
            addCookieItem(productId, action)
        }
        else {
            updateUserOrder(productId, action)
        }
    }
    )
}


function addCookieItem(productId, action){
    if (action == 'add') {
        console.log(cart)
        if (cart[productId] == undefined) {
            cart[productId] = {'quantity':1}
            
        }else {
            cart[productId]['quantity']++ ;
        }        
    }
    if (action == 'remove') {
        cart[productId]['quantity'] -= 1
        if (cart[productId]['quantity'] <= 0) {
            delete cart[productId]
        }       
    }
    if (action == 'deleter') {
        delete cart[productId]
    }

    if (action == 'favorite') {
        delete cart[productId]
    }
    
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    console.log(document.cookie[cart])
    location.reload()
}

function updateUserOrder(productId, action) {
    console.log('Sending data as logged in user')

    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action,})
    })


    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data', data)
        location.reload()

    })
    

}

