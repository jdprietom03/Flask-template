
const closeModal = () => {
    document.querySelector('.modal').classList.remove('is-active');
    document.querySelector('.modal').classList.add('is-hidden');
}

const hideEditable = (input) => {
    input.disabled = !input.disabled;

    input.classList.remove('is-relative');
    const sibling = input.previousElementSibling;
    sibling.classList.remove('is-hidden');
    sibling.innerText = input.value;
}

const showEditable = (input) => {
    const sibling = input.nextElementSibling;
    sibling.disabled = !sibling.disabled;
    sibling.focus();

    input.classList.add('is-hidden');
    sibling.classList.add('is-relative');
}