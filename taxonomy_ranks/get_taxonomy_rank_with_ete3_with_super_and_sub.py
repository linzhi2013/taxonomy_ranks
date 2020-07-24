#!/usr/bin/env python3
import argparse
"""
get_taxonomy_rank_with_ete3.py

Copyright (c) 2017-2018 Guanliang Meng <mengguanliang@foxmail.com>.

This file is part of MitoZ.

MitoZ is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

MitoZ is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with MitoZ.  If not, see <http://www.gnu.org/licenses/>.

"""

import sys
import re
from ete3 import NCBITaxa


def get_para():
    desc = '''
To get the lineage information of input taxid, species name, or higher ranks
(e.g., Family, Order) with ETE3 package.

The ete3 package will automatically download the NCBI Taxonomy database during
 the first time using of this program.

Please be informed:

(1) A rank name may have more than one taxids, e.g., Pieris can means:
Pieris <butterfly> and Pieris <angiosperm>. I will search the lineages for
both of them.

(2) When you give a species name, if I can not find the taxid for the species
name, I will try to search the first word (Genus).

(3) Any input without result found will be output in outfile.err ('-o' option).
    '''

    parser = argparse.ArgumentParser(description=desc,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-i', dest='taxonomy_list', metavar='<file>',
        help='A file can be a list of ncbi taxa id or species names (or higher ranks, e.g. Family, Order), or a mixture of them.')

    parser.add_argument('-o', dest='outfile', metavar='<file>',
        help='outfile')

    parser.add_argument('-t', dest='print_taxid', action='store_true',
        help='Also print out the taxid for each rank')

    parser.add_argument('-v', dest='verbose', action='store_true',
        help='verbose output')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()


class TaxonomyRanks(NCBITaxa):
    """
    A taxa_name may have more than one potential_taxid.

    Usage:

    >>>rank_taxon = TaxonomyRanks(taxa_name)
    >>>rank_taxon.get_lineage_taxids_and_taxanames()
    >>>rank_taxon.lineages[potential_taxid][rank]

    Then 'rank' can be any one of below:

    ranks = ('user_taxa', 'taxa_searched', 'superkingdom', 'kingdom', 'superphylum', 'phylum', 'subphylum', 'superclass', 'class', 'subclass', 'superorder', 'order', 'suborder', 'superfamily', 'family', 'subfamily', 'genus', 'subgenus', 'species')

    """

    ranks = ('user_taxa', 'taxa_searched', 'superkingdom', 'kingdom', 'superphylum', 'phylum', 'subphylum', 'superclass', 'class', 'subclass', 'superorder', 'order', 'suborder', 'superfamily', 'family', 'subfamily', 'genus', 'subgenus', 'species')

    def __init__(self, user_taxa):
        NCBITaxa.__init__(self)
        self.lineages = dict()
        self.user_taxa = user_taxa
        self.taxa_searched = user_taxa
        self.potential_taxids = None

    def get_taxid(self, verbose=False):
        if re.match(r'^\d+$', self.taxa_searched):
            # the input is NCBI taxid
            self.potential_taxids = [self.taxa_searched]
        else:
            # the input is a species name or rank name
            name_dict = self.get_name_translator([self.taxa_searched])
            if not name_dict:
                ## try only the first word (which may be a genus name?)
                if verbose:
                    print("can not find taxid for", self.user_taxa, file=sys.stderr)
                taxa_name = self.user_taxa.split()
                if len(taxa_name) > 1:
                    self.taxa_searched = taxa_name[0]
                    if verbose:
                        print("try to search %s instead..." % self.taxa_searched, file=sys.stderr)
                    name_dict = self.get_name_translator([self.taxa_searched])

                if not name_dict:
                    #assert("can not find taxid for %s, maybe it's a misspelling.\n" % self.taxa_searched)
                    raise ValueError("can not find taxid for %s, maybe it's a misspelling.\n" % self.taxa_searched)

            self.potential_taxids = name_dict[self.taxa_searched]

        for potential_taxid in self.potential_taxids:
            potential_taxid = str(potential_taxid)
            self.lineages.setdefault(potential_taxid, {})
            for rank in self.ranks:
                self.lineages[potential_taxid][rank] = ('NA', 'NA')

            self.lineages[potential_taxid]['user_taxa'] = self.user_taxa
            self.lineages[potential_taxid]['taxa_searched'] = self.taxa_searched

    def get_lineage_taxids_and_taxanames(self, verbose=False):
        self.get_taxid(verbose=verbose)
        for potential_taxid in self.potential_taxids:
            lineage_taxids = self.get_lineage(potential_taxid)
            for j in lineage_taxids:
                rank = self.get_rank([j])[j]
                taxa = self.get_taxid_translator([j])[j]
                if rank in self.ranks:
                    self.lineages[str(potential_taxid)][rank] = (taxa, j)


def main():
    args = get_para()
    taxonomy_list = args.taxonomy_list
    outfile = args.outfile
    verbose = args.verbose
    print_taxid = args.print_taxid
    err_list_outfile = outfile + '.err'

    ranks = ('user_taxa', 'taxa_searched', 'superkingdom', 'kingdom', 'superphylum', 'phylum', 'subphylum', 'superclass', 'class', 'subclass', 'superorder', 'order', 'suborder', 'superfamily', 'family', 'subfamily', 'genus', 'subgenus', 'species')

    ranks_taxid = ('user_taxa', 'taxa_searched', 'superkingdom', 'superkingdom_taxid', 'kingdom', 'kingdom_taxid', 'superphylum', 'superphylum_taxid', 'phylum', 'phylum_taxid', 'subphylum', 'subphylum_taxid', 'superclass', 'superclass_taxid', 'class', 'class_taxid', 'subclass', 'subclass_taxid', 'superorder', 'superorder_taxid', 'order', 'order_taxid', 'suborder', 'suborder_taxid', 'superfamily', 'superfamily_taxid', 'family', 'family_taxid', 'subfamily', 'subfamily_taxid', 'genus', 'genus_taxid', 'subgenus', 'subgenus_taxid', 'species', 'species_taxid')

    with open(taxonomy_list, 'r') as fh, open(outfile, 'w') as fhout, open(err_list_outfile, 'w') as fhlog:
        if not print_taxid:
            print('\t'.join(ranks), file=fhout)
        else:
            print('\t'.join(ranks_taxid), file=fhout)

        for taxa_name in fh:
            taxa_name = taxa_name.strip()
            if not taxa_name:
                continue

            rank_taxon = TaxonomyRanks(taxa_name)
            try:
                rank_taxon.get_lineage_taxids_and_taxanames()
            except ValueError:
                if verbose:
                    print('{0} is invalid!'.format(taxa_name), file=sys.stderr)

                print(taxa_name, file=fhlog, flush=True)
                continue
            else:
                for potential_taxid in rank_taxon.lineages:
                    line = []
                    for rank in ranks[0:2]:
                        # the first two columns: 'user_taxa', 'taxa_searched'
                        line.append(rank_taxon.lineages[potential_taxid][rank])

                    # remained columns
                    for rank in ranks[2:]:
                        taxon, taxid = rank_taxon.lineages[potential_taxid][rank]
                        if print_taxid:
                            line.extend([taxon, str(taxid)])
                        else:
                            line.append(taxon)

                    line = "\t".join(line)
                    print(line, file=fhout)


if __name__ == '__main__':
    main()