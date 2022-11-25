const showItem = (item) => {
    const modal = document.querySelector('.modal');
    
    document.getElementById('delete-button').classList.remove('is-hidden');
    document.getElementById('update-button').innerText = 'Actualizar';
    document.querySelector('#form-product').method = 'PUT';
    modal.classList.add('is-active');
    modal.classList.remove('is-hidden');

    
    if(!item || !item.dataset) return;
    
    const { dataset } = item;
    Object.entries(dataset).forEach((attribute) => {
        const key = attribute[0];
        const value = attribute[1];

        modal.querySelectorAll(`[name = '${key}']`).forEach((input) => {
            const { tagName } = input;
            
            if(tagName === 'INPUT'){
                input.value = value;
            }else{
                input.innerText = value;
            }
        });
    });

};

const addProduct = () => {
    showItem();
    document.getElementById('update-button').innerText = 'Crear';
    document.getElementById('delete-button').classList.add('is-hidden');
    document.querySelector('#form-product').method = 'POST';
};


const getData = (form) => {
    const body = {};
    let select = false;
    let ID = "";

    const inputs = Array.from(form.elements); 

    inputs.forEach((input) => {
        let { tagName, name, value, type } = input;

        value = type === 'number' ? parseFloat(value) : value;
        name = name.charAt(0).toUpperCase() + name.slice(1);

        if(type === 'checkbox') { 
            select = input.checked;
            return;
        }

        if (tagName !== 'BUTTON' && name !== 'Document_id') 
        {
            if(name in body) {
                body[name] = [...body[name], value];
            }else{
                body[name] = value;
            }

        }

        if(name === 'Document_id') ID = value;
    })

    return { body, select, ID };
}

const deleteItem = () => {
    const forms = document.querySelectorAll('[name="form-product"]');
    
    forms.forEach( form => {
        const METHOD = 'DELETE';
        const { select, ID } = getData(form);
        let PATH = '/ciudadanos/' +  ID;
        
        if(ID === "") PATH = '/ciudadanos';

        if(!select) return;

        fetch(PATH, {
            method: METHOD,
            headers: {
                'Content-Type': 'application/json'
                }
        }).then(response => response.json())
        .then(data => {
            const { message } = data;
            if (message) {
                setTimeout(() => {
                    location.reload();
                }, 3000);
            }  
        }).catch(error => {
            location.reload();
        });
    })  

}

const updateItem = (item) => {
    const forms = document.querySelectorAll('[name="form-product"]');
    
    forms.forEach( form => {
        const METHOD = form.method === 'post' ? 'POST' : 'PUT';
        const { body, select, ID } = getData(form);
        let PATH = '/ciudadanos/' +  ID;
        
        if(ID === "") PATH = '/ciudadanos';

        if(!select) return;

        fetch(PATH, {
            method: METHOD,
            headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify(body)
        }).then(response => response.json())
        .then(data => {
            const { message } = data;
            if (message) {
                setTimeout(() => {
                    location.reload();
                }, 3000);
            }  
        }).catch(error => {
            console.log(error)
        });
    })

}


const getDataUnit = () => {
    const form = document.querySelector('#form-product');
    
    const body = {};

    const inputs = Array.from(form.elements); 

    inputs.forEach((input) => {
        let { tagName, name, value, type } = input;

        value = type === 'number' ? parseFloat(value) : value;
        name = name.charAt(0).toUpperCase() + name.slice(1);

        if (tagName !== 'BUTTON' && name !== 'Id') 
        {
            if(name in body) {
                body[name] = [...body[name], value];
            }else{
                body[name] = value;
            }

        }
    })

    return body;
}


const updateItemUnit = (item) => {
    const form = document.querySelector('#form-product');
    const METHOD = form.method === 'post' ? 'POST' : 'PUT';
    const ID = "";
    let PATH = '/ciudadanos/' +  ID;
    
    if(ID === "") PATH = '/ciudadanos';

    const data = getDataUnit();
    const responseBox = document.querySelector('.modal-response');
    console.log(METHOD)
    fetch(PATH, {
        method: METHOD,
        headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
    }).then(response => response.json())
    .then(data => {
        const { message } = data;
        if (message) {
            responseBox.classList.add('is-success');
            responseBox.innerText = message;
            
            setTimeout(() => {
                location.reload();
            }, 3000);
        }  
    }).catch(error => {
        console.log(error)
        responseBox.classList.add('is-danger');
        responseBox.innerText = 'Ha ocurrido un error.';
    });

}