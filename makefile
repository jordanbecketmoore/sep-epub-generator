items: 
	ls entries/ | sort | sed 's|\(.*\)\.html|    <item id="\1" href="\1.html" media-type="application/xhtml+xml"/>|g' > ../../items