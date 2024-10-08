# ArborView: Changelog


## Unreleased

### Added ability to select and copy text in a tree

- The SVG text is not selectable and could be copied. This makes it easy for researchers to highlight elements of interest such as accession number, etc. This is both valid for interactive mode and even during SVG image exports [PR 8](https://github.com/phac-nml/ArborView/pull/8). Speciicaly, the text selection cursor symbol changes from hand (before) to a pipe symbol (`|`) when mouse over the text in both the webapp tree and SVG exported image. Injected the CSS style in the `<svg>` tag which is much safer and permanent solution available for both SVG image exports and webapp

### `Added`
- Added text selection of tree text including distance values and leaf nodes text in both webapp and SVG image exports [PR 8](https://github.com/phac-nml/ArborView/pull/8)
- Metadata fields have been added to inner and outer node labels. [PR 4](https://github.com/phac-nml/ArborView/pull/3)

- Cladeogram tree layout. [PR 2](https://github.com/phac-nml/ArborView/pull/2)

- Added slider for adjusting line thickness. [PR 5](https://github.com/phac-nml/ArborView/pull/5)
