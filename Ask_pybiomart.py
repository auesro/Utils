#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Get list of attributes in biomart for Mus Musculus 

Created on Wed Apr 26 14:59:39 2023

@author: auesro
"""

from pybiomart import Server

server = Server(host='sep2019.archive.ensembl.org')
b = server.list_marts()

mart = server['ENSEMBL_MART_ENSEMBL']
c = mart.list_datasets()

d = mart['mmusculus_gene_ensembl']

atributes = d.list_attributes()
