from src.pybridgeclient import PyBridge


def test_with_url():
    base_url = "http://0.0.0.0:8000/"
    headers = {
        "Authorization": "Bearer xxxxxxxx"}
    py_bridge = PyBridge(base_url, headers)
    items = py_bridge.items()
    item_detail = py_bridge.item_detail(item_id=1)
    create_item = py_bridge.item(name="item", description="description", amount=123)
    update_item = py_bridge.update_item(item_id=1, name="item", description="description", amount=123)
    print(items.json())
    print(item_detail.json())
    print(create_item.json())
    print(update_item.json())
