def pytest_addoption(parser):

    # browser type
    parser.addoption('--browse', action='store', default='chrome',
                     help='browse type such as chrome')
    # find element timeout time
    parser.addoption('--eleto', action='store', default=10,
                     help='timeout of find element')
    parser.addoption("--ALL", action="store_true",
                     help="run all combinations")




