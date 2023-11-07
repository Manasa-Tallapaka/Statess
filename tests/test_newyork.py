from States.NewYork import NewYork

NewYork_network = NewYork("regional", "unlimited")
def test_att_info():
    att_states = NewYork("regional", "special")
    assert att_states.get_info() == "Time Square is the busiest place in NewYork"