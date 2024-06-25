[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-green)](https://www.apache.org/licenses/LICENSE-2.0)

# ArborView

- [Introduction](#introduction)
  * [Citation](#citation)
  * [Contact](#contact)
- [Install](#install)
    + [Compatibility](#compatibility)
- [Getting Started](#getting-started)
  * [Usage](#usage)
  * [Data Input](#data-input)
  * [Data Output](#data-output)
- [Legal and Compliance Information](#legal-and-compliance-information)
- [Updates and Release Notes](#updates-and-release-notes)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Introduction

Phylogenetic trees are powerful tools in a biologist's arsenal, as they enable researchers to determine the evolutionary relationships between organisms, genes or proteins of interest. From a public health perspective, phylogenies are frequently used in conjuction with sample metadata and genetic distance thresholds to inform further action in potential outbreak scenarios. Although there are numerous programs available for visualizing phylogenies, such as [ggtree](https://bioconductor.org/packages/release/bioc/html/ggtree.html), [the Interactive Tree of Life (iTOL)](https://itol.embl.de/) and [TreeViewer](https://treeviewer.org/), they were not designed or optimized for use in a public health context. These programs provide numerous ways to customize the visualization of phylogenetic data, but they lack the ability to efficiently integrate additional contextual data that is key for timely decision making during potential outbreak events.

ArborView was designed to visualize phylogenetic trees with associated sample metadata to facilitate rapid data interpretation. It is executable with no installation or dependencies, and has a intuitive, clean graphical user interface (GUI), increasing its accessibility to users with a minimal background in bioinformatics.

## Citation

Wells, Matthew, Bessonov, Kyrylo, Reimer, Aleisha, Cook, Matthew, Deecker-Simon, Shayna, Robertson, James, Peterson, Christy-Lynn. ArborView.

## Contact

For any questions, issues or comments please make a Github issue or reach out to [**Matthew Wells**](matthew.wells@phac-aspc.gc.ca).

# Install

ArborView has no installation or dependancy requirements. It can be deployed as a static page by [**clicking here**](http://daad.pages.cscscience.ca/ArborView/).

### Compatibility

ArborView is compatible with Windows and Linux operating systems.

# Getting Started

## Usage

The ArborView application can be divided into three panes: 1) the tree editor; 2) the metadata editor ; and 3) the program functions.

### Tree Editor

The tree editor is where the phylogeny is visualized within the center portion of the screen.

Clicking on the external light grey node(s) at the end of the branches will add them to the selection list so the user can quickly filter the associated metadata for the sample using the `Filter data` button.

Clicking on the internal dark grey node(s) enables the user to select from one of three options:
1) Collapse/Uncollapse branch: Hides all of the branches associated with the node. They can be displayed again by re-selecting the node in question and uncollapsing the branch, or by using the `Redraw tree` button.
2) Display sub-tree: Uses the selected node as the pseudo-"root" of the tree, enabling the user to "zoom-in" on a clade of interest. The full tree can be displayed again by using the `Redraw tree` button.
3) Select all children: Adds all of the external nodes associated with the clade to the selection list.

### Metadata Editor

The metadata editor enables users to view and edit the metadata associated with the phylogeny to add additional contextual information to the analysis. This function also enables the user to quickly and efficiently make changes to the metadata, without needing to open and edit it in a separate program.

For example:
- A phylogeny is coloured by the "National Outbreak Code" column in the associated sample metadata, and the user notices there is an unassigned sample that is clustering with a specific outbreak.
- The user can filter the metadata for that specific sample, and can add the national outbreak code directly to that sample's metadata.
- The edited metadata can then be downloaded via the `Export Full Table` button.

### Program Functions

The program functions are denoted by the buttons present on the left-hand portion of the screen.

| Program Button | Description |
| :--- | :--- |
| `Upload Newick` | Uploads a Newick file formatted phylogeny for visualization. |
| `Upload Metadata` | Uploads a tab-delimited metadata file to add additional contextual information to the phylogeny. |
| `Export IDs` | Exports a list of IDs that correlate to the user-selected nodes of interest on the phylogeny. |
| `Export SVG` | Exports the phylogeny as a SVG file. |
| `Export PNG` | Exports the phylogeny as a PNG file. |
| `Export Full Table` | Exports the metadata table as a tab-delimited file. |
| `Export Filtered Table` | Exports the filtered metadata table as a tab-delimited file. |
| `Redraw Tree` | Re-builds the phylogeny using the original Newick File. |
| `Refocus Tree` | Adjusts the view within the tree editor pane so the entire phylogeny is centered and visible on the screen. |
| `Zoom` | Enables the user to manually adjust the view of the phylogeny within the tree editor. |
| `Layout` | Enables the user to select if the tree is visualized as rectangular (left on slider), hierarchical (center on slider) or circular (right on slider). |
| `Legend` | If using colour coding, it shows ("on") or hides ("off") the legend. |
| `Branch lengths` | Shows ("on") or hides ("off") the branch length values. |
| `Colour tree by column` | Enables the user to quickly colour the nodes on the tree using a column selected from the associated metadata. If the legend is turned on, the user can click on the boxes to customize the colours that are used for the visualization (as opposed to using the pre-set colour options). |
| `Filter data` | If a node is selected from the tree using the tree editor, the user can use this button to quickly filter the associated metadata for the sample. |
| `Clear nodes` | Clears the selected nodes from the tree editor. Note this does not remove the nodes, but simply unselects them so other nodes may be selected for further filtering. |
| `Clear Filters` | Enables the user to clear any filters they may have set on the tree. |

## Data Input

### Phylogenetic tree

- Must be in the Newick file format.

### Metadata

| sample_id  | serovar  | mlst_st  | earliest_date  | state_province | source_type | source_site | age | sex | reported_id | national_outbreak_code |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S1 | Enteritidis | 11.0  | 2021-06-19  | ON  | Human  | Stool  | 20 | F | Salmonella | None |
| S2 | Enteritidis | 11.0  | 2006-01-03  | QC  | Animal  | Chicken  | 52 | M | Salmonella | None |

- Metadata associated with samples present in the phylogenetic tree.

- Must be in a tab-delimed file format, with the header as the first line and `sample_id` as the first column.

- Additional metadata fields that could be useful from a public health perspective are shown in the above sample; however, this does not represent an exhaustive list.

## Data Output

- Phylogenetic trees that are visualized in ArborView can be exported as either PNG or SVG files.

- It is also possible to export both the full metadata table and a filtered metadata table as tab-delimited files.

# Legal and Compliance Information

Copyright Government of Canada 2024

Written by: National Microbiology Laboratory, Public Health Agency of Canada

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License. You may obtain a copy of the License at:

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

# Updates and Release Notes

Please see the `CHANGELOG.md`.
=======


