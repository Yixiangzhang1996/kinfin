#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import sys
import os
import itertools
import numpy as np
import pandas as pd
import matplotlib as mat
mat.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context("talk")
#sns.set(font='serif')
sns.set(style="whitegrid")

def plot(infile):

    data = pd.read_csv(infile, sep=",")

    f, ax = plt.subplots(figsize=(24, 12))
    sns.set_color_codes("pastel")
    total_proteins = 2376717
    percentage_proteins_different_not_hierarchical = data["count_of_proteins_different_not_hierarchical"]/total_proteins
    percentage_proteins_different_hierarchical = percentage_proteins_different_not_hierarchical + data["count_of_proteins_different_hierarchical"]/total_proteins
    percentage_proteins_identical = percentage_proteins_different_hierarchical + data["count_of_proteins_identical"]/total_proteins

    g = sns.barplot(y=percentage_proteins_identical, x="inflation_value_combination", data=data,
                                label="identical", color='r')

    g = sns.barplot(y=percentage_proteins_different_hierarchical, x="inflation_value_combination", data=data,
                                label="different (hierarchical)", color='g')

    g = sns.barplot(y=percentage_proteins_different_not_hierarchical, x="inflation_value_combination", data=data,
                                label="different (not hierarchical)", color='b')





    #sns.set_color_codes("pastel")
    #sns.barplot(y="count_genes", x="species_id", data=data,
    #        label="Genes", color='w')
    ax.legend(ncol=1, loc="upper center", frameon=True)
    ax.set_ylabel("Percentage of proteins")
    ax.set_xlabel("")
    sns.despine(left=False, offset=10, trim=True)
    #plt.xticks(rotation=90)
    f.tight_layout()

    f.savefig("barplot.jaccard.png")
    f.savefig("barplot.jaccard.svg")

    #g, ax = plt.subplots(figsize=(24, 12))
    #ax3 = sns.barplot(x="species_id", y="count_sequences", data=data,
    #        label="Sequences", color='w')
    #sns.despine(left=False, offset=10, trim=True)
    #ax3.legend(ncol=1, loc="upper right", frameon=True)
    #ax3.set_ylabel("Count")
    #ax3.set_xlabel("")

    #plt.xticks(rotation=90)
    #g.tight_layout()
    #g.savefig("barplot.species.proteins.svg")




    #perc_count_monospecies = data["count_monospecies"]/data["count_clusters"]
    #clusters = data["count_clusters"]
    #perc_count_singletons = data["count_singletons"]/data["count_clusters"]
    #inflation_values = data["#inflation_value"]
    #dataframe = pd.concat([clusters, perc_count_monospecies, perc_count_singletons, inflation_values], axis=1, keys=['clusters', 'mono-species clusters (%)', 'single-protein clusters (%)', 'Inflation value'])
    #f = sns.lmplot('mono-species clusters (%)', 'clusters', data=dataframe, hue='Inflation value', fit_reg=False)
    #f.add_legend()
    #f.savefig("mono_vs_clusters.png")
    #g = sns.lmplot('mono-species clusters (%)', 'single-protein clusters (%)', data=dataframe, hue='Inflation value', fit_reg=False)
    #g.add_legend()
    #g.savefig("mono_vs_single.png")
    #h = sns.lmplot('single-protein clusters (%)', 'clusters',  data=dataframe, hue='Inflation value', fit_reg=False)
    #h.add_legend()
    #h.savefig("single_vs_clusters.png")

if __name__ == "__main__":

    try:
        infile = sys.argv[1]
    except:
        sys.exit("./plot.py INFILE")

    plot(infile)