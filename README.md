# taxonomy-ranks

## 1 Introduction
To get taxonomy ranks information with ETE3 Python3 module (`http://etetoolkit.org/`)

## 2 Installation

Make sure your `pip` is from Python3

	$ which pip
	/Users/mengguanliang/soft/miniconda3/bin/pip

then type

    $ pip install taxonomy_ranks

There will be a command `taxaranks` created under the same directory where your `pip` command located.


If you want to learn more about Python3 and `pip`, please refer to `https://www.python.org/` and `https://docs.python.org/3/tutorial/venv.html?highlight=pip`.

## 3 Usage
### 3.1 commandline usage

	$ taxaranks

		usage: taxaranks [-h] [-i <file>] [-o <file>] [-t] [-v]

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


		optional arguments:
		  -h, --help  show this help message and exit
		  -i <file>   A file can be a list of ncbi taxa id or species names (or higher
		              ranks, e.g. Family, Order), or a mixture of them.
		  -o <file>   outfile
		  -t          Also print out the taxid for each rank
		  -v          verbose output


The `-i <file>` file can be a list of ncbi taxa id or species names (or higher ranks, e.g. Family, Order), or a mixture of them.


ETE3 package will automatically download the NCBI Taxonomy database during the first time using of this program.
    
Once the NCBI Taxonomy database has been installed, there is no need to connect to the network any more, unless you want to update the database after a period of time, for this case, please go to `http://etetoolkit.org/docs/latest/tutorial/tutorial_ncbitaxonomy.html` for more details.

### 3.2 using as a module

A taxa_name may have more than one potential_taxid.

        >>>from taxonomy_ranks import TaxonomyRanks
	    >>>rank_taxon = TaxonomyRanks(taxa_name)
	    >>>rank_taxon.get_lineage_taxids_and_taxanames()
	    >>>ranks = ('user_taxa', 'taxa_searched', 'superkingdom', 'kingdom', 'superphylum', 'phylum', 'subphylum', 'superclass', 'class', 'subclass', 'superorder', 'order', 'suborder', 'superfamily', 'family', 'subfamily', 'genus', 'subgenus', 'species')
	    >>>for rank in ranks:
	    >>>    print(rank, rank_taxon.lineages[potential_taxid][rank])

## 4 Example

run 

	$ taxaranks -i test.taxa -o test.taxa.out

Input file `test.taxa`content:
	
	Spodoptera litura
	Pieris rapae
	Locusta migratoria
	Frankliniella occidentalis
	Marsupenaeus japonicus
	Penaeus monodon

Result file `test.taxa.out` content:

	user_taxa	taxa_searched	superkingdom	kingdom	superphylum	phylum	subphylum	superclass	class	subclass	superorder	order	suborder	superfamily	family	subfamily	genus	subgenus	species
	Spodoptera litura	Spodoptera litura	Eukaryota	Metazoa	NA	Arthropoda	Hexapoda	NA	Insecta	Pterygota	Amphiesmenoptera	Lepidoptera	Glossata	Noctuoidea	Noctuidae	Amphipyrinae	Spodoptera	NA	Spodoptera litura
	Pieris rapae	Pieris rapae	Eukaryota	Metazoa	NA	Arthropoda	Hexapoda	NA	Insecta	Pterygota	Amphiesmenoptera	Lepidoptera	Glossata	Papilionoidea	Pieridae	Pierinae	Pieris	NA	Pieris rapae
	Locusta migratoria	Locusta migratoria	Eukaryota	Metazoa	NA	Arthropoda	Hexapoda	NA	Insecta	Pterygota	NA	Orthoptera	Caelifera	Acridoidea	Acrididae	Oedipodinae	Locusta	NA	Locusta migratoria
	Frankliniella occidentalis	Frankliniella occidentalis	Eukaryota	Metazoa	NA	Arthropoda	Hexapoda	NA	Insecta	Pterygota	NA	Thysanoptera	Terebrantia	Thripoidea	Thripidae	Thripinae	Frankliniella	NA	Frankliniella occidentalis
	Marsupenaeus japonicus	Marsupenaeus japonicus	Eukaryota	Metazoa	NA	Arthropoda	Crustacea	Multicrustacea	Malacostraca	Eumalacostraca	Eucarida	Decapoda	Dendrobranchiata	Penaeoidea	Penaeidae	NA	Penaeus	NA	Penaeus japonicus
	Penaeus monodon	Penaeus monodon	Eukaryota	Metazoa	NA	Arthropoda	Crustacea	Multicrustacea	Malacostraca	Eumalacostraca	Eucarida	Decapoda	Dendrobranchiata	Penaeoidea	Penaeidae	NA	Penaeus	NA	Penaeus monodon

With the '-t' optioin,

	$ taxaranks -i test.taxa -o test.taxa.out -t

Result file `test.taxa.out` will be:

	user_taxa	taxa_searched	superkingdom	superkingdom_taxid	kingdom	kingdom_taxid	superphylum	superphylum_taxid	phylum	phylum_taxid	subphylum	subphylum_taxid	superclass	superclass_taxid	class	class_taxid	subclass	subclass_taxid	superorder	superorder_taxid	order	order_taxid	suborder	suborder_taxid	superfamily	superfamily_taxid	family	family_taxid	subfamily	subfamily_taxid	genus	genus_taxid	subgenus	subgenus_taxid	species	species_taxid
	Spodoptera litura	Spodoptera litura	Eukaryota	2759	Metazoa	33208	NA	NA	Arthropoda	6656	Hexapoda	6960	NA	NA	Insecta	50557	Pterygota	7496	Amphiesmenoptera	85604	Lepidoptera	7088	Glossata	41191	Noctuoidea	37570	Noctuidae	7100	Amphipyrinae	95182	Spodoptera	7106	NA	NA	Spodoptera litura	69820
	Pieris rapae	Pieris rapae	Eukaryota	2759	Metazoa	33208	NA	NA	Arthropoda	6656	Hexapoda	6960	NA	NA	Insecta	50557	Pterygota	7496	Amphiesmenoptera	85604	Lepidoptera	7088	Glossata	41191	Papilionoidea	37572	Pieridae	7114	Pierinae	42449	Pieris	7115	NA	NA	Pieris rapae	64459
	Locusta migratoria	Locusta migratoria	Eukaryota	2759	Metazoa	33208	NA	NA	Arthropoda	6656	Hexapoda	6960	NA	NA	Insecta	50557	Pterygota	7496	NA	NA	Orthoptera	6993	Caelifera	7001	Acridoidea	92621	Acrididae	7002	Oedipodinae	27549	Locusta	7003	NA	NA	Locusta migratoria	7004
	Frankliniella occidentalis	Frankliniella occidentalis	Eukaryota	2759	Metazoa	33208	NA	NA	Arthropoda	6656	Hexapoda	6960	NA	NA	Insecta	50557	Pterygota	7496	NA	NA	Thysanoptera	30262	Terebrantia	38130	Thripoidea	45049	Thripidae	45053	Thripinae	153976	Frankliniella	45059	NA	NA	Frankliniella occidentalis	133901
	Marsupenaeus japonicus	Marsupenaeus japonicus	Eukaryota	2759	Metazoa	33208	NA	NA	Arthropoda	6656	Crustacea	6657	Multicrustacea	2172821	Malacostraca	6681	Eumalacostraca	72041	Eucarida	6682	Decapoda	6683	Dendrobranchiata	6684	Penaeoidea	111520	Penaeidae	6685	NA	NA	Penaeus	133894	NA	NA	Penaeus japonicus	27405
	Penaeus monodon	Penaeus monodon	Eukaryota	2759	Metazoa	33208	NA	NA	Arthropoda	6656	Crustacea	6657	Multicrustacea	2172821	Malacostraca	6681	Eumalacostraca	72041	Eucarida	6682	Decapoda	6683	Dendrobranchiata	6684	Penaeoidea	111520	Penaeidae	6685	NA	NA	Penaeus	133894	NA	NA	Penaeus monodon	6687


**Warning**

The reason for providing the two columns (`user_taxa` and `taxa_searched`) are,
sometimes a user input taxon may correspond to multiple NCBI taxa (probably belonging to different clades). When this happens, the lineage for all each taxon will be output, you MUST check this carefully!


## 5 Problems
### Your HOME directory runs out of space when downloading and installing the NCBI Taxonomy database during the first time using of this program.

The error message can be:

	sqlite3.OperationalEoor: disk I/O error

This is caused by `ete3` which will create a directory `~/.etetoolkit` to store the databse (ca. 500M), however, your HOME directory does not have enough space left.

*Solutions:*    
The solution is obvious.   

1. create a directory somewhere else that have enough space left:

		$ mkdir /other/place/myetetoolkit


2. remove the directory `~/.etetoolkit`  created by `ete3`:

		$ rm -rf ~/.etetoolkit
	

3. link your new directory to the HOME directory:

		$ ln -s /other/place/myetetoolkit ~/.etetoolkit

4. run the program again:

		$ taxaranks my_taxonomy_list outfile

This way, ete3 should work as expected.


### Update the NCBI taxonomy database
For more details, refer to `http://etetoolkit.org/docs/latest/tutorial/tutorial_ncbitaxonomy.html`.

1. open a console, and type

		$ python3

	You will enter the Python3 command line status.

2. excute following commands in Python3

		>from ete3 import NCBITaxa
		>ncbi = NCBITaxa()
		>ncbi.update_taxonomy_database()


## 6 Citations

	Guanliang Meng, Yiyuan Li, Chentao Yang, Shanlin Liu,
	MitoZ: a toolkit for animal mitochondrial genome assembly, annotation and visualization,
	Nucleic Acids Research,
	https://doi.org/10.1093/nar/gkz173



Besides, since `taxonomy-ranks` makes use of the `ete3` toolkit, you should also cite it if you use `taxonomy-ranks` in your publications. 

	ETE 3: Reconstruction, analysis and visualization of phylogenomic data.
	Jaime Huerta-Cepas, Francois Serra and Peer Bork. 
	Mol Biol Evol 2016; doi: 10.1093/molbev/msw046

Please go to `http://etetoolkit.org/` for more details.

## 7 Author

Guanliang MENG. 

linzhi2012\<MitoZ\>gmail\<MitoZ\>com




