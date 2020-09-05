import unittest

from HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./", pattern="login*")

with open("./report/report.html", "wb") as f:
    HTMLTestRunner(stream=f).run(suite)

