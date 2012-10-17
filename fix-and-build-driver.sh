#!/bin/bash

set -e
set -x

SRCRPM=$1
SPECDIR=`rpm -E '%_specdir'`
SPEC=$SPECDIR/${SRCRPM/-[0-9]*/.spec}

rpm -i $SRCRPM
sed -i 's/^autoreconf/\0 --force/' $SPEC
rpmbuild --define "_rpmdir rpm/" -bb $SPEC

