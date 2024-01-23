import codewars_test as test
from solution import reverse_words

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
        test.assert_equals(reverse_words('apple'), 'elppa')
        test.assert_equals(reverse_words('a b c d'), 'a b c d')
        test.assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')