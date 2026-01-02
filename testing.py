def test_parse_items():
    html = """
    <div class="item">
        <span class="title">Sample</span>
        <span class="price">$10</span>
    </div>
    """
    results = parse_items(html)
    assert results[0]["title"] == "Sample"
