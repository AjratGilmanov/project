'use strict';

const books = document.querySelectorAll('.book_list__item');
const selectsForCustom = document.querySelectorAll('.select_custom')



selectsForCustom.forEach(select => {
	function filter() {
		if (select.value == 'Все') {
			books.forEach(book => {
				book.style.display = '';
			})
			return;
		}
		books.forEach(book => {
			let categories = [...book.querySelectorAll('.book_list__item__categories__list__item')].map(elem => elem.textContent)
			if ( categories.includes(select.value) ) {
				book.style.display = '';
			} else {
				book.style.display = 'none';
			}
		})
	}
	
	select.style.display = 'none';
	
	const parent = select.parentElement;
	const selected = document.createElement('div');
	selected.className = 'filter_select-selected';
	selected.textContent = select.selectedOptions[0].textContent;
	
	const list = document.createElement('div');
	list.className = 'filter_select__list';
	
	const wrap = document.createElement('div');
	wrap.className = 'filter_select';
	select.parentElement.insertBefore(wrap, select.nextSibling);
	wrap.appendChild(selected);
	wrap.appendChild(list)

	const hr = document.createElement('hr');
	list.appendChild(hr);

	select.querySelectorAll('option').forEach(select => {
		const option = document.createElement('div');
		option.textContent = select.textContent;
		option.className = 'filter_select__list__item';
		option.dataset.value = select.value;
		list.appendChild(option);
	})
	
	list.addEventListener('click', event => {
		const selected_option = event.target.closest('.filter_select__list__item');
		selected.textContent = selected_option.textContent;
		select.value = selected_option.dataset.value;
		filter()
		list.style.maxHeight = '0';
		setTimeout(() => {
			list.style.maxHeight = '';
		}, 300);
	})
})