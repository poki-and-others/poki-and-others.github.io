function nextImage(button_el) {
	img_el = button_el.parentNode.querySelector("img")
	const image_list = img_el.dataset.image_set.split(",")
	
	idx = parseInt(img_el.dataset.curr_image)
	num_image = parseInt(img_el.dataset.num_image)
	idx += 1
	if (idx === num_image) {
		idx = 0
	}
	img_el.dataset.curr_image = idx

	img_el.src = image_list[idx]
}

function previousImage(button_el) {
	img_el = button_el.parentNode.querySelector("img")
	const image_list = img_el.dataset.image_set.split(",")
	
	idx = parseInt(img_el.dataset.curr_image)
	num_image = parseInt(img_el.dataset.num_image)
	idx -= 1
	if (idx === -1) {
		idx = num_image-1
	}
	img_el.dataset.curr_image = idx

	img_el.src = image_list[idx]
}