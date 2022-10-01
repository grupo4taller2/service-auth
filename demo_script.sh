#!/bin/bash

if [ "lint" == "$1" ]
then
	docker exec fiuber.service-tipitos.dev flake8

elif [ "behave" == "$1" ]
then
	docker exec fiuber.service-tipitos.dev coverage run --source='.' -m behave ./test/features
	
elif [ "montar" == "$1" ]
then
	echo 'montar'
fi
