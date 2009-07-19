#!/bin/bash

echo "Content-type: text/html"
echo ""

forumname="My Forum"
forumdir="threads/"
header="../header.html"
footer="../footer.html"
curdate=`date -u +%F | sed 's/-/\//g'`
forum=`echo "$QUERY_STRING" | sed -n 's/^.*forum=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
thread=`echo "$QUERY_STRING" | sed -n 's/^.*thread=\([^&]*\).*$/\1/p' | sed "s/%20/ /;s/%2F/\//g"`

function getName
{
	echo `head -$1 .threads | tail -1`
}

if [ -f $header ] ; then
  	cat $header
else
  	echo "<html><body bgcolor='#FFFFFF' link='#000000' vlink='#000000'>"
fi

if [ $forum ]
	nicename=`echo $forum | sed 's/-/ /g'`
	echo "<h1>$forumname: $nicename</h1>"
	echo "<table border=\"1\"><tbody>"
	echo "<tr><td></td>"
	echo "<td><strong>Topic</strong></td>"
	echo "<td><strong>Posts</strong></td></tr>"
	
	for file in `ls -1 $forumdir/$forum/*.thread | sed 's/.thread//g'`
	do
		moddate=`date -ur $forumdir/$forum/$name.thread +%F | sed 's/-/\//g'`
		echo "<tr><td>"
		if [ `echo $moddate $curdate | awk '$2<$1{print -1;next}{print ($2>$1)}'` == 0 ]
		then
			echo "<strong>^_^</strong>"
		else
			echo "-_-"
		fi
		
		echo "</td><td>"
		getName $file
		echo "</td><td>$( wc -l $forumdir/$forum/$name.thread )</td></tr>"
	done
	
	echo "</tbody></table>"
fi
