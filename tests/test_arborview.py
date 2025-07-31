import re, pytest, time
from playwright.sync_api import Page, expect


def test_load_newick_phylo_tree(page: Page) -> None:
    page.goto("../html/table.html")

    # we first wait for the file chooser dialog to appear
    # before clicking the button that triggers it.
    with page.expect_file_chooser() as fc_info:
        # Click on the button that opens the file dialog
        page.locator("#tree-upload-button").click()

    file_chooser = fc_info.value
    
    # Now, set the files on the file chooser itself.
    # This is the correct way to handle hidden or styled file inputs.
    file_chooser.set_files("example/test_phylo_tree_with_bootstrap_values.nwk")
    
    tree_svg_element = page.locator("#TreeSVG")
    expect(tree_svg_element).to_be_visible()
  

    root_node_text_element = page.locator("#TreeSVG g[transform=\"translate(0, 0)\"] text").nth(0)
    expect(root_node_text_element).to_have_text("0")

    scale_bar_element = page.locator("#scale-bar-group text").nth(0)
    expect(scale_bar_element).to_have_text("0")

