from States.Missouri import Missouri

Missouri = Missouri("nationwide", "fast")
def test_Missouri_info():
    Missouri_states = Missouri("location", "special")
    assert Missouri_states.get_info() == "Missouri is the land of Geospatial Research"