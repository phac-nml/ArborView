import os, pytest, logging
from playwright.sync_api import Page, expect

LOG = logging.getLogger(__name__)

@pytest.fixture
def page(page: Page) -> Page:
    """
    A Pytest fixture that sets up the page for all subsequent tests.
    It navigates to the html/table.html file before each test.
    """
    # This is a robust way to handle local file paths, ensuring it works
    # regardless of where the test is executed from.
    LOG.info("Opening the webapp html/table.html page ...")
    # Set the viewport size (resolution) for the browser window
    page.set_viewport_size({"width": 1440, "height": 900}) 
    page.goto(f"file:///{os.path.abspath('html/table.html')}")
    

    yield page

def test_load_newick_phylo_tree_and_metadata(page: Page) -> None:
 
    with page.expect_file_chooser() as fc_info:
        # Click on the button that opens the file dialog
        page.locator("#tree-upload-button").click()

    file_chooser = fc_info.value
    
    # Now, set the files on the file chooser itself.
    # This is the correct way to handle hidden or styled file inputs.
    file_chooser.set_files("example/test_phylo_tree_with_bootstrap_values.nwk")
    
    tree_svg_element = page.locator("#TreeSVG")
    expect(tree_svg_element).to_be_visible()
  
    #test if the root of the tree starts with zero value
    root_node_text_element = page.locator("#TreeSVG g[transform=\"translate(0, 0)\"] text").nth(0)
    expect(root_node_text_element).to_have_text("0")

    #check if scale bar starts from zero
    scale_bar_element = page.locator("#scale-bar-group text").nth(0)
    expect(scale_bar_element).to_have_text("0")

    # Locate the checkbox input associated with the toggle.
    toggle_checkbox = page.locator("div.toggle:has(#inner_node_labels_toggle)")
    # Click the toggle button to activate inner labels
    toggle_checkbox.click()

    inner_node_labels = page.locator("#TreeSVG .inner-node-label")

    LOG.info(f"Found {inner_node_labels.count()} inner node labels. Checking if they are all visible or not")
    assert inner_node_labels.count() > 0, "Expected at least one inner node label, but found none."

    for i in range(inner_node_labels.count()):
        label = inner_node_labels.nth(i)
        expect(label).to_be_visible()

    LOG.info("All bootstrap values are visible and test passed")  

    

def test_select_nodes_in_a_tree(page: Page) -> None:

    with page.expect_file_chooser() as fc_info:
        # Click on the button that opens the file dialog
        page.locator("#tree-upload-button").click()

    file_chooser = fc_info.value
    
    # Now, set the files on the file chooser itself.
    # This is the correct way to handle hidden or styled file inputs.
    file_chooser.set_files("example/ultrametric_simple_tree.nwk")


    # Wait for the file chooser dialog to appear, then click the upload button
    
    with page.expect_file_chooser() as fc_info_meta:
        LOG.info("Loading metadata table now ...")
        # Click on the button that opens the file dialog for metadata.
        # This targets the <label> element that visually acts as the button.
        page.locator("#metadata-selector-input").click() 

    file_chooser_meta = fc_info_meta.value
    
    # Set the files on the file chooser.
    file_chooser_meta.set_files("example/ultrametric_simple_tree_metadata.tsv")

    page.get_by_text("B", exact=True).nth(1).click()
    page.get_by_text("A", exact=True).nth(1).click()
    page.get_by_text("T", exact=True).nth(1).click()


    selected_nodes_div = page.locator("#SelectedNodes")
    expect(selected_nodes_div).to_be_visible()


    selected_node_elements = selected_nodes_div.locator(".selected-node")

    # Assert that there are exactly 3 such elements
    expect(selected_node_elements).to_have_count(3)

    text_contents=[]
    for i in range(selected_node_elements.count()):
        text_element = selected_node_elements.nth(i).locator("div.flex-grow-1").text_content()
        if text_element:
            text_contents.append(text_element)

    LOG.info(f"The text contents of the selected nodes is {text_contents}")
    assert sorted(text_contents) == ["A", "B", "T"]

    remove_buttons = selected_nodes_div.locator(".selected-node button.btn-danger")

    for i in range(remove_buttons.count()):
        # Re-locate the button as the DOM might change after each click
        # We always click the first available button, as they shift up
        remove_buttons.first.click()
    expect(selected_node_elements).to_have_count(0)  

    page.wait_for_timeout(3000) #3s wait time
    #assert if metadata values are visible 
    expect(page.locator("#metadata")).to_be_visible()
    expect(page.locator("#metadata tbody tr")).to_have_count(10) 
  
   
