from q_python.lamp import Lamp


def test_lamp():
    lamp = Lamp(False)

    assert lamp.is_on() is False

    lamp.on()

    assert lamp.is_on() is True

    lamp.off()

    assert lamp.is_on() is False
