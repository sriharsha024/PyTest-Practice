def test_argtest_01(cmdopt):
    """
    Test to verify that the configuration file
    contains the keyword 'Lab'.
    """

    # Read a single line from the CmdOpt input (file/stream)
    line = cmdopt.readline()

    # Assert that the word 'Lab' exists in the line
    # .index() will raise ValueError if 'Lab' is not found
    assert "Lab" in line
