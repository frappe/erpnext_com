frappe.ready(() => {
	let pathname = window.location.pathname;
	if (pathname.startsWith('/docs')) {
		let $search = $('<input type="search" placeholder="Search docs" class="form-control mt-4" />');
		$('.page-head .col-sm-12').append($search);
		$search.on('keydown', e => {
			if (e.key == 'Enter') {
				window.location.href = '/search?scope=/docs&q=' + e.target.value;
			}
		});
	}

	if (pathname.startsWith('/search')) {
		$('.page_content').addClass('container');
	}
});
