import unittest

from labs.subsrt_with_concatenation_of_all_words import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        result = Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])
        self.assertEqual(sorted(result), [0, 9])

    def test_2(self):
        result = Solution().findSubstring("wordgoodgoodgoodbestword",
                                          ["word", "good", "best", "word"])
        self.assertEqual(result, [])

    def test_3(self):
        result = Solution().findSubstring("barfoofoobarthefoobarman",
                                          ["bar", "foo", "the"])
        self.assertEqual(sorted(result), [6, 9, 12])

    def test_4(self):
        result = Solution().findSubstring("foobarfoobar", ["foo", "bar"])
        self.assertEqual(sorted(result), [0, 3, 6])

    def test_5(self):
        result = Solution().findSubstring("aaaaaaaaaaaaaa", ["aa", "aa"])
        self.assertEqual(sorted(result), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # def test_6(self):
    #     result = Solution().findSubstring(
    #         "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel",
    #         ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty",
    #          "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj", "lnle", "sefg",
    #          "vimw", "bxcb"])
    #     self.assertEqual(sorted(result), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()
