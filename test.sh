#!/usr/bin/bash

rm -fv post*
./emp_compare.py q1_2016.xlsx q2_2016.xlsx
libreoffice post*
