import cgi
form = cgi.FieldStorage()
patname =  form.getvalue('pname')
patID = form.getvalue('pid')
docname = form.getvalue('dname')
docID = form.getvalue('did')


print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello - Second CGI Program</title>')
print ("</head>")
print ("<body>")
print ("<h2>Hello %s %s</h2>" % (patname, patID))
print ("</body>")
print ("</html>")
