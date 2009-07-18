#!/bin/bash

echo "Content-type: text/html"
echo ""

forumname="My Forum"
forumdir="threads/"
header="header.html"
footer="footer.html"
curdate=`date -u +%F | sed 's/-/\//g'`

if [ -f $header ] ; then
  	cat $header
else
  	echo "<html><body bgcolor='#FFFFFF' link='#000000' vlink='#000000'>"
fi

echo "<h1>$forumname: Index</h1>"
echo "<table border=\"1\"><tbody>"
echo "<tr><td></td>"
echo "<td><strong>Forum</strong></td>"
echo "<td><strong>Threads</strong></td></tr>"


for name in `ls -1 $forumdir | sed 's/\///;s/-/ /g'`
do
	moddate=`date -ur $forumdir/$name +%F | sed 's/-/\//g'`
	echo "<tr><td>"
	if [ `echo $moddate $curdate | awk '$2<$1{print -1;next}{print ($2>$1)}'` == 0 ]
	then
		echo "<strong>^_^</strong>"
	else
		echo "-_-"
	fi
	echo "</td><td>$name</td>"
	
	threadcount=`ls -1 $forumdir/$name | wc -l`
	echo "<td>$threadcount</td></tr>"
done

echo "</tbody></table>"

if [ -f $footer ] ; then
	cat $footer
else
	echo "</body></html>"
fi

exit 0
