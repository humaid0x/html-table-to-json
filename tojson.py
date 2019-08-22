import json, re

def tojson(data):
	k = [x.strip().lower() for x in re.findall("<th(?!ead)[^>]*>(.*?)<\/th>", data)]
	patt = re.compile("<td[^>]*>(.*?)<\/td>")
	row = re.findall("<tr[^>]*>(.*?)<\/tr>", data, re.S)
	val = filter(None, [patt.findall(x) for x in row])
	out = [dict(zip(k, v)) for v in val] if k else [*val]
	return json.dumps(out)

if __name__ == "__main__":
	table = '''<table><tr><th>Firstname</th><th>Lastname</th><th>Age</th></tr>
			<tr><td>Jill</td><td>Smith</td><td>50</td></tr>
			<tr><td>Eve</td><td>Jackson</td><td>94</td></tr>
			<tr><td>John</td><td>Doe</td><td>80</td></tr></table>'''
	print(tojson(table))