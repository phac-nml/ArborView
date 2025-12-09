
## Scripts

This directory contains utility scripts to extend ArborView's functionality.


### `inline_arborview.py`: Embed Data Directly into ArborView HTML

This script embeds your Newick tree and metadata TSV directly into an ArborView HTML file. This eliminates the need for users to upload data manually in the browser — making the visualization file fully self-contained and ready to share or host.

#### Example usage
To embed a newick file `tree.nwk` and metadadta `metadata.tsv` in Arborview represented by the `table.html`, one could simply run
`python inline_arborview.py -d metadata.tsv -n tree.nwk -t ./table.html -o embedded_tree.html`. This would generate a `embedded_tree.html` file where newick string will be injected into the `const TREE` and metadata in `const DATA` global variables.
