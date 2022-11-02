taxaranks_parallel(){

    ## stop after error
    set -e
    
    ## get current directory
    current_dir=$(pwd)
    
    ##parse the input path
    input=$1
    dir=$(dirname $input|xargs realpath)
    base=$(basename $input)
    real_input="${dir}/${base}"
    echo "Input is $input."
    
    ## go to sub_dir
    sub_dir="${dir}/split_${base}"
    rm -rf $sub_dir; mkdir -p $sub_dir
    cd $sub_dir
    echo "Create temporary directory $sub_dir."
    
    ## get parameters for spliting, then split
    total_line=$(cat $real_input|wc -l )
    threads=$(nproc)
    need_length=3
    split -a $need_length -d -n "l/${threads}" $real_input
    echo "Have $threads threads, split the file to $threads parts."
    
    ## run taxaranks in parallel
    echo "Annotating..."
    ls .|parallel "taxaranks -i {} -o {}.lineage -t"
    
    ## merge
    merge_file="../${base}.lineage"
    merge_file_with_head="../${base}.lineage.with_head"
    
    #### drop the first line for each file, then merge
    rm -rf $merge_file;ls *.lineage|parallel "awk 'NR>1 {print}' {} &>> $merge_file"
    
    #### add the first line for the merge file
    head_line=$(ls *.lineage|head -n1|xargs head -n1)
    awk -v a="$head_line" 'BEGIN{print a} {print $0}' $merge_file &>$merge_file_with_head
    rm -rf $merge_file;mv $merge_file_with_head $merge_file
    
    ## remove the sub_dir
    rm -rf $sub_dir
    echo "Clear temporary directory."
    
    ## back to the previous working directory
    cd $current_dir
    
    ## prompt
    echo "All finished."
}
