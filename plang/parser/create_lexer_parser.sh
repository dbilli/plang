#!/bin/sh

CLASSPATH="$CLASSPATH:"$ANTLR_JAR

echo "ANTLR_JAR =" $ANTLR_JAR
echo "CLASSPATH =" $CLASSPATH

java -classpath $CLASSPATH org.antlr.v4.Tool -Dlanguage=Python3 -visitor Lang.g
