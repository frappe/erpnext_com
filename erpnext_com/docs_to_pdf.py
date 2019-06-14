import frappe
import io
import re
import os
from pathlib import Path

# bench --site sitename execute erpnext_com.docs_to_pdf.execute --args user/manual/en/index.md
# pandoc ./sites/erpnext-manual.md -o erpnext-manual.pdf

source = ''
target = ''
base = ''
assets_path = ''
already_done = []
index = 0
all_content = ''

def execute(source_file_path=None):
	global all_content
	setup_paths(source_file_path)
	s = Path(source)

	make_file(s, s.name)

	all_content = all_content.replace('/docs/assets/img', assets_path + '/assets/img')
	all_content = all_content.replace(
		'{{docs_base_url}}', assets_path).replace(
			'{{ docs_base_url }}', assets_path)

	all_content = all_content.replace('.html', '')
	all_content = re.sub(r'\n---\n', '', all_content)
	all_content = re.sub(r'!\[.*]\(/docs/assets/old_images/.*\n', '', all_content)
	all_content = re.sub(r'<img .*src="(.*)">', r'<br>![](\1)', all_content)
	all_content = re.sub(r'(#+)(\w)', r'\1 \2', all_content)
	all_content = re.sub('{next}', '', all_content)

	image_links = re.findall(r'!\[.*]\((.*)\)', all_content)

	for link in image_links:
		if not Path(link).exists():
			all_content = all_content.replace(link, '')

	manual = Path(target) / 'erpnext-manual.md'
	manual.touch()
	manual.write_text(all_content)
	print(manual.absolute())


def setup_paths(source_file_path):
	global source, target, base, assets_path

	if not source_file_path:
		source_file_path = 'user/manual/en/index.md'

	app_path = frappe.get_app_path('erpnext_com')
	source = os.path.join(app_path, 'www/docs', source_file_path)
	target = '.'
	base = os.path.join(app_path, 'www')
	assets_path = os.path.join(app_path, 'www/docs')


def make_file(s, file_name):
	global index
	global already_done
	global all_content

	if s.absolute() in already_done:
		return

	# print(index)
	content = get_content(s)
	content += '\n\n\\newpage\n\n'

	all_content += content

	index += 1
	already_done.append(s.absolute())

	children = get_children_files(content)

	for child in children:
		if child.is_dir():
			index_file = child / 'index.md'
			if index_file.exists():
				make_file(index_file, child.name)
		if child.is_file():
			make_file(child, child.name)


def get_children_files(content):
	matches = re.findall(r'\(/(docs/user/manual.*?)\)', content)

	paths = []
	for m in matches:
		paths.append(Path(base) / m)
		paths.append(Path(base) / (m + '.md'))

	return [p for p in paths if p.exists()]


def get_content(path_obj):
	with path_obj.open() as f:
		return f.read()
