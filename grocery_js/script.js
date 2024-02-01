const form = document.querySelector('#form');
const list = document.querySelector('#list');
const item = document.querySelector('#item');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    if (item.value.trim() !== '') {
        const li = document.createElement('li');
        li.textContent = item.value;
        list.appendChild(li);
        item.value = '';
        li.addEventListener('click', () => {
            li.style.textDecoration = 'line-through';
        });
    }
});