#!/bin/bash
for F in *.ui
do
	OUTPUT=ui_$(basename $F .ui).py
	echo "Generating $OUTPUT..."
	pyuic4 -o $OUTPUT $F
done
