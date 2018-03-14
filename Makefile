PREFIX?=/opt/local
PORTINDEX=$(PREFIX)/var/macports/sources/github.com/macports/macports-ports/Portindex

ports.json: portindex2json.tcl $(PORTINDEX)
	tclsh $^ > $@
	wc -l $@

portindex2json:
	wget https://github.com/repology/repology/raw/master/helpers/portindex2json/portindex2json.tcl

_output:
	mkdir $@
