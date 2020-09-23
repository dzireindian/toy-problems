from LRU import lru

class lru_test:

    def testcases(self):
        a = lru(3)
        a.put("google")
        assert a.get("google") != None,"testcase 1 failed"
        print("testcase 1 passed")

        a.put("amazon")
        assert a.get("amazon") != None,"testcase 2 failed"
        print("testcase 2 passed")

        a.put("github")
        assert a.get("github") != None,"testcase 3 failed"
        print("testcase 3 passed")

        a.put("google")
        assert a.get("google") != None,"testcase 4 failed"
        print("testcase 4 passed")

        print("All testcases passed")

        lst = a.get_cache()
        for i in lst:
            print(i)

a = lru_test()
a.testcases()
