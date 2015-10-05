import os,sys

def get_wood(current_dir = None):
	files = []
	if not current_dir:
		current_dir = os.path.dirname(os.path.abspath(__file__))
	open('%s/js/output.js' % current_dir,'w').close()
	for dirpath, dirname, filename in os.walk(current_dir):
		if '.git' not in dirpath:	
			for a in filename:
				files.append('%s/%s' % (dirpath,a))
	file_text_split = ''
	for file_path in files:
		with open(file_path,'r+') as w:
			file_text_split += w.read().replace('\n',' ').replace('\t',' ').replace('"','_') + ' '
	with open('%s/js/output.js' % current_dir,'w') as fi:
		fi.write('window.output = "%s"' % file_text_split)

if __name__ == '__main__':
	try:
		get_wood(sys.argv[1])
	except IndexError:
		get_wood()