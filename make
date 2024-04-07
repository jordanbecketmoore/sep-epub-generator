
metadata() {
	cat >book/OPS/content.opf <<EOF 
<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>Hegel's Dialectics</dc:title>
    <dc:creator opf:role="aut">Stanford Encyclopedia of Philosophy</dc:creator>
    <dc:language>en</dc:language>
    <dc:date>2024-04-06</dc:date>
    <!-- Add more metadata as needed -->
  </metadata>
  <manifest>
    <!-- Include all HTML files used in the EPUB -->
EOF
	ls book/OPS/entries/ | sort | sed 's|\(.*\)\.html|    <item id="\1" href="entries/\1.html" media-type="application/xhtml+xml"/>|g' >> book/OPS/content.opf
	echo "	</manifest>" >> book/OPS/content.opf
	echo "	<spine>" >> book/OPS/content.opf
	ls book/OPS/entries/ | sort | sed 's|\(.*\)\.html|    <itemref idref="\1"/>|g' >> book/OPS/content.opf
	echo "	</spine>" >> book/OPS/content.opf
	echo "</package>" >> book/OPS/content.opf
	cp book/OPS/content.opf book/META-INF/metadata.xml
}

epub() {
	cd book
	zip ../book.epub -r * -f
	cd ..
}


# MAIN
$1

