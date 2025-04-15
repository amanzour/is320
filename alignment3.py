# Created by Molly - Group 3
def suggest_network_update(building_name):
    """
    Returns a suggested router upgrade plan for a given building.
    """
    upgrades = {
        "Donovan Hall": "Install dual-band mesh routers with 5GHz support.",
        "Student Center": "Add new access points and upgrade existing cabling.";
        "Cayan Library": "Upgrade to Wi-Fi 6E routers with 3 access points per floor."
    }
    return upgrades.get(building_name, "No recommendation available. Needs site survey.")