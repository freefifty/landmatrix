import csv

def clean(cell):
	cell = cell.replace('Viet Nam', 'Vietnam')
	cell = cell.replace('Timor-Leste', 'East Timor')
	cell = cell.replace('Timor-Leste', 'East Timor')
	cell = cell.replace('United States of America', 'USA')
	cell = cell.replace("Côte d'Ivoire", 'Ivory Coast')
	cell = cell.replace("Venezuela (Bolivarian Republic of)", 'Venezuela')
	cell = cell.replace("United Republic of Tanzania", 'Tanzania')
	cell = cell.replace("Lao People's Democratic Republic", 'Laos')
	cell = cell.replace("Russian Federation", 'Russia')
	cell = cell.replace("Bolivia (Plurinational State of)", 'Bolivia')
	cell = cell.replace("Republic of Korea", 'South Korea')
	cell = cell.replace('United Kingdom of Great Britain and Northern Ireland', 'England')

	# clean opening and closing whitespace
	cell = cell. replace('^\s', "")
	cell = cell. replace('\s$', "")
	return cell

with open("../data/landmatrix/all.csv", "r") as f1, open("../data/landmatrix/all_fixed.csv", "w") as f2:
	reader = csv.reader(f1, delimiter="|")
	writer = csv.writer(f2, delimiter="|")
	for row in reader:
		new_line = [clean(x) for x in row]
		writer.writerow(new_line)