all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(items):
	return list(map(lambda item: f"<li>{item['label']}</li>", filter_colors(items)))

def filter_colors(items):
	return list(filter(lambda item: item["sexy"], items))

print(generate_li(all_colors))
