from pathlib import Path
import shutil


def on_page_markdown(markdown, page, config, files):
    catalog_index = Path("docs/examples/web_catalog/index.html")
    catalog_data = Path("docs/examples/web_catalog/data.json")
    if page.file.src_path != "README.md":
        return markdown

    if not (catalog_index.is_file() and catalog_data.is_file()):
        return markdown.replace(
            "<!-- mkdocs:iframe -->",
            "> The inherited web-catalog preview is not generated in this review build. "
            "Generate and review it separately before including it in retained evidence.",
        )

    iframe = """

<div align="center" style="position: relative;">
    <button onclick="window.open('examples/web_catalog/index.html', '_blank')" style="position: absolute; top: -40px; right: 10px; z-index: 1000; padding: 8px; background: #000; color: #fff; border: none; border-radius: 4px; cursor: pointer; display: flex; align-items: center; justify-content: center;">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
            <polyline points="15 3 21 3 21 9"></polyline>
            <line x1="10" y1="14" x2="21" y2="3"></line>
        </svg>
    </button>
    <iframe src="examples/web_catalog/index.html" frameborder="0"></iframe>
    <br><br>
</div>
    """
    return markdown.replace("<!-- mkdocs:iframe -->", iframe)


def on_post_build(config):
    source = Path("docs/examples/web_catalog/data.json")
    if not source.is_file():
        return

    destination = Path(config["site_dir"]) / "data.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
